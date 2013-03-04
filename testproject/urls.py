from django.conf.urls import include, patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^create-log/$', views.create_requestlog, name='create_requestlog'),
    (r'', include('django.contrib.auth.urls')),
)
