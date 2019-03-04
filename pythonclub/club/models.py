from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    agenda=models.TextField()
    meetingdate=models.DateField()
    meetingtime=models.TimeField(null=True,blank=True)

    def __str__(self):
       return self.meetingtitle

    class Meta:
        db_table='meeting'
class MeetingMinuted(models.Model):
    meetingid=models.ForeignKey(Meeting, on_delete=models.CASCADE)
    attendance=models.ManyToManyField(User)
    minutestext=models.TextField()

    def __str__(self):
       return self.meetingid

    class Meta:
        db_table='meetingminuted'   


class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255)
    resourceurl=models.URLField(null=True, blank=True)
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    description=models.TextField()

    def __str__(self):
       return self.resourcename
    
    class Meta:
        db_table='resource'

class Event(models.Model):
    eventtitle=models.CharField(max_length=255) 
    eventlocation=models.CharField(max_length=255)
    eventdate=models.DateField()
    eventtime=models.TimeField()
    userid=models.CharField(max_length=255)

    def __str__(self):
       return self.eventtitle
    
    class Meta:
        db_table='event'

