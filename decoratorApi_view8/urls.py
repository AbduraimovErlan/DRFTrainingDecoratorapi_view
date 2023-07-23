from django.urls import path
from decoratorApi_view8 import views


urlpatterns = [
    path('books8/', views.Book_list_create_api_view8),
    path('books8/<int:id>/', views.Book_retrieve_update_delete_api_view8),
]