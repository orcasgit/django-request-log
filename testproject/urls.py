from django.conf.urls import include, patterns, url
from django.contrib import admin

from . import views


admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    url(r'^create-log/$', views.create_requestlog, name='create_requestlog'),
    (r'', include('django.contrib.auth.urls')),
)
