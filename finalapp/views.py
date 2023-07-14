from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import *
from .serializers import *


# Create your views here.
class FoodModelViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Fooditem.objects.all()
    serializer_class = FoodSerializer

class DietModelViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Dietplan.objects.all()
    serializer_class = DietSerializer

class BreakfastModelViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Fooditem.objects.filter(category='breakfast')
    serializer_class = FoodSerializer

class LunchModelViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Fooditem.objects.filter(category='lunch')
    serializer_class = FoodSerializer
class DinerModelViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Fooditem.objects.filter(category='diner')
    serializer_class = FoodSerializer

class SnacksModelViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Fooditem.objects.filter(category='snacks')
    serializer_class = FoodSerializer

@api_view(['PUT'])
def updateuser(request, pk):
    if request.method == 'PUT':
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

# class ConnectionView(APIView):
#     def post(self, request, user_id):
#         try:
#             user = User.objects.get(id=user_id)

#         except User.DoesNotExist:
#             return Response("User not found", status=404)
        
#         connection_serializer = ConnectionSerializer(data=request.data)
#         if connection_serializer.is_valid():
#             connection = connection_serializer.save(user=user)
#         else:
#             return Response(connection_serializer.errors, status=400)
        