from django.urls import path
from decoratorApi_view7 import views


urlpatterns = [
    path('books7/', views.Book_list_create_api_view),
    path('books7/<int:id>/', views.Book_retrieve_update_delete_api_veiw),
]