from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('decoratorApi_view.urls')),
    path('api/v1/', include('decoratorApi_view2.urls')),
    path('api/v1/', include('decoratorApi_view3.urls')),
    path('api/v1/', include('decoratorApi_view4.urls')),
    path('api/v1/', include('decoratorApi_view5.urls')),
    path('api/v1/', include('decoratorApi_view6.urls')),
    path('api/v1/', include('decoratorApi_view7.urls')),
    path('api/v1/', include('decoratorApi_view8.urls')),
    path('api/v1/', include('decoratorApi_view9.urls')),
    path('api/v1/', include('decoratorApi_view10.urls')),
    path('api/v1/', include('decoratorApi_view11.urls')),
    path('api/v1/', include('decoratorApi_view12.urls')),
    path('api/v1/', include('decoratorApi_view13.urls')),
    path('api/v1/', include('decoratorApi_view14.urls')),
    path('api/v1/', include('decoratorApi_view15.urls')),
]
