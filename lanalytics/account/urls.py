from django.conf.urls.defaults import *

urlpatterns = patterns('lanalytics.account.views',
    url(r'accounts/profile/$', 'profile', name='profile'),
    url(r'^$', 'home', name='home'),
    url(r'^sites/$', 'my_sites', name='my_sites'),
    url(r'site/add/$', 'edit_site', name='add_site'),
    url(r'site/(?P<pk>[A-Za-z0-9\-]+)/edit/$', 'edit_site', name='edit_site'),
    url(r'site/(?P<pk>[A-Za-z0-9\-]+)/delete/$', 'delete_site', name='delete_site'),
    url(r'accounts/registration/$', 'registration', name='registration'),
    url(r'^accounts/logout/$', 'logout', name='logout'),
)

urlpatterns += patterns('',
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
)
