from django.conf.urls.defaults import *
from piston.resource import Resource

from lanalytics.api.handlers import GetHandler, FindUserHandler, \
    SiteShareAddHandler, SiteShareDelHandler
from lanalytics.api.authentication import SiteKeyAuth


ad = {'authentication': SiteKeyAuth()}

get_resource = Resource(GetHandler, **ad)
find_user_resource = Resource(FindUserHandler)
site_share_add_resource = Resource(SiteShareAddHandler)
site_share_del_resource = Resource(SiteShareDelHandler)

urlpatterns = patterns('',
    url(r'^analytics\.(?P<emitter_format>.+)$', get_resource, name='api_post'),
    url(r'find-user\.(?P<emitter_format>.+)$', find_user_resource, 
        name='api_find_user'),
    url(r'^site-share\.(?P<emitter_format>.+)$', site_share_add_resource,
        name='api_site_share'),
    url(r'^site-share-del\.(?P<emitter_format>.+)$', site_share_del_resource,
        name='api_site_share_del'),
)
