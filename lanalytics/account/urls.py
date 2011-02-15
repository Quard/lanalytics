from django.conf.urls.defaults import *

urlpatterns = patterns('lanalytics.account.views',
    url(r'registration/$', 'registration', name='registration'),
)

urlpatterns += patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
)
