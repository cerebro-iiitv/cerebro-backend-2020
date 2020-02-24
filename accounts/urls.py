from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
# from rest_framework.routers import SimpleRouter
from . import views


app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
# urlpatterns += router.urls
