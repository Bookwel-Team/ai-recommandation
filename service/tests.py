from django.test import TestCase, Client
import json

from django.urls import reverse


class RecommendationsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_recommendations(self):
        user_books = [
            {
                "category": {"id": "1"},
                "author": "John Doe",
                "user_reaction": "LIKE",
                "user_id": "123",
            }
        ]
        all_books = [
            {
                "id": "1",
                "title": "Book 1",
                "author": "John Doe",
                "category": {"id": "1"},
                "file_link": "link1",
            },
            {
                "id": "2",
                "title": "Book 2",
                "author": "Jane Smith",
                "category": {"id": "2"},
                "file_link": "link2",
            },
        ]

        payload = {
            "books": user_books,
            "all_books": all_books,
        }
        json_payload = json.dumps(payload)

        endpoint_url = reverse('get_recommendations')

        response = self.client.post(endpoint_url, data=json_payload, content_type='application/json')

        print(response.content)

        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.content)

        self.assertIn('recommendations', response_data)

