from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.generic import View
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import requests
import random 
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponseRedirect
from organization.models import Organization
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from meetings.models import Meeting,Participant,MeetingRoom
import datetime 
from organization.models import Organization
from models import UserProfile

class HomeView(View):
    def get(self, request):
        # <view logic>i
	data = {}
	
	data['title'] = "Home"
        return render_to_response(  'home.html',
        	data,
    		context_instance=RequestContext(request))

#    def post(self, request, *args, **kwargs):


def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)
    data = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #userType = request.POST['user']
	
	user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect('/account/profile/')
        else:
            return HttpResponse("Invalid login details supplied.")

    else:
	#userType = request.GET['user']
	#if userType == "admin":
	#    data['title'] = "Admin Login"
	#    data['userType'] = 'admin'
	#else:
	data['title'] = "User Login"
	data['userType'] = 'user'
        return render_to_response('user_register.html', data, context)

class UserView(View):
    def get(self, request):
        # <view logic>i
	data = {}
	data['title'] = "Create User"
        return render_to_response(  'user_register.html',
        	data,
    		context_instance=RequestContext(request))

    def post(self, request, *args, **kwargs):
	username = request.POST.get('username','')
	first_name = request.POST.get('first_name','')
	email = request.POST.get('email','')
	password = request.POST.get('password','')
	password1 = request.POST.get('password1','')
	last_name = request.POST.get('last_name','')
	org_pin = request.POST.get('org_pin','')

        if org_pin:
	    try:
		org = Organization.objects.get(org_pin = org_pin)
	    except:
                messages.success(request, 'Organization does not exist.')
                return HttpResponseRedirect('/account/create')
        if password != password1:
            messages.success(request, 'Password did not match ')
            return HttpResponseRedirect('/account/create')
        else:
	    num_of_user = UserProfile.objects.filter(org_pin = org_pin)
	    org1 = User.objects.create_user(username,email,password)
	    org1.first_name = first_name
            org1.last_name = last_name
	#    org1.org_name = org
	    org1.save()
	    up = UserProfile()
	    up.org_pin = org_pin
	    if not len(num_of_user) > 0:
		org.org_super_user = org1
		org.save()
	        up.user_type = 'admin'
	    else:
		up.user_type = 'user'
	    up.user = org1
	    up.save()
	    send_mail('Your User Registration successfull','Thanks for registring with.','admin@myconfec.com',[email])

	    messages.success(request, 'Profile created please login with now')
	    return HttpResponseRedirect('/account/create')

class ProfileView(View):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProfileView, self).dispatch(*args, **kwargs)

    def get(self, request):
        # <view logic>i
	data = {}
	m_date = request.GET.get('meeting_date',None)
	if not m_date:
	   m_date = datetime.datetime.today()
	else:
	   m_date =  datetime.datetime.strptime(m_date, '%Y-%m-%d')
	data['title'] = "Profile"
	data['today'] = datetime.datetime.now()
	#data['tomorrow'] = datetime.timedelta(days=1)
	data['user'] = User.objects.all()
	my_meetings = Meeting.objects.filter(created_by = request.user)
	data['meetings'] = my_meetings
	login_user = UserProfile.objects.get(user = request.user.id)
	data['login_user'] = login_user
	participant_meetings = Participant.objects.filter(name= request.user.username,meeting_id__meeting_datetime__year = m_date.year)
        org = Organization.objects.get(org_pin = login_user.org_pin)
	data['org'] = org
	participant = []
	for  x in participant_meetings:
	    if  x.meeting_id.meeting_datetime.date() == m_date.date():
		participant.append(x)
	data['participant']  = participant
        return render_to_response('profile.html',
        	data,
    		context_instance=RequestContext(request))

    def post(self, request, *args, **kwargs):
	username = request.POST.get('username','')
	first_name = request.POST.get('first_name','')
	email = request.POST.get('email','')
	password = request.POST.get('password','')
	password1 = request.POST.get('password1','')
	last_name = request.POST.get('last_name','')
	org_pin = request.POST.get('org_pin','')

	return None



class TeamView(View):
    def get(self, request):
        # <view logic>i
        data = {}
        login_user = UserProfile.objects.get(user = request.user.id)
        data['login_user'] = login_user
        org = Organization.objects.get(org_pin = login_user.org_pin)
        data['org'] = org

	data['users'] = UserProfile.objects.filter(org_pin = login_user.org_pin)
        data['title'] = "My Team"
        return render_to_response('myTeamHome.html',
                data,
                context_instance=RequestContext(request))


