from django.conf.urls.defaults import *
from piston.resource import Resource

from lanalytics.api.handlers import PostHandler
from lanalytics.api.authentication import SiteKeyAuth


ad = {'authentication': SiteKeyAuth()}

post_resource = Resource(PostHandler, *ad)

urlpatterns = patterns('',
    url(r'^post\.(?P<emitter_format>.+)$', post_resource, name='api_post')
)