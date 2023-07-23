from django.urls import path
from decoratorApi_view13 import views


urlpatterns = [
    path('books13/', views.Book_list_create_api_view13),
    path('books13/<int:id>/', views.Book_retrieve_update_delete_api_view13),
]