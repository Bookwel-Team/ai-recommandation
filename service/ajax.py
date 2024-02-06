import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST


@require_POST
def get_recommendations(request, user_id):
    try:
        request_body = request.body.decode('utf-8')
        data = json.loads(request_body)

        user_books = data.get('user_books', [])
        books = data.get('books', [])
        recommendations = []

        for user_book in user_books:
            category = user_book.get('category')
            author = user_book.get('author')

            similar_books = [book for book in books if book.get('category') == category
                             and book.get('author') == author]

            recommendations.extend(similar_books)

        return JsonResponse({"recommendations": recommendations})

    except json.JSONDecodeError as e:
        return JsonResponse({"error": f"Invalid JSON in request body: {e}"}, status=400)