from django.conf import settings
from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^', include('lanalytics.api.urls')),
    (r'^', include('lanalytics.account.urls')),
    (r'^statistic/', include('lanalytics.statistic.urls')),
    (r'^auth/', include('social_auth.urls')),
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'^%s/(?P<path>.*)$' % settings.MEDIA_URL.strip('/'), 'serve',
         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )