#coding=utf-8

from django.conf.urls import url
from D3js.views import hello, imagenet, imagA, wordcloud, fenci, segmentation, generate, download, upload_file

urlpatterns = [url(r'^$', hello),
               url(r'imagenet/$',imagenet, {'template_name': 'imagenet.html'}),
               url(r'wordcloud/$', wordcloud, {'template_name': 'wordcloud.html'}),
               url(r'segmentation/$', segmentation),
               url(r'generate/$', generate),
               url(r'download/$', download),
               url(r'fenci/$', fenci),
               url(r"imgA/$", imagA),
               url(r"imagenet/upload_file/$", upload_file, {'template_name': 'imagenet.html'}),
               ]