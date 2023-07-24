from django.urls import path
from decoratorApi_view17 import views


urlpatterns = [
    path('books17/', views.Book_list_create_api_view),
    path('books17/<int:id>/', views.Book_retrieve_update_delete_api_view),
]