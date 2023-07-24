from django.urls import path
from decoratorApi_view18 import views


urlpatterns = [
    path('books18/', views.Book_list_create_api_view18),
    path('books18/<int:id>/', views.Book_retrieve_update_delete_api_veiw18),

]