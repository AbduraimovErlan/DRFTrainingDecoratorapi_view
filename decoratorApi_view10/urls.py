from django.urls import path
from decoratorApi_view10 import views


urlpatterns = [
    path('books10/', views.Book_list_create_api_view10),
    path('books10/<int:id>/', views.Book_retrieve_update_delete_api_view10),
]