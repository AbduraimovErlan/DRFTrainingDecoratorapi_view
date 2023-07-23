from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('decoratorApi_view.urls')),
    path('api/v1/', include('decoratorApi_view2.urls')),
    path('api/v1/', include('decoratorApi_view3.urls')),
    path('api/v1/', include('decoratorApi_view4.urls')),
    path('api/v1/', include('decoratorApi_view5.urls')),
]
