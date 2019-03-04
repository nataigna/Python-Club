from django.urls import path
from . import views

urlpatterns=[
    path ('', views.index, name='index'),
    path ('resources/', views.resources, name='resources'),
    path ('meeting/',views.meeting,name='meeting'),
    path ('meetingdetails/<int:id>', views.meetingdetail,name='details'),
    path('newMeeting/',views.newMeeting,name='newmeeting'),
    path('newResource/',views.newResource,name='newresource'),
    path('loginmessage/',views.loginmessage,name='loginmessage'),
    path('logoutmessage/',views.logoutmessage,name='logoutmessage'),

]