#coding=utf-8

from django.conf.urls import url
from D3js.views import hello,echart, wordcloud, fenci, segmentation, generate, download

urlpatterns = [url(r'^$', hello),
               url(r'echart/$', echart),
               url(r'wordcloud/$', wordcloud, {'template_name': 'wordcloud.html'}),
               url(r'segmentation/$', segmentation),
               url(r'generate/$', generate),
               url(r'download/$', download),
               url(r'fenci/$', fenci),]