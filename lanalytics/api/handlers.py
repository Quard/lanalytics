from django.conf import settings
from piston.handler import BaseHandler

from lanalytics.analytics.forms import AnalyticForm


class PostHandler(BaseHandler):
    allowed_methods = ('POST', )

    def post(self, request):
        post = request.POST.copy()
        post['site'] = request.session[settings.SITE_KEY]
        form = AnalyticForm(post)
        if form.is_valid():
            form.save()
            return {'status': True}

        return {'status': False}
