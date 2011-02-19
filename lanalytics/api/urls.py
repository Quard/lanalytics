from django.conf.urls.defaults import *
from piston.resource import Resource

from lanalytics.api.handlers import PostHandler
from lanalytics.api.authentication import SiteKeyAuth


ad = {'authentication': SiteKeyAuth()}

post_resource = Resource(PostHandler, **ad)

urlpatterns = patterns('',
    url(r'^la_push\.js$', post_resource, {'emitter_format': 'json'},
        name='api_post'),
)
