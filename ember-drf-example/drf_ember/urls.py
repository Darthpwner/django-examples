from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from django_server import views as django_server
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categories', django_server.CategorySetView)
router.register(r'posts', django_server.PostSetView)


urlpatterns = patterns(
    '',
    url(r'^$', 'ember_client.views.ember_view', name='home'),
    url(r'^posts/$', 'ember_client.views.ember_view', name='home'),
    url(r'^posts/(?P<slug>[\w\-_]+)/$', 'ember_client.views.ember_view', name='home'),
    url(r'^category/(?P<id>[\w\-_]+)/$', 'ember_client.views.ember_view', name='home'),
    url(r'^django_server/', include('django_server.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
