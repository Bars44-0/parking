from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # <-- здесь путь к accounts
    path('', include('vehicles.urls')),  # главная страница после входа
]
