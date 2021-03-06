from django.conf.urls import patterns, url, include

from . import views


urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^search/$', views.search, name='search'),
    url(r'^congresista/(?P<congresista_slug>.*)$', views.congresista,
        name='congresista'),

    url(r'^(?P<short_url>[0-9a-z]*)/$', views.proyecto),
)
