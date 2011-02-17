from django.conf.urls.defaults import *

urlpatterns = patterns('lanalytics.account.views',
    url(r'account/profile/$', 'profile', name='profile'),
    url(r'$^', 'my_sites', name='my_sites'),
    url(r'site/add/$', 'edit_site', name='add_site'),
    url(r'site/(?P<pk>\d+)/edit/$', 'edit_site', name='edit_site'),
    url(r'site/(?P<pk>\d+)/delete/$', 'delete_site', name='delete_site'),
    url(r'account/registration/$', 'registration', name='registration'),
)

urlpatterns += patterns('',
    url(r'^account/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^account/logout/$', 'django.contrib.auth.views.logout', name='logout'),
)
