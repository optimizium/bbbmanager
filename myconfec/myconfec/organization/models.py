from django.db import models
from datetime import datetime 
import datetime as d
from django.contrib.auth.models import User

class Organization(models.Model):
    
    org_name = models.CharField(max_length=30)
    org_super_user = models.ForeignKey(User,null = True,blank = True)
    org_type = models.CharField(max_length=30,null=True, blank=True)
    status = models.IntegerField(null=True, blank=True)
    org_url = models.CharField(max_length = 120,null = True,blank = True)     
    notes = models.TextField(null=True)
    email = models.CharField(max_length = 120) 
    city = models.CharField(max_length=50,null = True,blank = True)
    state = models.CharField(max_length=50,null = True,blank = True)
    country = models.CharField(max_length=50,null = True,blank = True)
    street = models.TextField(null=True,blank = True)
    date_created = models.DateTimeField(default=d.datetime.now,blank=True, null=True)
    is_activated = models.BooleanField(default = False)
    primary_mobile =models.CharField(max_length = 100)
    org_pin = models.CharField(max_length=50,null = True,blank = True)
# Create your models here.
