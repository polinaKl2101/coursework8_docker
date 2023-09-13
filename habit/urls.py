from habit.apps import HabitConfig
from django.urls import path

from habit.views import HabitListAPIView, HabitCreateAPIView, HabitUpdateAPIView, HabitRetrieveAPIView, \
    HabitDeleteAPIView

app_name = HabitConfig.name

urlpatterns = [
    path('habit/', HabitListAPIView.as_view(), name='list_habit'),
    path('habit/create/', HabitCreateAPIView.as_view(), name='create_habit'),
    path('habit/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='update_habit'),
    path('habit/retrieve/<int:pk>/', HabitRetrieveAPIView.as_view(), name='retrieve_habit'),
    path('habit/delete/<int:pk>/', HabitDeleteAPIView.as_view(), name='delete_habit')
]
