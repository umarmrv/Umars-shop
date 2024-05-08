
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),  # это кореннивая маршрут главный
    path('shop/', include('shop.urls')),
    path('api/', include('api.urls')),
    path('', include('api.urls'))
]
