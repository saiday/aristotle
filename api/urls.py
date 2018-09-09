from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from api.views import UserViewSet, GroupViewSet, TicketViewSet, LocationViewSet, CityViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'cities', CityViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
