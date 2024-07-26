from django.urls import path
from .api import api

urlpatterns = [
    path('', api.urls),  # Inclua as URLs definidas em api.py
]

