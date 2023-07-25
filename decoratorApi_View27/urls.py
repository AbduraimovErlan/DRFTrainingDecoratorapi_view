from django.urls import path
from decoratorApi_View27 import views

urlpatterns = [
    path('books27/', views.Book_list_create_api_view),
    path('books27/<int:id>/', views.Book_retrieve_update_delete_api_view),
]