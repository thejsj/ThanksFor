from django.conf.urls import patterns, include, url
from thanksfor.views import *
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, }),
   	url(r'^$', 'thanksfor.views.main', name='main'),
)

static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)