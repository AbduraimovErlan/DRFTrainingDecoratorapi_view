from django.urls import path
from decoratorApi_view4 import views



urlpatterns = [
    path('books4/', views.Book_list_create_api_view4),
    path('books4/<int:id>/', views.Book_retrieve_update_delete_api_view4),
]