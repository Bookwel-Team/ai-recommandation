import base64

from django.test import TestCase, Client
import json

from django.urls import reverse


class RecommendationsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_recommendations(self):
        user_books = [
            {
                "id": "1",
                "title": "Book 1",
                "author": "John Doe",
                "category": {
                    "id": "1",
                    "name": "adventure"
                },
                "filename": "link1",
                "userReaction": 'LIKE',
                "userId": "123",
            },
            {
                "id": "2",
                "title": "Book 2",
                "author": "Jane Doe",
                "category": {
                    "id": "2",
                    "name": "mystery"
                },
                "filename": "link2",
                "userReaction": 'DISLIKE',
                "userId": "123",
            }
        ]

        all_books = [
            {
                "id": "1",
                "title": "Book 1",
                "author": "John Doe",
                "category": {
                    "id": "1",
                    "name": "adventure"
                },
                "filename": "link1",
            },
            {
                "id": "2",
                "title": "Book 2",
                "author": "Jane Doe",
                "category": {
                    "id": "2",
                    "name": "mystery"
                },
                "filename": "link2",
            },
            {
                "id": "3",
                "title": "Book 3",
                "author": "Jack Doe",
                "category": {
                    "id": "3",
                    "name": "romance"
                },
                "filename": "link3",
            }
        ]

        payload = {
            "books": user_books,
            "all_books": all_books,
            "user_categories": [{"id": "1", "userReaction": 'LIKE'}, {"id": "2", "userReaction": 'DISLIKE'}]
        }

        json_payload = json.dumps(payload)

        endpoint_url = reverse('get_recommendations')

        response = self.client.post(endpoint_url, data=json_payload, content_type='application/json')

        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.content)

        self.assertIn('recommendations', response_data)
        print(response_data)
        self.assertEqual(len(response_data['recommendations']), 1)  # Adjust based on your expected result


class PdfInfoExtractionTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_extract_info_from_pdf(self):
        sample_pdf_content = base64.b64encode(b"Sample PDF content").decode('utf-8')

        json_payload = {
            "pdf_content": sample_pdf_content
        }

        request_body = json.dumps(json_payload)

        endpoint_url = reverse('extract_info_from_pdf')
        response = self.client.post(endpoint_url, data=request_body, content_type='application/json')

        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.content)

        self.assertIn('title', response_data)
        self.assertIn('author', response_data)
