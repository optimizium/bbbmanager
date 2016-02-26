from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.generic import View
from django.template import RequestContext
import requests
import random 
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponseRedirect
from organization.models import Organization
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from meetings.models import Meeting,Participant,MeetingRoom

def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
	
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect('/account/profile/')
        else:
            return HttpResponse("Invalid login details supplied.")

    else:
        return render_to_response('user_register.html', {}, context)

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
	    org = User.objects.create_user(username,email,password)
	    org.first_name = first_name
            org.last_name = last_name
	    org.save()
	    send_mail('Your User Registration successfull','Thanks for registring with.','admin@myconfec.com',[email])

	    messages.success(request, 'Profile created please login with now')
	    return HttpResponseRedirect('/account/create')


class ProfileView(View):
    def get(self, request):
        # <view logic>i
	data = {}
	data['title'] = "Profile"
	data['user'] = User.objects.all()
	my_meetings = Meeting.objects.filter(created_by = request.user)
	data['meetings'] = my_meetings
	participant_meetings = Participant.objects.filter(name= request.user.username)
	data['participant']  = participant_meetings
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


