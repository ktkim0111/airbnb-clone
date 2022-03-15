from django.urls import path
from . import views

app_name = "rooms"

# <type:name>
urlpatterns = [path("<int:pk>", views.RoomDetail.as_view(), name="detail")]
