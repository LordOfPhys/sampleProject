from rest_framework import serializers

from app.models.outlet import Outlet


class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    phone_number = serializers.CharField()

class OutletSerializer(serializers.ModelSerializer):
    label = serializers.CharField()

    class Meta:
        model = Outlet
        fields = '__all__'

class MakeVisitSerializer(serializers.Serializer):
    date = serializers.DateField()
    lat = serializers.FloatField()
    lon = serializers.FloatField()