from django.urls import path
from . import views



urlpatterns = [
    path('books1/', views.Book_list_create_api_view),
    path('books1/<int:id>/', views.Book_retrieve_update_delete_api_view),
]