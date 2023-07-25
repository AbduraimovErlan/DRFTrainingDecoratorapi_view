from django.urls import path
from decoratorApi_View25 import views

urlpatterns = [
    path('books25/', views.Book_list_create_api_view25),
    path('books25/<int:id>/', views.Book_retrieve_update_delete_api_view25),
]