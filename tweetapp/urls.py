from django.urls import path
from . import views

app_name = 'tweetapp'

urlpatterns = [
    path('', views.listtweet, name='listtweet'),
    path('addtweet/', views.addtweet, name='addtweet'),
    path('addtweetbyform/', views.addtweetbyform, name='addtweetbyform'),
    path('addtweetbymodelform/', views.addtweetbymodelform, name='addtweetbymodelform'),
    path('signup/', views.SignUpView.as_view(), name="signup"),   #class bazli view larla calisirken as_view() ile gorunumu cerirebiliriz
    path('deletetweet/<int:id>', views.deletetweet, name='deletetweet'),
]
