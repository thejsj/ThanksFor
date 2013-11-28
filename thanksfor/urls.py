from django.conf.urls import patterns, include, url
from thanksfor.views import *
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^admin/', include(admin.site.urls)),

    # Media
    url(r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, }),

    # Main View
   	url(r'^$', 'thanksfor.views.main', name='main'),

    # Api
   	url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Ajax
    url(r'^upload-image/', 'thanksfor.views.ajax_upload', name='ajax_upload'),
   	
)

static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)