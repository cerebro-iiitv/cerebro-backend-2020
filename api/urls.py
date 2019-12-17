from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]
