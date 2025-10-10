from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # ✅ API base path
    path('api/', include([
        path('posts/', include('posts.urls')),   # ✅ Includes posts app
        path('accounts/', include('accounts.urls')),  # (Optional if you have accounts app)
    ])),
]

from django.urls import path, include

urlpatterns = [
    path('posts/', include('posts.urls')),  # ✅ Required so feed/ is found
]

path('api/notifications/', include('notifications.urls')),
