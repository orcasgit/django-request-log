from django.conf.urls import include, patterns, url


urlpatterns = patterns('',
    (r'', include('django.contrib.auth.urls')),
)
