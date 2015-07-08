from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^', include('apps.hello.urls')),
                       url(r'^admin/', include(admin.site.urls),
                           name='django-admin'),
                       url(r'^admin/doc/',
                           include('django.contrib.admindocs.urls')),

                       (r'^admin/jsi18n/',
                           'django.views.i18n.javascript_catalog'),
                       (r'^uploads/(?P<path>.*)$',
                           'django.views.static.serve',
                           {'document_root': settings.MEDIA_ROOT}),

                       )
urlpatterns += staticfiles_urlpatterns()
