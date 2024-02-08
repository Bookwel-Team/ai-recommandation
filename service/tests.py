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
            {
                "id": "456",
                "title": "Book 3",
                "author": "John Peters",
                "category": {"id": "1"},
                "file_link": "link1",
            },
            {
                "id": "4",
                "title": "Book 4",
                "author": "Park Doe",
                "category": {"id": "5"},
                "file_link": "link1",
            },
            {
                "id": "5",
                "title": "Book 5",
                "author": "Jane Doe",
                "category": {"id": "2"},
                "file_link": "link3",
            },
            {
                "id": "456",
                "title": "Book 6",
                "author": "John Doe",
                "category": {"id": "5"},
                "file_link": "link4",
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
