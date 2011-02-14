from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^auth/', include('social_auth.urls')),
    url(r'^auth/login/$', 'django.contrib.auth.views.login'),
    url(r'^auth/logout/$', 'django.contrib.auth.views.logot'),
    (r'^admin/', include(admin.site.urls)),
)
