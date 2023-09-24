from django.urls import path
from . import views

app_name = 'tweetapp'

urlpatterns = [
    path('', views.listtweet, name='listtweet'),
    path('addtweet/', views.addtweet, name='addtweet'),
    path('addtweetbyform/', views.addtweetbyform, name='addtweetbyform'),
]
