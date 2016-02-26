from django.conf.urls import patterns, include, url
from django.contrib import admin
from meetings.views import MeetingsView,addparticipant,get_part_url,add_external_attendee,join,MyMeetingsView,MeetingRoomView
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myconfec.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^create$',MeetingsView.as_view()),

    url(r'^join$',join),
    url(r'^add_external_attendee$',add_external_attendee),
    url(r'^get_part_url$',get_part_url),
    url(r'^add_participant$',addparticipant),

    url(r'^createMeetingRoom$',MeetingRoomView.as_view()),
    url(r'^MyMeetings$',MyMeetingsView.as_view(),name='mymeetings'),
)

