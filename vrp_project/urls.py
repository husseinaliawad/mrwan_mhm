from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vrp_app.urls')),  # Include all URLs from vrp_app
]
