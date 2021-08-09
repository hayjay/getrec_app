from django.db import models
from datetime import datetime

# Create your models here.
class TravelHistory(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(default=None)
    swipe_in_station_id = models.IntegerField(default=None, blank=True, null=True)
    swipe_out_station_id = models.IntegerField(default=None, blank=True, null=True)
    swipe_in_at = models.CharField(max_length = 5, default=None, blank=True, null=True)
    swipe_out_at = models.CharField(max_length = 5, default=None, blank=True, null=True)
    created_at = models.DateField(default=datetime.now, blank=True)
    travel_time = models.IntegerField(default=None, blank=True, null=True)
    objects = models.Manager()


    