from django.conf.urls import include, url
from django.contrib import admin
from apps.hello.views import IndexView, RequestView, CreateAuthView
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView
from django.conf.urls.static import static


admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^requests/$', RequestView.as_view(), name='requests'),
    url(r'^accounts/profile/register/$', CreateAuthView.as_view(), name='register'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^accounts/profile/$', RedirectView.as_view(url='register/')),
    url(r'^accounts/logout/$',
        'django.contrib.auth.views.logout', name='logout'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
