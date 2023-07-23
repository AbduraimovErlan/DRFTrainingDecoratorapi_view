from django.urls import path
from decoratorApi_view12 import views


urlpatterns = [
    path('books12/', views.Book_list_create_api_view12),
    path('books12/<int:id>/', views.Book_retrieve_update_delete_api_view12),
]