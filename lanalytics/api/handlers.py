from piston.handler import BaseHandler

from lanalytics.analytic.forms import AnalyticForm


class PostHandler(BaseHandler):
    allowed_methods = ('POST', )

    def post(self, request):
        post = request.POST.copy()
        post['site'] = request.session['site_key']
        form = AnalyticForm(post)
        if form.is_valid():
            form.save()
            return {'status': True}

        return {'status': False}
