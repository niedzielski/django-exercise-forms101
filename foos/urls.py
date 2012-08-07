from django.conf.urls import patterns, include, url

urlpatterns = patterns('foos.views',
    url(r'^$', 'foo'),
)
