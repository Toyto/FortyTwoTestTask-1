from django.conf.urls import include, url
from django.contrib import admin
from apps.hello.views import IndexView


admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(), name='index'),
]
