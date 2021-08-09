from django.db.models import fields
from rest_framework import serializers
from .models import TravelHistory

class TravelHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelHistory
        fields = '__all__'