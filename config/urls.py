"""
config/urls.py
ok: 12/20/21 0655
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),

    # User management
    path('accounts/', include('allauth.urls')), # new

    # Local apps
    path('', include('pages.urls')),
    path('books/', include('books.urls')),
]
