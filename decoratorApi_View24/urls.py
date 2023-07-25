from django.urls import path
from decoratorApi_View24 import views


urlpatterns = [
    path('books24/', views.Book_list_create_api_view24),
    path('books24/<int:id>/', views.Book_retrieve_update_delete_api_view24),
]