import base64
import io
import json

import fitz
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt


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
            book_author = user_book.get('author', '')
            user_category = user_book.get('category', {})
            user_reactions = user_book.get('userReaction', '')

            liked_books = list(filter(lambda ub: 'LIKE' in user_reactions, all_books))
            disliked_books = list(filter(lambda ub: 'DISLIKE' in user_reactions, all_books))

            similar_books = [
                {
                    "id": book.get("id"),
                    "title": book.get("title"),
                    "author": book.get("author"),
                    "category": book.get("category"),
                    "filename": book.get("filename"),
                }
                for book in all_books
                if (
                    book not in disliked_books
                    and book in liked_books
                    and (
                        book.get('category', {}).get('id') == user_category.get('id')
                        or book.get('author') == book_author
                    )
                )
            ]

            recommendations.extend(similar_books)

        return JsonResponse({"recommendations": recommendations})

    except json.JSONDecodeError as e:
        return JsonResponse({"error": f"Invalid JSON in request body: {e}"}, status=400)


@csrf_exempt
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

                return JsonResponse({"title": title, "author": author})

    except Exception as e:
        return HttpResponseBadRequest(f"Error extracting information from PDF: {e}")
