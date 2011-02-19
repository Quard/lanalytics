import httpagentparser
from datetime import datetime, timedelta
from django.conf import settings
from piston.handler import BaseHandler

from lanalytics.statistic.models import Site
from lanalytics.analytics.forms import AnalyticForm


class PostHandler(BaseHandler):
    allowed_methods = ('GET', )

    def read(self, request):
        post = request.GET.copy()
        post['site'] = Site.objects\
            .get(key=request.session[settings.SITE_KEY]).pk
        post['visitor'] = request.session.session_key
        expiry = datetime.now().date() + timedelta(days=1)
        request.session.set_expiry(datetime(
            expiry.year, expiry.month, expiry.day
        ))

        browser = httpagentparser.detect(request.META['HTTP_USER_AGENT'])
        post['browser'] = browser['browser']['name']
        post['browser_version'] = 'version' in browser['browser'] and \
            browser['browser']['version'] or None
        if 'os' in browser:
            post['platform'] = browser['os']['name']
            post['platrorm_version'] = 'version' in browser['os'] and \
                browser['os']['version'] or None
        
        form = AnalyticForm(post)
        if form.is_valid():
            site = form.save()
            return {'status': True}
        else:
            print form.errors

        return {'status': False}
