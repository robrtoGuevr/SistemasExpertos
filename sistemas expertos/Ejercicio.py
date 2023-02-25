import urllib.request
import re
import nltk
import heapq
#import goslate
from inscriptis import get_text
from nltk import word_tokenize, sent_tokenize
from googletrans import *
#nltk.download()

texto = "This article is about the book by Stephen King. For the television series based on the book, see 11.22.63. For the date, see November 1963 § November 22, 1963 (Friday). For other uses, see 11-22-63. 11/22/63 is a novel by Stephen King about a time traveller who attempts to prevent the assassination of United States President John F. Kennedy, which occurred on November 22, 1963 (the novel's titular date).[1][2] It is the 60th book published by Stephen King, his 49th novel and the 42nd under his own name. The novel was announced on King's official site on March 2, 2011.[3] A short excerpt was released online on June 1, 2011,[4] and another excerpt was published in the October 28, 2011, issue of Entertainment Weekly.[5] The novel was published on November 8, 2011[6] and quickly became a number-one bestseller. It stayed on The New York Times Best Seller list for 16 weeks.[7] 11/22/63 won the 2011 Los Angeles Times Book Prize for Best Mystery/Thriller and the 2012 International Thriller Writers Award for Best Novel,[8][9] and was nominated for the 2012 British Fantasy Award for Best Novel[10] and the 2012 Locus Award for Best Science Fiction Novel.[11] The novel required considerable research to accurately portray the late 1950s and early 1960s.[12] King commented on the amount of research it required, saying I've never tried to write anything like this before. It was really strange at first, like breaking in a new pair of shoes.[12] The novel was adapted into a Hulu television series in 2016, 11.22.63."
#enlace=""
#html = urllib.request.urlopen(enlace).read().decode('utf-8')
#text = get_text(html)
#article_text = text
#article_text = article_text.replace("[ edit ]", "")
print("###########################################################################")

#article_text = re.sub(r'\[[0-9]*\']', ' ', article_text)
#article_text = re.sub(r'\s+', ' ', article_text)

#formatted_article_text = re.sub(r'\[^a-zA-Z]', ' ', article_text)
#formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

sentence_list = nltk.sent_tokenize(texto)

stopwords = nltk.corpus.stopwords.words('english')

word_frecuencies = {}
for word in nltk.word_tokenize(texto):
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