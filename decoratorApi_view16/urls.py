from django.urls import path
from decoratorApi_view16 import views


urlpatterns = [
    path('books16/', views.Book_list_create_api_view16),
    path('books16/<int:id>/', views.Book_retrieve_update_delete_api_view),
]