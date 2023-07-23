from django.urls import path
from decoratorApi_view2 import views



urlpatterns = [
    path('books2/', views.Book_list_create_api_view2),
    path('books2/<int:id>/', views.Book_retrieve_update_delete2),
]