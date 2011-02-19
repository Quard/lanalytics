import urlparse
from django.core.management.base import NoArgsCommand

from lanalytics.analytics.models import Analytic
from lanalytics.statistic.models import Site, Browser, OS, Refferrer, \
    ScreenResolution


class Command(NoArgsCommand):

    def handle_noargs(sef, **options):
        for site in Site.objects.all():
            browser = {}
            os = {}
            refferrer = {}
            resolution = {}

            last_update = Browser.objects.filter(site=site)\
                .order_by('-last_update')
            qs = None
            if last_update:
                qs = Analytic.objects.filter(
                    site=site,
                    date_created__gte=last_update[0].last_update
                )
            else:
                qs = Analytic.objects.filter(site=site)

            for an in qs:
                # browser
                if not an.browser in browser:
                    browser[an.browser] = {'__count__': 0}
                    
                if an.browser_version:
                    if not an.browser_version in browser[an.browser]:
                        browser[an.browser][an.browser_version] = 0
                    browser[an.browser][an.browser_version] += 1

                browser[an.browser]['__count__'] += 1

                # os
                if not an.platform in os:
                    os[an.platform] = {'__count__': 0}
                    
                if an.platform_version:
                    if not an.platform_version in os[an.platform]:
                        os[an.platform][an.platform_version] = 0
                    os[an.platform][an.platform_version] += 1

                os[an.platform]['__count__'] += 1

                # refferrer
                if not an.refferrer in refferrer:
                    refferrer[an.refferrer] = 0

                refferrer[an.refferrer] += 1

                # screen resolution
                if not an.screen_resolution in resolution:
                    resolution[an.screen_resolution] = 0

                resolution[an.screen_resolution] += 1

            for br in browser.keys():
                for ver in browser[br].keys():
                    obj, created = Browser.objects.get_or_create(
                        site=site,
                        name=br,
                        version=ver != '__count__' and ver or None
                    )
                    obj.count += browser[br][ver]
                    obj.save()

            for o in os.keys():
                for ver in os[o].keys():
                    obj, created = OS.objects.get_or_create(
                        site=site,
                        name=o,
                        version=ver != '__count__' and ver or None
                    )
                    obj.count += os[o][ver]
                    obj.save()

            for ref in refferrer.keys():
                url = urlparse.urlparse(ref)
                obj, created = Refferrer.objects.get_or_create(
                    site=site,
                    host=url.netloc
                )
                obj.count += refferrer[ref]
                obj.save()

            for res in resolution.keys():
                obj, created = ScreenResolution.objects.get_or_create(
                    site=site,
                    resolution=res,
                )
                obj.count += resolution[res]
                obj.save()
