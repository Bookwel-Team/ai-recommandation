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

        user_books = data.get('user_books', [])
        all_books = data.get('books', [])
        recommendations = []

        for user_book in user_books:
            user_category = user_book.get('category', {})
            user_author = user_book.get('author', '')
            user_reactions = user_book.get('user_reaction', '')
            user_id = user_book.get('user_id', '')

            # liked_books = [ub for ub in all_books if ub.get('user_id') == user_id and 'LIKE' in user_reactions]
            liked_books = filter(lambda ub: ub.get('user_id') == user_id and 'LIKE' in user_reactions, all_books)
            # disliked_books = [ub for ub in all_books if ub.get('user_id') == user_id and 'DISLIKE' in user_reactions]
            disliked_books = filter(lambda ub: ub.get('user_id') == user_id and 'LIKE' in user_reactions, all_books)

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
                        book in liked_books and
                        book not in disliked_books and
                        book.get('category', {}).get('id') == user_category.get('id') or
                        book.get('author', "") == user_author
                )
            ]

            recommendations.extend(similar_books)

        return JsonResponse({"recommendations": recommendations})

    except json.JSONDecodeError as e:
        return JsonResponse({"error": f"Invalid JSON in request body: {e}"}, status=400)
