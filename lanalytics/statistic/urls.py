from django.conf.urls.defaults import *

urlpatterns = patterns('lanalytics.statistic.views',
    url(r'^(?P<pk>\d+)\.html$', 'statistic', name='site_statistic'),
    url(r'^graph_(?P<pk>\d+)\.jpg$', 'analytic_graph',
        name='statistic_graph'),
)