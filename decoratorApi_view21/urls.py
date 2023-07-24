from django.urls import path
from decoratorApi_view21 import views


urlpatterns = [
    path('books21/', views.Book_list_create_api_view21),
    path('books21/<int:id>/', views.Book_retrieve_update_delete_api_view21),
]