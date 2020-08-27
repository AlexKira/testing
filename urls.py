#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'firstapp.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^1/', 'article.views.basic_one'),
                       url(r'^2/', 'article.views.template_two'),
                       url(r'^3/', 'article.views.template_three_simple'),
                       url(r'^articles/all/$', 'article.views.articles'),
                       url(r'^articles/get/(?P<article_id>\d+)/$', 'article.views.article'),
                       url(r'^articles/addlike/(?P<article_id>\d+)/$', 'article.views.addlike'),
                       url(r'^articles/addcomment/(?P<article_id>\d+)/$', 'article.views.addcomment'),
                       url(r'^page/(\d+)/$', 'article.views.articles'),
                       url(r'^$', 'article.views.articles'),

                       )
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)