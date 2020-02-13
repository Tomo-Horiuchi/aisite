"""ulls"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('toppage.urls')),
    path('satomi/', include('satomipage.urls')),
]
