#
from wordcloud import WordCloud  ,STOPWORDS
from web.settings import BASE_DIR
import jieba

def gcloud(text, name):
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
    stoplist = stopwords.split(';')
    cut = jieba.cut(text)
    result = ""
    for word in cut:
        if word not in stoplist:
            result += word + " "
    print(result)
    return result

