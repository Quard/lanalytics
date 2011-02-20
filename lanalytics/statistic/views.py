import urllib2
from random import randint
from hashlib import sha1
from datetime import datetime, timedelta
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from annoying.decorators import render_to

from lanalytics.statistic.models import Site, Browser, OS, Refferrer, \
    ScreenResolution, Flash
from lanalytics.analytics.models import Analytic


@login_required
@render_to('statistic/statistic.html')
def statistic(request, pk):
    site = get_object_or_404(Site, pk=pk)
    date_start = datetime.now() - timedelta(days=1)
    date_end = datetime.now()
    content = {
        'site': site,
        'date_start': date_start,
        'date_end': date_end,
        'current_menu': 'my-sites',
    }

    qs = list(Browser.objects.filter(site=site, version=None))
    chart_browsers = 'chd=t:%s&chl=%s' % (
        ','.join([str(i.count) for i in qs]),
        '|'.join([i.name for i in qs]),
    )
    content['chart_browsers'] = chart_browsers

    qs = list(Browser.objects.filter(site=site, version__isnull=False))
    chart_browsers_version = 'chd=t:%s&chl=%s' % (
        ','.join([str(i.count) for i in qs]),
        '|'.join(['%s %s' % (i.name, i.version) for i in qs]),
    )
    content['chart_browsers_version'] = chart_browsers_version

    qs = list(OS.objects.filter(site=site, version=None))
    chart_os = 'chd=t:%s&chl=%s' % (
        ','.join([str(i.count) for i in qs]),
        '|'.join([i.name for i in qs]),
    )
    content['chart_os'] = chart_os

    # qs = list(OS.objects.filter(site=site, version__isnull=False))
    # chart_os_version = 'chd=t:%s&chl=%s' % (
    #     ','.join([str(i.count) for i in qs]),
    #     '|'.join(['%s %s' % (i.name, i.version) for i in qs]),
    # )
    # content['chart_os_version'] = chart_os_version

    qs = list(ScreenResolution.objects.filter(site=site))
    chart_resolution = 'chd=t:%s&chl=%s' % (
        ','.join([str(i.count) for i in qs]),
        '|'.join([i.resolution for i in qs]),
    )
    content['chart_resolution'] = chart_resolution

    qs = list(Refferrer.objects.filter(site=site))
    chart_referrer = 'chd=t:%s&chl=%s' % (
        ','.join([str(i.count) for i in qs]),
        '|'.join([i.host for i in qs]),
    )
    content['chart_referrer'] = chart_referrer

    qs = list(Flash.objects.filter(site=site))
    chart_flash = 'chd=t:%s&chl=%s' % (
        ','.join([str(i.count) for i in qs]),
        '|'.join([i.version for i in qs]),
    )
    content['chart_flash'] = chart_flash

    return content


@login_required
def analytic_graph(request, pk):
    site = get_object_or_404(Site, pk=pk)
    date_start = datetime.now() - timedelta(hours=24)
    date_end = datetime.now()
    statistic = []
    qs = Analytic.objects.filter(site=site, date_created__gte=date_start,
        date_created__lte=date_end).order_by('date_created')
    dt = None
    if qs:
        dt = qs[0].date_created

    count = 0
    _delta = settings.STATISTIC_GRAPH_DELTA
    delta = None
    if qs:
        delta = (qs[0].date_created - date_start).seconds
        if delta >= _delta:
            statistic.extend([0] * ((delta - _delta) / _delta))

    for obj in qs:
        count += 1
        delta = (obj.date_created - dt).seconds
        if delta >= _delta:
            statistic.append(count)
            count = 1
            if delta >= _delta * 2:
                statistic.extend([0] * ((delta - _delta) / _delta))
            dt = obj.date_created

    statistic.append(count)
    if delta >= _delta:
        statistic.extend([0] * ((delta - _delta) / _delta))

    delta = (date_end - obj.date_created).seconds
    if delta >= _delta:
        statistic.extend([0] * ((delta - _delta) / _delta))

    st = ','.join(map(str, statistic))
    print st
    post = {
        'cht': 'ls',
        'chs': '800x200',
        'chd': 't:%s' % st,
        'chxr': '0,0,%s' % max(statistic),
        'chxt': 'y',
        'chma': '2',
        'chls': '1',
        'chg': '0,10,0,0',
    }
    f = urllib2.urlopen(
        'https://chart.googleapis.com/chart?chid=%s' % sha1(st).hexdigest(),
        '&'.join(['%s=%s' % (k, v) for k, v in post.items()])
    )

    response = HttpResponse(mimetype='image/jpeg')
    response.write(f.read())

    return response
