from django.urls import path
from .api import UserApi
urlpatterns = [
    path('api', UserApi.as_view()),
]