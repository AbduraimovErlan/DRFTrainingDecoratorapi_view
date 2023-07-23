from django.urls import path
from decoratorApi_view5 import views


urlpatterns = [
    path('books5/', views.Book_list_create_api_view5),
    path('books5/<int:id>/', views.Book_retrieve_update_delete_api_view5),
]