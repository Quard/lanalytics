from django.db import models

from lanalytics.statistic.models import Site


class Analytic(models.Model):
    site = models.ForeignKey(Site, related_name='analytics')
    path = models.TextField()
    visitor = models.IPAddressField()
    browser = models.CharField(max_length=20)
    browser_version = models.CharField(max_length=15)
    platform = models.CharField(max_length=20)
    time_zone = models.CharField(max_length=20, blank=True, default='')

    screen_resolution = models.CharField(max_length=9)
    window_dimensions = models.CharField(max_length=9)
    enabled_cookie = models.BooleanField()
    flash = models.CharField(max_length=30)
    have_java = models.BooleanField(default=False)

    referrer = models.URLField(max_length=500, null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s / %s" % (self.site, self.browser)