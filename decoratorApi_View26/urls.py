from django.urls import path
from decoratorApi_View26 import views


urlpatterns = [
    path('books26/', views.Book_list_create_api_view),
    path('books26/<int:id>/', views.Book_retrieve_update_delete_api_veiw),
]