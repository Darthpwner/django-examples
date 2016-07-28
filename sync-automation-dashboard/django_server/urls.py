from django.conf.urls import patterns, url, include

from django.contrib.auth.models import User
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from views import *
from . import views

urlpatterns = [
    # 'django_server.views',
    # url(r'^$', 'home_view', name='posts'),
    # url(r'^category/(?P<pk>[0-9]+)/$', 'category_posts', name='category-posts'),
    # url(r'^(?P<slug>[\w\-_]+)/$', 'post_view', name='post'),
	url(r'^summary_server/$', views.SummaryList.as_view()),
	url(r'^summary_server/(?P<pk>[^/]+)/$', views.SummaryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
