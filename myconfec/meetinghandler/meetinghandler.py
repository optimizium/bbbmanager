import httplib
#import settings
from django.conf import settings
import string, re, urllib
from urllib2 import urlopen
from urllib import urlencode
from hashlib import sha1
import random 
from pyxml2obj import XMLin, XMLout

def GetBBBWelcomeMsg(meetingName):
    wmsg = 'You can mute yourself in the Listeners window.'
    return wmsg

#XMLin   xml to python dict
# Xmlout dict to xmlinitialize
class BBBMeeting():
    def __init__(self,meetingID,name,moderator_passwd,attendee_passwd,meeting_logout_url, welcome=None, force = False):
        self.meetingID = meetingID
        self.name = name
        self.attandee_list = []
        self.moderator_passwd = moderator_passwd
        self.attendee_passwd = attendee_passwd
        self.start_time = None
        self.end_time = None
        self.status = None
        self.messageKey = None
        if welcome is None:
            welcome = GetBBBWelcomeMsg(name)
        self.welcome = welcome
        self.meeting_logout_url = meeting_logout_url
        self.force = force
    
    def forceCreate(self):
        self.start()
        
       # if self.meetingID:
         #   self.meeting_Info()
    def api_call(self, query, call):
        prepared = "%s%s%s" % (call, query, settings.SALT)
        checksum = sha1(prepared).hexdigest()
        result = "%s&checksum=%s" % (query, checksum)
        url = settings.BBB_API_URL + call + '?' + result
	print url
        result = urllib.urlopen(url)
        get_xml = result.read()
	print get_xml
        hashed = XMLin(get_xml)
        for k,v in hashed.items():
            if k.lower() == "failed" and self.force :
                self.forceCreate()
            
        
        return hashed
    
    def is_running(self):
        call = 'isMeetingRunning'
        query = urlencode((
            ('meetingID', self.meetingID),
        ))
        hashed = self.api_call(query, call)
        return hashed
  
    def end_meeting(self):
        call = 'end'
        query = urlencode((
            ('meetingID', self.meetingID),
            ('password', self.moderator_passwd),
        ))
        hashed = self.api_call(query, call)
    #    url = settings.BBB_API_URL + call + '?' + hashed
      #  result = urllib.urlopen(url)
    #    get_xml = result.read()
      #  rd_xml = XMLin(hashed)
        for getd,v in hashed.items():
            if getd == "attendees":
               for attandee in v.items():
                   self.attandee_list.append(attandee)
            if getd == "moderatorPW":
                self.moderator_passwd = v
            if getd == "moderatorPW":
                self.moderator_passwd = v
            if getd == "attendeePW":
                self.attendee_passwd = v  
            if getd == "startTime":
                self.start_time = v  
            if getd == "endTime":
                self.end_time = v  
            if getd == "messageKey":
                self.messageKey = v
        if self.start_time == '0' and  self.end_time == '0':
            self.status = 'Not Yet started'
        if self.start_time !='0' and self.end_time == '0':
            self.status = 'Meeting Started at %s'(self.start_time)       
        if self.start_time !='0' and self.end_time != '0':
            self.status = 'Meeting completed at '+ str(self.end_time)   
        return hashed
    
    
    def meeting_info(self):
        call = 'getMeetingInfo'
        query = urlencode((
            ('meetingID', self.meetingID),
            ('password', self.moderator_passwd),
        ))
        hashed = self.api_call(query, call)
        for getd,v in hashed.items():
            if getd == "attendees":
                for attandee in v.items():
                    self.attandee_list.append(attandee)
            if getd == "moderatorPW":
                self.moderator_passwd = v
            if getd == "attendeePW":
                self.attendee_passwd = v  
            if getd == "startTime":
                self.start_time = v  
            if getd == "endTime":
                self.end_time = v  
            if getd == "messageKey":
                self.messageKey = v
        if self.start_time == '0' and  self.end_time == '0':
            self.status = 'Not Yet started'
        if self.start_time !='0' and self.end_time == '0':
            self.status = 'Meeting Started at ' + str(self.start_time)       
        if self.start_time !='0' and self.end_time != '0':
            self.status = 'Meeting Ended at ' + str(self.end_time)      
        return hashed
    
    
    def start(self):
        call = 'create'
        voicebridge = 70000 + random.randint(0,9999)
        query = urlencode((
            ('name', self.name),
            ('meetingID', self.meetingID),
            ('attendeePW', self.attendee_passwd),
            ('moderatorPW', self.moderator_passwd),
            ('logoutURL', self.meeting_logout_url),
            ('welcome', self.welcome),
        ))
        hashed = self.api_call(query, call)
	print hashed
        for getd,v in hashed.items():
            if getd == "meetingID":
                self.meetingID = v
            if getd == "moderatorPW":
                self.moderator_passwd = v
            if getd == "moderatorPW":
                self.moderator_passwd = v
            if getd == "attendeePW":
                self.attendee_passwd = v  
            if getd == "startTime":
                self.start_time = v    
            if getd == "messageKey":
                self.messageKey = v                 
 
        return hashed
    
    def join_url(self,name):#, meetingID, name, attandee_passwd):
        call = 'join'
        query = urlencode((
            ('fullName', name),
            ('meetingID', self.meetingID),
            ('password', self.attendee_passwd),
        ))
        prepared = "%s%s%s" % (call, query, settings.SALT)
        checksum = sha1(prepared).hexdigest()
        hashed = "%s&checksum=%s" % (query, checksum)
        url = settings.BBB_API_URL + call + '?' + hashed
        return url
    
    def moderator_join_url(self,name):#, meetingID, name, attandee_passwd):
        call = 'join'
        query = urlencode((
            ('fullName', name),
            ('meetingID', self.meetingID),
            ('password', self.moderator_passwd),
        ))
        prepared = "%s%s%s" % (call, query, settings.SALT)
        checksum = sha1(prepared).hexdigest()
        hashed = "%s&checksum=%s" % (query, checksum)
        url = settings.BBB_API_URL + call + '?' + hashed
        return url
    
