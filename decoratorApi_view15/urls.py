from django.urls import path
from decoratorApi_view15 import views

urlpatterns = [
    path('books15/', views.Book_list_create_api_veiw15),
    path('books15/<int:id>/', views.Book_retrieve_update_delete_api_view15),
]