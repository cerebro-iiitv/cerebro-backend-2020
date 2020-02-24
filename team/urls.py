from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register("teams", views.TeamViewSet, basename='api-team')

urlpatterns = router.urls
