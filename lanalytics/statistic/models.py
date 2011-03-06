from django.db import models
from django.contrib.auth.models import User


class Site(models.Model):
    owner = models.ForeignKey(User, related_name='lanalytic_sites')
    name = models.CharField(max_length=50)
    url = models.URLField(unique=False, verbose_name='URL')
    key = models.CharField(max_length=40, unique=True, verbose_name='Key')
    date_created = models.DateTimeField(auto_now_add=True)
    share_with = models.ManyToManyField(User, related_name='share_sites')

    @property
    def host_name(self):
        pref1 = 'http://'
        pref2 = 'https://'
        url = self.url

        if self.url[-1] == '/':
            url = self.url[:-1]

        return url.replace(pref1, '').replace(pref2, '')

    class Meta:
        unique_together = ('owner', 'url')

    def __unicode__(self):
        return "%s - %s" % (self.owner, self.url)


class BaseStatistic(models.Model):
    count = models.PositiveIntegerField(default=0)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-count', )


class Browser(BaseStatistic):
    site = models.ForeignKey(Site, related_name='browser')
    name = models.CharField(max_length=20)
    version = models.CharField(max_length=15)


class OS(BaseStatistic):
    site = models.ForeignKey(Site, related_name='os')
    name = models.CharField(max_length=20)
    version = models.CharField(max_length=15)


class Refferrer(BaseStatistic):
    site = models.ForeignKey(Site, related_name='refferrer')
    host = models.CharField(max_length=50)
    url = models.CharField(max_length=300)


class ScreenResolution(BaseStatistic):
    site = models.ForeignKey(Site, related_name='resolution')
    resolution = models.CharField(max_length=9)


class Flash(BaseStatistic):
    site = models.ForeignKey(Site, related_name='flash')
    version = models.CharField(max_length=20)
