from django.conf.urls.defaults import *

urlpatterns = patterns('lanalytics.account.views',
    url(r'accounts/profile/$', 'profile', name='profile'),
    url(r'$^', 'my_sites', name='my_sites'),
    url(r'site/add/$', 'edit_site', name='add_site'),
    url(r'site/(?P<pk>\d+)/edit/$', 'edit_site', name='edit_site'),
    url(r'site/(?P<pk>\d+)/delete/$', 'delete_site', name='delete_site'),
    url(r'accounts/registration/$', 'registration', name='registration'),
)

urlpatterns += patterns('',
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='logout'),
)
