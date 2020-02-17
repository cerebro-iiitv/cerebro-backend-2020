from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import SimpleRouter, DefaultRouter
from . import views

router = SimpleRouter()
router.register("accounts", views.AccountViewSet, basename='api-account')

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += router.urls
