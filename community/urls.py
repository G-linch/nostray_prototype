# -*- coding: utf-8 -*-

from django.conf.urls import url, include

from community.views import AllPosts, PosterView


urlpatterns =[
    url(r'^allpost/$', AllPosts.as_view(), name='allpost'),
    url(r'^poster/$', PosterView.as_view(), name='poster'),
]