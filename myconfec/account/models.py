from django.db import models
#from organization.models import *
import datetime 
from django.contrib.auth.models import User
from organization.models import Organization
class UserProfile(models.Model):

    user = models.OneToOneField(User)  
#    first_name = models.CharField(max_length=100)
#    middle_name = models.CharField(max_length=100)
#    last_name = models.CharField(max_length=100)

#    user_name = models.CharField(max_length=100)
#    passwd = models.CharField(max_length=80)
#    role = models.CharField(max_length = 20)
#    org_name = models.ForeignKey('organization.Organization',related_name = 'user_org_nm',null= False)
    timezone = models.CharField(max_length = 50)
    
    org_pin = models.CharField(max_length = 100)
    city = models.CharField(max_length=100,null = True,blank = True)
    state = models.CharField(max_length=100,null = True,blank = True)
    country = models.CharField(max_length=100,null = True,blank = True)
    street = models.TextField(null=True,blank = True)
    pin = models.CharField(max_length=30,null = True,blank = True)

    
    user_type = models.CharField(max_length = 100)
    status =models.IntegerField(null=True, blank=True)
    primary_mobile =models.CharField(max_length = 100,null = True,blank = True)
    secondary_mobile =models.CharField(max_length = 100,null = True,blank = True)
    primary_email = models.CharField(max_length = 100,null = True,blank = True)
    date_created = models.DateTimeField(default=datetime.datetime.now,blank=True, null=True)
    date_modified =models.DateTimeField(auto_now = False,null = True)
# Create your models here.
