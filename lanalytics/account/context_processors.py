from django.contrib.sites.models import Site


def site(request):
    return {
    'active_site': Site.objects.get_current(),
    }