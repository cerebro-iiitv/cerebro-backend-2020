from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register("events", views.EventViewSets,
                basename='api-event')
router.register("contact", views.ContactViewSets,
                basename='api-contact')


urlpatterns = router.urls
