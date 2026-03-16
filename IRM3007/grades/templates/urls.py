from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('IRM3007.urls')),  # Make sure this points to your app
]