from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from account.views import HomeView
from django.views.generic import TemplateView
urlpatterns = patterns('',
    # Examples:
     url(r'^$', HomeView.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^disclaimer/', TemplateView.as_view(template_name="term.html"), name='whatever'),
    url(r'^meeting/', include('meetings.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^organization/', include('organization.urls'))
)
urlpatterns += staticfiles_urlpatterns()

