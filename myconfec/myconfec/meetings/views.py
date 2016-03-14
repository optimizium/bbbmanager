from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.generic import View
from django.template import RequestContext
import requests
import random
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponseRedirect
from meetinghandler.meetinghandler import BBBMeeting
from meetings.models import Meeting,Participant,MeetingRoom
import json
from django.views.decorators.csrf import csrf_exempt
from random import randint
import datetime 

BASE_URL = settings.BASE_URL
class MeetingsView(View):
    def get(self, request):
        # <view logic>i
        data = {}
        data['title'] = "Create Meeting"
	data['num_of_user'] = User.objects.filter()
#	data['meetings'] = Meetings.objects.filter(meeting_datetime = datetime.now(), created_by = User)
        return render_to_response('createMeeting.html',
                data,
                context_instance=RequestContext(request))

    def post(self, request, *args, **kwargs):
        print "-------------------------"
        meeting_name = request.POST.get('meeting_name','')
        meeting_id = str(randint(0,90909090)) #request.POST.get('meeting_id','')
        meeting_time = request.POST.get('meeting_time','')
        #meeting_duration = request.POST.get('meeting_duration','')
        attendee_password = request.POST.get('attendee_password','')
        moderator_password = request.POST.get('moderator_password','')
	bbm_obj = BBBMeeting(meeting_id,meeting_name,moderator_password,attendee_password,"http://google.com")
	resp = bbm_obj.start()	
	mid = Meeting()
	mid.name = meeting_name
	mid.meetingID = meeting_id
	mid.meeting_duration = '5'#meeting_duration 
	mid.attendee_passwd = attendee_password
	mid.moderator_passwd = moderator_password
	mid.meeting_datetime = meeting_time
 	mid.meeting_logout_url = "http://google.com"
	print dir(User)
	mid.created_by = request.user
	mid.save()
	
   	join_url = bbm_obj.moderator_join_url(request.user.username)	
	add_partcpnt = Participant()
	add_partcpnt.name = request.user.username
	add_partcpnt.meeting_id = mid
	add_partcpnt.previlage = 'moderator'
	add_partcpnt.email = request.user.email
	add_partcpnt.user_view_url = join_url
	add_partcpnt.save()
#	d = Meeting.objects.all()
#	d.delete()
	data = {}
	data['name'] = meeting_name
	data['meeting_id'] = meeting_id
	return HttpResponse(json.dumps(data))
@csrf_exempt		
def addparticipant(request):
    
    participant_name = request.POST.get('participant_name','')
    meeting_id = request.POST.get('meetingID','')
    user_name = User.objects.get(username = participant_name)
    meeting = Meeting.objects.get(meetingID = meeting_id)
    bbm_obj = BBBMeeting(meeting_id,meeting.name,meeting.moderator_passwd,meeting.attendee_passwd,"http://google.com")
    if bbm_obj:
   	join_url = bbm_obj.join_url(user_name.username)
        add_partcpnt = Participant()
        add_partcpnt.name = user_name.username
        add_partcpnt.meeting_id = meeting
        add_partcpnt.previlage = 'attendee'
        add_partcpnt.email = user_name.email
        add_partcpnt.user_view_url = join_url
	add_partcpnt.save()
        data = {}
        data['name'] = participant_name
        data['meeting_id'] = meeting_id
        return HttpResponse(json.dumps(data))

def add_external_attendee(request):
    participant_name = request.POST.get('external_name','')
    participant_email = request.POST.get('external_emailid','')

    participant_mobile = request.POST.get('contact_number','')
    meeting_id = request.POST.get('meetingID','')

#    user_name = User.objects.get(username = participant_name)
    meeting = Meeting.objects.get(meetingID = meeting_id)
    bbm_obj = BBBMeeting(meeting_id,meeting.name,meeting.moderator_passwd,meeting.attendee_passwd,"http://google.com")
    if bbm_obj:
        join_url = bbm_obj.join_url(participant_name)
        add_partcpnt = Participant()
        add_partcpnt.name = participant_name
        add_partcpnt.meeting_id = meeting
        add_partcpnt.previlage = 'attendee'
        add_partcpnt.email = participant_email
        add_partcpnt.user_view_url = join_url
        add_partcpnt.save()
	url = BASE_URL+'/meeting/join?meetingID='+meeting_id+'&email='+participant_email
        send_mail('Your are invited for a meeting Please click on below link to join',url,'admin@myconfec.com',[participant_email])

        data = {}
        data['name'] = participant_name
        data['meeting_id'] = meeting_id
        return HttpResponse(json.dumps(data))

