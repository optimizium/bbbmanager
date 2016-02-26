from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import OrganizationView
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myconfec.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^create$',OrganizationView.as_view()),
)

