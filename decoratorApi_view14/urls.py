from django.urls import path
from decoratorApi_view14 import views


urlpatterns = [
    path('books14/', views.Book_list_create_api_view14),
    path('books14/<int:id>/', views.Book_retrieve_update_delete_api_view14),
]