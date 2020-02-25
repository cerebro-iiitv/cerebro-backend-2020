from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import SimpleRouter, DefaultRouter
from . import views

router = SimpleRouter()
router.register("events", views.EventViewSets,
                basename='api-event')
router.register("contact", views.ContactViewSets,
                basename='api-contact')
router.register("participant", views.ParticipantViewSets,
                basename='api-participant')


urlpatterns = router.urls
