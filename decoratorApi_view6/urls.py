from django.urls import path
from decoratorApi_view6 import views


urlpatterns = [
    path('books6/', views.Book_list_create_api_view6),
    path('books6/<int:id>/', views.Book_retrieve_update_delete),
]