from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('courses.views',

    url(r'^occurrence/(?P<id>\d+)/$', 'occurrence',
        name='occurrence'),
    
    url(r'^(?P<slug>[-\w]+)/$', 'detail',
        name='course'),

)