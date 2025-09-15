from django.contrib import admin
from django.urls import path, include   # include is needed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),   # ✅ include api app urls
]
