from django.conf.urls import include, url
from django.contrib import admin

from . import views


admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^create-log/$', views.create_requestlog, name='create_requestlog'),
    url(r'', include('django.contrib.auth.urls')),
]
