from django.urls import path
from decoratorApi_view22 import views


urlpatterns = [
    path('books22/', views.Book_list_create_api_view22),
    path('books22/<int:id>/', views.Book_retrieve_update_delete_api_view22),
]