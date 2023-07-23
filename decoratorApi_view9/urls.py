from django.urls import path
from decoratorApi_view9 import views


urlpatterns = [
    path('books9/', views.Book_list_create_api_view9),
    path('books9/<int:id>/', views.Book_retrieve_update_delete_api_view9),
]