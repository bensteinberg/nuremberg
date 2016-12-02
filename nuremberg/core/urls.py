from django.conf.urls import include, url
from django.contrib import admin
from httpproxy.views import HttpProxy
from django.views.generic.base import RedirectView
from django.http import HttpResponse

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^transcripts/', include('nuremberg.transcripts.urls')),
    url(r'^documents/', include('nuremberg.documents.urls')),
    url(r'^photographs/', include('nuremberg.photographs.urls')),
    url(r'^search/', include('nuremberg.search.urls')),
    url(r'^', include('nuremberg.content.urls')),
    url(r'^proxy_image/printing/(?P<url>.*)$',
        # RedirectView.as_view(url='http://nuremberg.law.harvard.edu/imagedir/HLSL_NUR_printing/%(url)s')),
        HttpProxy.as_view(base_url='http://nuremberg.law.harvard.edu/imagedir/HLSL_NUR_printing')),
    url(r'^proxy_image/(?P<url>.*)$',
        # RedirectView.as_view(url='http://s3.amazonaws.com/nuremberg-dev/%(url)s'))
        HttpProxy.as_view(base_url='http://s3.amazonaws.com/nuremberg-dev')),
    url(r'^robots.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /search/", content_type="text/plain")),
]

handler400 = 'nuremberg.core.views.handler400'
handler403 = 'nuremberg.core.views.handler403'
handler404 = 'nuremberg.core.views.handler404'
handler500 = 'nuremberg.core.views.handler500'
