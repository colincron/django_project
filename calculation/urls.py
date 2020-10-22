from django.urls import path
from .views import AddToN

urlpatterns = [
    path('', AddToN.as_view(num=100), name="calc"),
]