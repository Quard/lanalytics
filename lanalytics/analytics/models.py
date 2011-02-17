from django.db import models

from lanalytics.statistic.models import Site


class Analytic(models.Model):
    site = models.ForeignKey(Site, related_name='analytics')
    visitor = models.CharField(max_length=32)
    browser = models.CharField(max_length=20)
    browser_version = models.CharField(max_length=15)
    platform = models.CharField(max_length=20)
    platrorm_version = models.CharField(max_length=15)
    time_zone = models.IntegerField()

    screen_resolution = models.CharField(max_length=9)
    window_dimensions = models.CharField(max_length=9)
    enabled_cookie = models.BooleanField()
    have_flash = models.BooleanField()
    have_java = models.NullBooleanField()

    refferrer = models.URLField(max_length=500, null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True)
