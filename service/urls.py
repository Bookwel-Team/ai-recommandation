from django.urls import path

from service.ajax import get_recommendations, extract_info_from_pdf

urlpatterns = [
   path("recommandation/", get_recommendations, name="get_recommendations"),
   path("pdf/", extract_info_from_pdf, name="extract_info_from_pdf"),
]
