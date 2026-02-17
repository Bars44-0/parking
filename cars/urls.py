from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.api_urls')),  # если есть API
    path('accounts/', include('accounts.urls')),         # веб-страницы входа/регистрации
    path('api/vehicles/', include('vehicles.urls')),
]
