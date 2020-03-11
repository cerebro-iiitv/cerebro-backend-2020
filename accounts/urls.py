from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register("accounts", views.AccountViewSets,
                basename='api-account')


app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += router.urls
