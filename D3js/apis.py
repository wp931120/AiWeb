import keras
from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
from wordcloud import WordCloud  ,STOPWORDS
from web.settings import BASE_DIR
import jieba
from translate import Translator
translator = Translator(to_lang="zh")
"""
defeine some apis

"""

def gcloud(text, name):
    """
    用于生成词云
    :param text:
    :param name:
    :return:
    """
    wordlist = jieba.cut(text)
    wordstring = ' '.join(wordlist)
    wordcloud = WordCloud(
         font_path = BASE_DIR + '/static/' + 'msyh.ttc',
         stopwords=STOPWORDS,
        ).generate(wordstring)
    dic = BASE_DIR +'/static' +'/wordcloud_pic/'
    picpath = dic + name + ".png"
    print(picpath)
    wordcloud.to_file(picpath)

def segment(text,stopwords):
    """
    用于分词
    :param text:
    :param stopwords:
    :return:
    """
    stoplist = stopwords.split(';')
    cut = jieba.cut(text)
    result = ""
    for word in cut:
        if word not in stoplist:
            result += word + " "
    print(result)
    return result

def imgnet(imgpath):
    """
    用于图像识别
    :param imgpath:
    :return:
    """

    keras.backend.clear_session()
    model = ResNet50(weights='imagenet')
    img_path = imgpath
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    res = decode_predictions(preds, top=3)[0][1][1]
    translator = Translator(to_lang="zh")
    translator.translate(res)
    return translator.translate(res)
