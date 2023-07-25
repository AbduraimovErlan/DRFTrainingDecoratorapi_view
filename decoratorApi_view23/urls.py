from django.urls import path
from decoratorApi_view23 import views

urlpatterns = [
    path('books23/', views.Book_list_create_api_view23),
    path('books23/<int:id>/', views.Book_retrieve_update_delete_api_view23),
]