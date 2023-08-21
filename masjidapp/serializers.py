from rest_framework import serializers
from .models import Countries,States,District,Masjidregister

class Countriesserializer(serializers.ModelSerializer):
    class Meta:
        model=Countries
        fields='__all__'

class Stateserializer(serializers.ModelSerializer):
    class Meta:
        model=States
        fields='__all__'

class Districtserializer(serializers.ModelSerializer):
    class Meta:
        model=District
        fields='__all__'

class Masjidserializer(serializers.ModelSerializer):
    class Meta:
        model=Masjidregister
        fields='__all__'

