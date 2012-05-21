from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from workshop import settings
from django.views.generic.simple import direct_to_template

admin.autodiscover()

urlpatterns = patterns('',

    ('^$', direct_to_template, {
        'template': 'home.html'
    }),
    # upload
    url(r'^upload/$', 'upload.views.upload_handler'),
    url(r'^upload/code$', 'upload.views.upload_code'),

    # code
    url(r'^source/$', 'source.views.index'),

    # admin
    url(r'^admin/', include(admin.site.urls)),

    url(r'^upload/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
        }),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
        }),
)
