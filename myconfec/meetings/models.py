from django.db import models
from django.contrib.auth.models import User
import datetime

class MeetingRoom(models.Model):
    
    name = models.CharField(max_length=100,null = True, blank = True)
    type = models.CharField(max_length = 200,blank = True,null = True)
    expired_on = models.CharField(max_length = 100,blank = True)
    user = models.ForeignKey(User,related_name ='meeting_created',null = True,blank = True)

                

class Meeting(models.Model):
    name = models.CharField(max_length=200)
    meetingID = models.CharField(max_length = 50) 
    venue = models.ForeignKey(MeetingRoom,related_name ='meetingroom',null = True,blank = True)   # whether One Time or Recurring
    status =models.IntegerField(null=True, blank=True)
    attendee_passwd = models.CharField(max_length=100)
    moderator_passwd = models.CharField(max_length = 100)
    date_created = models.DateTimeField(auto_now=True)               # it should be auto fill 
   
    meeting_datetime = models.DateTimeField(default=datetime.datetime.now,blank=True, null=True)
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=100)
    meeting_duration = models.CharField(max_length=100)

    duration = models.CharField(max_length=20)
    created_by = models.ForeignKey(User,related_name ='meetingroom_created')
    conferenceID = models.IntegerField(blank=True, null=True)
    meeting_logout_url = models.CharField(max_length=100)
    max_participants = models.IntegerField(blank=True, null=True)

class Participant(models.Model):
    
    name = models.CharField(max_length=100)
    meeting_id = models.ForeignKey(Meeting,related_name = 'meeting_participants')
#    password = models.CharField(max_length=100)
#    notification_url = models.CharField(max_length=250)  ###
    user_view_url = models.CharField(max_length = 300)  #### This is what user will get 
 #   key = models.CharField(max_length = 200)
    contact_no = models.CharField(max_length = 50,null = True,blank = True)
    #notification_pin = models.IntegerField(max_length=100)
    type = models.CharField(max_length=100,null = True,blank = True)
    status =models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length = 200)
    previlage =  models.CharField(max_length=30,default="attendee")

# Create your models here.
