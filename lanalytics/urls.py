from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^auth/', include('lanalytics.account.urls')),
    (r'^auth/', include('social_auth.urls')),
    (r'^admin/', include(admin.site.urls)),
)
