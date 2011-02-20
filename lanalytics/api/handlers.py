import httpagentparser
from datetime import datetime, timedelta
from django.conf import settings
from piston.handler import BaseHandler

from lanalytics.statistic.models import Site
from lanalytics.analytics.forms import AnalyticForm


class GetHandler(BaseHandler):
    allowed_methods = ('GET', )

    def read(self, request):
        data = request.GET.copy()
        callback = request.GET.get('callback')

        # override fields
        data['visitor'] = request.META['REMOTE_ADDR']
        data['site'] = request.session['%s-id' % settings.SITE_KEY]

        form = AnalyticForm(data)

        if form.is_valid():
            site = form.save()
            return {'status': True}
        else:
            print form.errors

        return {
        'status': False,
        'details': form.errors,
        }
