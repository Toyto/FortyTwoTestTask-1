from django.conf.urls import include, url
from django.contrib import admin
from apps.hello.views import IndexView, RequestView, CreateAuthView
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static


admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^requests/$', RequestView.as_view(), name='requests'),
    url(r'^register/$', CreateAuthView.as_view(), name='register'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
