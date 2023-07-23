from django.urls import path
from decoratorApi_view3 import views



urlpatterns = [
    path('books3/', views.Book_list_create_api_view3),
    path('books3/<int:id>/', views.Book_retrieve_updata_delete_api_view3),
]