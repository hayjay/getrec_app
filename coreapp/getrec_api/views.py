from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TravelHistorySerializer
from rest_framework import serializers
# from .models import SwipeIn
# from .models import SwipeOut
from .models import TravelHistory
from datetime import datetime
from django.utils.dateparse import parse_datetime

"""
    API Overview
"""
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Swipe In' : 'swipe-in',
        'Swipe Out' : 'swipe-out',
        'Get Average' : 'calculate-average',
    }
    return Response(api_urls)

@api_view(['POST'])
def swipeIn(request):
    serializer = TravelHistorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def swipeOut(request):
    # get existing swipe in event
    swipe_in = TravelHistory.objects.get(user_id=request.data.get("user_id"))
    print(swipe_in.swipe_in_at)
    print(request.data.get("swipe_out_at"))
    # time1 = datetime.strptime("6:30",'%H:%M')
    # time2 = datetime.strptime("7:30",'%H:%M')
    # print(time2)
    # print(time1)
    # print(time2-time1)
    swipe_in_at = datetime.strptime(str(request.data.get("swipe_out_at")), '%H:%M')
    swipe_out_at = datetime.strptime(str(swipe_in.swipe_in_at), '%H:%M')
    travel_time = swipe_out_at - swipe_in_at
    request.data["travel_time"] = travel_time
    serializer = TravelHistorySerializer(instance=swipe_in, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)