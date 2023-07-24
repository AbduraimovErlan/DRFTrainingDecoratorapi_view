from django.urls import path
from decoratorApi_view19 import views

urlpatterns = [
    path('books19/', views.Book_list_create_api_view19),
    path('books19/<int:id>/', views.Book_retrieve_update_delete_api_view19),
]