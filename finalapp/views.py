from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import *
from .serializers import *

# Create your views here.
class FoodModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Fooditem.objects.all()
    serializer_class = FoodSerializer

class DietModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Dietplan.objects.all()
    serializer_class = DietSerializer

class BreakfastModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Fooditem.objects.filter(category='breakfast')
    serializer_class = FoodSerializer

class LunchModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Fooditem.objects.filter(category='lunch')
    serializer_class = FoodSerializer
class DinerModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Fooditem.objects.filter(category='diner')
    serializer_class = FoodSerializer

class SnacksModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Fooditem.objects.filter(category='snacks')
    serializer_class = FoodSerializer

