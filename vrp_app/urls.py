from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LocationViewSet, VehicleViewSet, RunVRPAlgorithm, home

# Set up the router for viewsets
router = DefaultRouter()
router.register(r'locations', LocationViewSet)
router.register(r'vehicles', VehicleViewSet)

# URL patterns for the app
urlpatterns = [
    path('', home, name='home'),  # Route for the home page
    path('api/', include(router.urls)),  # Routes for Location and Vehicle APIs
    path('api/run-algorithm/', RunVRPAlgorithm.as_view(), name='run-algorithm'),  # Route for running VRP algorithm
]
