from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *
from user.serializers import UserSerializer

class FoodSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, many=True)
    class Meta:
        model = Fooditem
        fields = ['name','user','carbohydrate','protein','fats', 'calorie','image', 'category', 'quantity', 'unit',]

class DietSerializer(ModelSerializer):
    user = UserSerializer(read_only=True, many=True)
    fooditem = FoodSerializer(read_only=True, many=True)
    class Meta:
        model = Dietplan
        fields = ['fooditem', 'DietName', 'user', 'info', 'duration','age']
