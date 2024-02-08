import base64
import json

import io

from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from fitz import fitz


@csrf_exempt
@require_POST
def get_recommendations(request):
    try:
        request_body = request.body.decode('utf-8')
        data = json.loads(request_body)

        user_books = data.get('books', [])
        all_books = data.get('all_books', [])
        recommendations = []

        for user_book in user_books:
            user_category = user_book.get('category', {})
            user_author = user_book.get('author', '')
            user_reactions = user_book.get('user_reaction', '')
            user_id = user_book.get('user_id', '')

            liked_books = [ub for ub in all_books if ub.get('user_id') == user_id and 'LIKE' in user_reactions]
            disliked_books = [ub for ub in all_books if ub.get('user_id') == user_id and 'DISLIKE' in user_reactions]

            similar_books = [
                {
                    "id": book.get("id"),
                    "title": book.get("title"),
                    "author": book.get("author"),
                    "category": book.get("category"),
                    "file_link": book.get("file_link"),
                }
                for book in all_books
                if (
                        book.get('category', {}).get('id') == user_category.get('id') or
                        book.get('author', "") == user_author and
                        book in liked_books and
                        book not in disliked_books
                )
            ]

            recommendations.extend(similar_books)

        return JsonResponse({"recommendations": recommendations})

    except json.JSONDecodeError as e:
        return JsonResponse({"error": f"Invalid JSON in request body: {e}"}, status=400)


@require_POST
def extract_info_from_pdf(request):
    try:
        request_body = request.body.decode('utf-8')
        data = json.loads(request_body)

        pdf_content = data.get('pdf_content', None)

        if pdf_content:
            pdf_file = io.BytesIO(base64.b64decode(pdf_content))

            with fitz.open(pdf_file) as pdf_document:
                metadata = pdf_document.metadata

                title = metadata.get('title', None)
                author = metadata.get('author', None)

                return {"title": title, "author": author}

    except Exception as e:
        return {"error": f"Error extracting information from PDF: {e}"}
