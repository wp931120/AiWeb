from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from D3js.apis import gcloud , segment, imgnet
from django.http import FileResponse
import os
from web.settings import BASE_DIR


def hello(request):
    return render(request, 'mainpage.html')

def imagenet(request,template_name):
    picname = '/static/img/word.jpg'
    param = {
        'picname': picname
    }
    return render(request, template_name, param)


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
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename={}'.format(file_name)
    return response


def upload_file(request,template_name):
    result = {'status': '', 'up_src': ''}
    if request.method == "POST":    # 请求方法为POST时，进行处理
        myFile = request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return HttpResponse("no files for upload!")
        destination = open(BASE_DIR+"/static/imgnet/{}".format(myFile.name), 'wb+')    # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():      # 分块写入文件
            destination.write(chunk)
        destination.close()
        up_src = "/static/imgnet/{}".format(myFile.name)
        result["up_src"] = up_src
        result['status'] = 1
        param = {
            'picname': '/static/img/word.jpg',
            'upload_name': up_src
        }
        return render(request, template_name, param)

# def showimg(request):
#    if request.method == "POST":
#        try:
#            result = {'status': '', 'up_src': ''}
#            myFile = request.FILES.get("myfile", None)
#            up_src = BASE_DIR + "/D3js/Img/{}".format(myFile.name)
#            result["up_src"] = up_src
#            result['status'] = 1
#        except Exception as e:
#            result['status'] = 0
#            result['res'] = str(e)
#        return  JsonResponse(result)




def imagA(request):
    if request.method == "POST":
        result = {'status': '', 'res': ''}
        try:
             filename = os.listdir(BASE_DIR+"/static/imgnet/")
             if len(filename) == 0:
                 result['status'] = '1'
                 result['res'] = "请上传图片"
                 return JsonResponse(result)
             else:
                 response = imgnet(BASE_DIR+"/static/imgnet/{}".format(filename[0]))
                 result['res'] = response
                 result['status'] = '1'
                 os.remove(BASE_DIR+"/static/imgnet/{}".format(filename[0]))
        except Exception as e:
            result['res'] = str(e)
        return JsonResponse(result)

