from django.urls import path

from service import ajax
from service.ajax import get_recommendations

urlpatterns = [
   path("(?P<user_id>[0-9]+)/recommandation/", get_recommendations, name="get_recommendations"),
]
