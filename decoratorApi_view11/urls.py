from django.urls import path
from decoratorApi_view11 import views



urlpatterns = [
    path('books11/', views.Book_list_create_api_view11),
    path('books11/<int:id>/', views.Book_retrieve_update_delete_api_view11),
]