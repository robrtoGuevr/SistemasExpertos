import urllib.request
import re
import nltk
import heapq
#import goslate
from inscriptis import get_text
from nltk import word_tokenize, sent_tokenize
from googletrans import *
#nltk.download()

enlace = "https://www.newyorker.com/contributors/stephen-king"
html = urllib.request.urlopen(enlace).read().decode('utf-8')
text = get_text(html)
article_text = text
article_text = article_text.replace("[ edit ]", "")
print("##################")

article_text = re.sub(r'\[[0-9]*\']', ' ', article_text)
article_text = re.sub(r'\s+', ' ', article_text)

formatted_article_text = re.sub(r'\[^a-zA-Z]', ' ', article_text)
formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

sentence_list = nltk.sent_tokenize(article_text)

stopwords = nltk.corpus.stopwords.words('english')

word_frecuencies = {}
for word in nltk.word_tokenize(formatted_article_text):
    if word not in stopwords:
        if word not in word_frecuencies.keys():
            word_frecuencies[word] = 1

sentence_scores = {}
for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frecuencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frecuencies[word]
                else:
                    sentence_scores[sent] += word_frecuencies[word]

maximun_frequncy = max(word_frecuencies.values())

for word in word_frecuencies.keys():
    word_frecuencies[word] = (word_frecuencies[word]/maximun_frequncy)

#RESUMEN CON LAS MEJORES FRASES
summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
summary = ' '.join(summary_sentences)

translator = Translator()
traslated=translator.translate(summary, dest='spanish')
print(traslated.text)