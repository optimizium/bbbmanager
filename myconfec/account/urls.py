from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import  UserView,user_login,ProfileView
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myconfec.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login$',user_login),
    url(r'^logout/$','django.contrib.auth.views.logout',{'next_page': '/account/login'}),
    url(r'^create$',UserView.as_view()),
    url(r'^profile/$',ProfileView.as_view()),


)

