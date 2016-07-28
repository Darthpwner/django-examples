from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from django_server import views as django_server
from rest_framework import routers

# router = routers.DefaultRouter()
# # router.register(r'categories', django_server.CategorySetView)
# # router.register(r'posts', django_server.PostSetView)
# router.register(r'summary', django_server.SummarySetView)


urlpatterns = [
    url(r'^', include('django_server.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^summary_client/', 'ember_client.views.ember_view', name='home'),
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
