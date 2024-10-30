from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status  # Ensure status is imported
from django.shortcuts import render
from .models import Location, Vehicle
from .serializers import LocationSerializer, VehicleSerializer
from .genetic_algorithm import GeneticAlgorithm  # Make sure this module exists

# Define the home view
def home(request):
    return render(request, 'vrp_app/index.html')  # Ensure you have this template file

# Location and Vehicle ViewSets
class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Location, Vehicle
from .genetic_algorithm import GeneticAlgorithm  # Ensure this exists

logging.basicConfig(level=logging.DEBUG)

class RunVRPAlgorithm(APIView):
    def get(self, request):
        # Check if there are any locations
        locations = Location.objects.all()
        if not locations.exists():
            logging.debug("No locations found.")
            return Response({"error": "No locations found. Please add locations first."}, status=status.HTTP_400_BAD_REQUEST)

        # Extract coordinates from locations
        location_points = [(loc.x, loc.y) for loc in locations]
        logging.debug(f"Location points: {location_points}")
        
        # Ensure there is a vehicle in the database
        vehicle = Vehicle.objects.first()
        if not vehicle:
            logging.debug("No vehicle found.")
            return Response({"error": "No vehicle found. Please add a vehicle first."}, status=status.HTTP_400_BAD_REQUEST)

        # Attempt to run the VRP algorithm
        try:
            ga = GeneticAlgorithm(location_points, vehicle.capacity)
            best_route = ga.get_best_route()
            total_distance = ga.fitness(best_route)

            logging.debug(f"Best route: {best_route}, Total distance: {total_distance}")

            return Response({
                "best_route": best_route,
                "total_distance": total_distance
            })
        except Exception as e:
            logging.error(f"Algorithm error: {str(e)}")
            return Response({"error": f"Algorithm error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
