from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myconfec.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^meeting/', include('meetings.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^organization/', include('organization.urls'))
)
urlpatterns += staticfiles_urlpatterns()

