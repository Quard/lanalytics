from django.conf.urls.defaults import *
from piston.resource import Resource

from lanalytics.api.handlers import GetHandler
from lanalytics.api.authentication import SiteKeyAuth


ad = {'authentication': SiteKeyAuth()}

get_resource = Resource(GetHandler, **ad)

urlpatterns = patterns('',
    url(r'^analytics\.(?P<emitter_format>.+)$', get_resource, name='api_post')
)
