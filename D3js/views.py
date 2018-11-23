from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from D3js.apis import gcloud , segment
from django.http import FileResponse
import json
def hello(request):
    return render(request, 'mainpage.html')

def echart(request):
    return render(request, 'Echart.html')

def wordcloud(request, template_name):
    name = '/static/img/word.jpg'
    param = {
        'picname': name
    }
    return render(request, template_name, param)

def segmentation(request):
    return render(request, 'segmentation.html')

def generate(request):
    """
    用于生成词云
    """
    result = {'word': '', 'name': ''}
    try:
        word = str(request.GET.get("words"))
        name = str(request.GET.get("name"))
        gcloud(word, name)
        result['word'] = word
        result['name'] = name + '.png'
    except Exception as e:
        result['status'] = str(e)
    return JsonResponse(result)


def fenci(request):
    result = {'status': '', 'segwords': ''}
    try:
        sentance = str(request.POST.get("sen"))
        stopwords = str(request.POST.get("stop"))
        seg_sentance = segment(sentance, stopwords)
        result['segwords'] = seg_sentance
        result['status'] = '1'
    except Exception as e:
        result['segwords'] = str(e)
    return JsonResponse(result)



def download(request):
    """
    用于下载
    """
    file_name = request.GET.get("name") + '.png'
    filename = '/root/web/static/wordcloud_pic/{}'.format(file_name)
    file = open(filename, 'rb')
    response = FileResponse(file)
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename={}'.format(file_name)
    return response