from rest_framework import serializers
from cars.models import Car

class CarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class CarListSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Car
        fields = ('id','vin','user')
