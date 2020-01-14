from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path('listAPI/', views.AccountListAPI.as_view(), name='account_api'),
    path('signup/', views.signup, name='signup'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

