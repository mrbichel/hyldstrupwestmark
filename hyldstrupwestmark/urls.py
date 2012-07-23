from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings

from django.contrib.auth.decorators import login_required
from flatblocks.views import edit

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'hyldstrupwestmark.views.index', name='index'),

    url(r'^courses/', include('courses.urls')),
    url(r'^flatblocks/(?P<pk>\d+)/edit/$', login_required(edit),
        name='flatblocks-edit'),
    url(r'^a/doc/', include('django.contrib.admindocs.urls')),
    url(r'^a/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
    (r'^media/(?P<path>.*)$',
        'serve', {
        'document_root': settings.MEDIA_ROOT,
        'show_indexes': True }),)