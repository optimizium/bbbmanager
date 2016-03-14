from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.generic import View
from django.template import RequestContext
import requests
import random 
from django.core.mail import send_mail
from django.contrib import messages
from models import Organization
from django.http import HttpResponseRedirect

class OrganizationView(View):
    def get(self, request):
        # <view logic>i
	data = {}
	data['title'] = "Create Organization"

        return render_to_response(  'organization.html',
        	data,
    		context_instance=RequestContext(request))

    def post(self, request, *args, **kwargs):
	org_name = request.POST.get('org_name','')
	org_contact = request.POST.get('org_contact','')
	org_email = request.POST.get('org_email','')
	org_password = request.POST.get('org_password','')
	org_password1 = request.POST.get('org_password1','')
	org_address = request.POST.get('org_address','')
	org_url = request.POST.get('org_url','')

        if org_password != org_password1:
            messages.success(request, 'Password did not match ')
            return HttpResponseRedirect('/organization/create')
        else:
	    org = Organization()
	    org.org_name = org_name
	    org.org_url = org_url	    
	    org.street = org_address
	    org.email = org_email
            org.password = org_password
	    org.org_url = org_url
	    pin  ='REG_'+str(random.randint(56,100022))
 	    org.org_pin = pin
	    org.save()
	    send_mail('Your User Registration pin on Myconfec','Thanks for registring with us ask your users to enter '+pin+'  to register.','admin@myconfec.com',[org_email])

	    messages.success(request, 'Profile created please check your email for pin.')

	    return HttpResponseRedirect('/organization/create')


class OriganizationView(View):
    def get(self, request):
        # <view logic>i
	data = {}
	data['title'] = "Admin login"

        return render_to_response('admin_login.html',
        	data,
    		context_instance=RequestContext(request))