def join(request):

    meeting_id = request.GET['meetingID']
    email = request.GET['email']
    meeting = Meeting.objects.get(meetingID = meeting_id)
    bbm_obj = BBBMeeting(meeting_id,meeting.name,meeting.moderator_passwd,meeting.attendee_passwd,"http://google.com")
    resp = bbm_obj.start()

    url = Participant.objects.get(meeting_id = meeting,email = email)

    return HttpResponseRedirect(url.user_view_url)



@csrf_exempt		
def get_part_url(request):

    participant_name = request.POST.get('participant_name','')
    meeting_id = request.POST.get('meetingID','')

    meeting = Meeting.objects.get(meetingID = meeting_id)
    bbm_obj = BBBMeeting(meeting_id,meeting.name,meeting.moderator_passwd,meeting.attendee_passwd,"http://google.com")
    resp = bbm_obj.start()	

    url = Participant.objects.get(meeting_id = meeting,name = participant_name)

    data = {}
    data['url'] = url.user_view_url
    data['meeting_id'] = meeting_id
    return HttpResponse(json.dumps(data))

class MyMeetingsView(View):
    def get(self, request):
        # <view logic>i
        data = {}
	update = request.GET.get('update',None)
        data['title'] = "My Meetings"
	data['update'] = update
	if update == 'update':
	    data['meetings'] = Meeting.objects.filter(created_by = request.user,meeting_datetime__gte=datetime.datetime.now())
        else:data['meetings'] = Meeting.objects.filter(created_by = request.user)
#       data['meetings'] = Meetings.objects.filter(meeting_datetime = datetime.now(), created_by = User)
        return render_to_response('mymeetings.html',
                data,
                context_instance=RequestContext(request))

class MeetingRoomView(View):

    def get(self, request):
        data = {}
        data['title'] = "Create Meeting Room"
	data['num_of_user'] = User.objects.filter()
        return render_to_response('createMeetingRoom.html',
                data,
                context_instance=RequestContext(request))


    def post(self, request, *args, **kwargs):
        meeting_name = request.POST.get('meeting_name','')
        meeting_id = str(randint(0,90909090)) #request.POST.get('meeting_id','')
        meeting_time = request.POST.get('meeting_time','')
        max_participants = request.POST.get('max_participants','')
        attendee_password = request.POST.get('attendee_password','')
        moderator_password = request.POST.get('moderator_password','')
        bbm_obj = BBBMeeting(meeting_id,meeting_name,moderator_password,attendee_password,"http://google.com")
        resp = bbm_obj.start()


	mrid = MeetingRoom()
	mrid.name = meeting_name
	mrid.expired_on = meeting_time
        mrid.created_by = request.user
	mrid.save()

        mid = Meeting()
        mid.name = meeting_name
	mid.venue = mrid
        mid.meetingID = meeting_id
        mid.meeting_duration = '5'#meeting_duration 
        mid.attendee_passwd = attendee_password
        mid.moderator_passwd = moderator_password
        mid.meeting_datetime = meeting_time
        mid.meeting_logout_url = "http://google.com"
        mid.created_by = request.user
        mid.save()

        join_url = bbm_obj.moderator_join_url(request.user.username)
        add_partcpnt = Participant()
        add_partcpnt.name = request.user.username
        add_partcpnt.meeting_id = mid
        add_partcpnt.previlage = 'moderator'
        add_partcpnt.email = request.user.email
        add_partcpnt.user_view_url = join_url
        add_partcpnt.save()
#       d = Meeting.objects.all()
#       d.delete()
        data = {}
        data['name'] = meeting_name
        data['meeting_id'] = meeting_id
        return HttpResponse(json.dumps(data))




# Create your views here.
