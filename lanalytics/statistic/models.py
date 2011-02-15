from django.db import models


class BaseStatistic(models.Model):
    count = models.PositiveIntegerField(default=0)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Browser(BaseStatistic):
    name = models.CharField(max_length=20)
    version = models.CharField(max_length=15)


class OS(BaseStatistic):
    name = models.CharField(max_length=20)
    version = models.CharField(max_length=15)


class Refferrer(BaseStatistic):
    host = models.CharField(max_length=50)
    url = models.CharField(max_length=300)


class ScreenResolution(BaseStatistic):
    resolution = models.CharField(max_length=9)
