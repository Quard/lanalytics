import httpagentparser
from datetime import datetime, timedelta
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
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

        return {
            'status': False,
            'details': form.errors,
        }


class FindUserHandler(BaseHandler):
    allowed_methods = ('GET', )

    def read(self, request):
        users = []
        if request.GET.get('q'):
            q = request.GET['q']
            users_qs = User.objects.exclude(pk=request.user.pk)
            users.extend(
                [u.username for u in users_qs.filter(username__startswith=q)]
            )
            users.extend(
                [u.email for u in users_qs.filter(email__startswith=q)\
                    .exclude(username__in=users)]
            )

        return '\n'.join(users)


class SiteShareAddHandler(BaseHandler):
    allowed_methods = ('GET', )
    model = Site

    def read(self, request):
        ret = {'status': False}
        user, site = None, None
        
        try:
            user = User.objects.get(
                Q(username=request.GET['username']) | 
                Q(email=request.GET['username'])
            )
        except (KeyError, User.DoNotExist):
            ret['error'] = _('User not found')
            return ret
        
        try:
            site = Site.objects.get(owner=request.user, pk=request.GET['site'])
        except (KeyError, Site.DoesNotExist):
            ret['error'] = _('Site not found')
            return ret
        
        if user in site.share_with.all():
            ret['error'] = _('User already exist')
        else:
            try:
                site.share_with.add(user)
            except:
                ret['error'] = _('Something went wrong, try later')
            else:
                ret['status'] = True
                ret['user'] = {
                    'username': user.username,
                    'pk': user.pk,
                }

        return ret


class SiteShareDelHandler(BaseHandler):
    allowed_method = ('GET', )
    model = Site

    def read(self, request):
        ret = {'status': False}
        site, user = None, None
        
        try:
            site = Site.objects.get(owner=request.user, pk=request.GET['site'])
        except (KeyError, Site.DoesNotExist):
            ret['error'] = _('Site not found')
            return ret

        try:
            user = site.share_with.get(pk=request.GET['user'])
        except (KeyError, User.DoNotExist):
            ret['error'] = _('User not found')
            return ret

        try:
            site.share_with.remove(user)
        except:
            ret['error'] = _('Something went wrong, try later')
        else:
            ret['status'] = True
            ret['user'] = {
                'username': user.username,
                'pk': user.pk,
            }

        return ret
