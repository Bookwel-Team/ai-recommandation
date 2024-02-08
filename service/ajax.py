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
        recommendations = []

        for user_book in user_books:
            user_category = user_book.get('category', {})
            user_reactions = user_book.get('user_reaction', '')

            liked_books = list(filter(lambda ub: 'LIKE' in user_reactions, all_books))
            disliked_books = list(filter(lambda ub: 'DISLIKE' in user_reactions, all_books))

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
                        book not in disliked_books and
                        book in liked_books and
                        book.get('category', {}).get('id') == user_category.get('id')
                )
            ]

            recommendations.extend(similar_books)

        return JsonResponse({"recommendations": recommendations})

    except json.JSONDecodeError as e:
        return JsonResponse({"error": f"Invalid JSON in request body: {e}"}, status=400)
