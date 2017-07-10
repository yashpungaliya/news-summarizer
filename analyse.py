from collections import Counter
from nltk import *
import re
from nltk.stem import PorterStemmer
from nltk import ngrams
from nltk.corpus import stopwords
import glob


def analyse_article(filename,headline):
	f=open(filename,'r')
	r=f.read()
	all_tokens_stemmed=[]
	all_bigrams=[]
	al_tokens=[]
	wo_sw=[]
	#stemmer=PorterStemmer()

	#stopwordsFile=open('english','r')
	#stopwordsText=stopwordsFile.read()
	#stopwords=stopwordsText.split('\n')

	eng_sw=stopwords.words('english')
	all_tokens=word_tokenize(r)
	all_sent=r.split('.')
	sent_freq=[]
	for i in range(0,100):
		sent_freq.append(0)
	for i,j in enumerate(all_tokens):
		all_tokens[i]=all_tokens[i].lower()

	for token in all_tokens:
		if token in eng_sw:
			continue
		#stemmed_token=stemmer.stem(token.lower())
		#all_tokens_stemmed.append(stemmed_token)
		wo_sw.append(token)
		bigrams=list(ngrams(all_tokens,5))
		all_bigrams=all_bigrams+bigrams

	freq_wo_sw=Counter(wo_sw)
	i=0
	for sent in all_sent:
		words_in_sent=sent.split(' ')
		for word in words_in_sent:
			sent_freq[i]=sent_freq[i]+freq_wo_sw[word]
		i=i+1	

	dictionary=dict(zip(all_sent,sent_freq))
	#print(dictionary)
	sorted_dict=sorted(dictionary.items(), key=lambda x: x[1],reverse=True)
	j=5
	top_news=""
	for x in sorted_dict:
		top_news+=x[0]+'.'+'\n'
		if j is 1:
			break
		j=j-1
		
	#print(top_news)
	#print(Counter(all_tokens_stemmed))
	freq=Counter(all_tokens)
	#print(freq)
	#print('-----------------------------')
	#freq1=Counter(all_tokens_stemmed)
	#print(freq1)
	#freq2=Counter(all_bigrams)
	#print(all_bigrams)
	#print(freq2.most_common(10))
	f.close()
	f=open('analysed_'+filename,'w')
	f.write("Headline : "+headline+"\n...........................................................................\n"+top_news)
	f.close()

def analyse_all():
	txtCounter = len(glob.glob1('/home/yash/Summer Projects/news-crawler',"*.txt"))
	txtCounter-=2
	h=open('allHeads.txt','r')
	heads=h.read()
	#print(heads)
	heads=heads.split('\t')
	#print(heads)
	for i in range(0,txtCounter):
		analyse_article('news'+str(i)+'.txt',heads[i])
		