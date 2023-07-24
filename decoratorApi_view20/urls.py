from django.urls import path
from decoratorApi_view20 import views


urlpatterns = [
    path('books20/', views.Book_list_create_api_view20),
    path('books20/<int:id>/', views.Book_retrieve_update_delete_api_view20),
]