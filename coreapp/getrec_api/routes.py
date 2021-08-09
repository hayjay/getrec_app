from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('swipe-in', views.swipeIn, name="swipe-in"),
    path('swipe-out', views.swipeOut, name="swipe-out")
] 

# {
#      "id": "1",
#      "user_id": 1,
#      "swipe_in_station_id": 1,
#      "swipe_in_at": "2020-08-09 1:00:00",
#      "created_at": "2020-08-08"
# }

# {
#       "user_id": 1,
#       "swipe_out_station_id": 1,
#       "swipe_out_at": "2020-08-09 3:00:00",
#       "travel_time": "2"
# }

# {
#       "user_id": 1,
#       "swipe_out_station_id": 1,
#       "swipe_out_at": "3:00"
# }