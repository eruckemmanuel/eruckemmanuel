
from django.contrib import admin
from django.urls import path
from django.conf.urls import include



urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/home/', include('home.urls')),
    path('api/account/', include('accounts.urls')),
]
