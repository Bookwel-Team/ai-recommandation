import json


from django.http import JsonResponse
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
        user_categories = data.get('user_categories', [])

        recommendations = []

        liked_categories = list(
            map(lambda cat: cat['id'], filter(lambda cat: cat.get('userReaction') == 'LIKE', user_categories)))
        disliked_categories = list(
            map(lambda cat: cat['id'], filter(lambda cat: cat.get('userReaction') == 'DISLIKE', user_categories)))

        for user_book in user_books:
            book_author = user_book.get('author', '')
            user_category = user_book.get('category', {})
            user_reaction = user_book.get('userReaction', '')

            liked_books = list(filter(lambda ub: 'LIKE' in user_reaction, all_books))
            disliked_books = list(filter(lambda ub: 'DISLIKE' in user_reaction, all_books))

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
                    and book.get("category", {}).get("id") not in disliked_categories
                    and book.get("category", {}).get("id") in liked_categories
                    and (
                        book.get('category', {}).get('id') == user_category.get('id')
                        or book.get('author') == book_author
                    )
                )
            ]

            disliked_liked_books = [
                book for book in disliked_books
                if book.get('author') == book_author and book.get('category', {}).get('id') not in disliked_categories
            ]

            recommendations.extend(similar_books)

            if disliked_liked_books:
                recommendations.extend(disliked_liked_books)

        return JsonResponse({"recommendations": recommendations})

    except json.JSONDecodeError as e:
        return JsonResponse({"error": f"Invalid JSON in request body: {e}"}, status=400)


@csrf_exempt
@require_POST
def extract_info_from_pdf(request):
    pdf_content = request.FILES.get('pdf-content')
    reader = pdf_content.read()
    meta = reader.metadata
    author = meta.get('author')
    title = meta.get('title')

    try:
        if pdf_content:
            with pdf_content:
                return JsonResponse({"title": title, "author": author})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)