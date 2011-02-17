from django.conf import settings
from django.http import HttpResponse

from lanalytics.statistic.models import Site


class SiteKeyAuth(object):

    def is_authenticated(self, request):
        try:
            site = Site.objects.get(key=request.GET.get('api_key'))
            request.session[settings.SITE_KEY] = site.key

            return True
        except Site.DoesNotExist:
            pass

        return False

    def challenge(self):
        resp = HttpResponse("Site key required")
        resp.status_code = 401

        return resp
