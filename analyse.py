from collections import Counter
from nltk import *
import re
from nltk.stem import PorterStemmer
from nltk import ngrams
from nltk.corpus import stopwords
import glob


def analyse_article(filename,headline):
	f=open(filename,'r')
	afile=open("THEfile.html",'a')
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
	j=4
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
	f=open('analysed_'+filename[:-3]+'html','w')

	style="<style type='text/css'>#block{margin: 20px;display: inline-block;	border-style: groove;border-radius: 5px;width: 35em;box-shadow: 10px 10px 5px #888888;} #header{background: lightblue;padding: 15px;font-size:1.15em;font-family: 'roboto';} #article{background: lightyellow;padding: 9px;	font-size:1em;border-style: groove;}</style>"

	f.write(style+
	"<div id='block'>"+
	"<div id='header'>"+
		headline+
	"</div>"+
	"<div id='article'>"+
		 top_news+ 
	"</div>"+	
	"</div>")
	
	afile.write("<div id='block'>"+
	"<div id='header'>"+
		headline+
	"</div>"+
	"<div id='article'>"+
		 top_news+ 
	"</div>"+	
	"</div>")
	f.close()
	afile.close()

def analyse_all():
	txtCounter = len(glob.glob1('/home/yash/Summer Projects/news-crawler',"*.txt"))
	txtCounter-=2
	h=open('allHeads.txt','r')
	heads=h.read()
	afile=open("THEfile.html",'w')
	afile.write("<style type='text/css'>body{background: #100a0a;} #block{margin: 20px;display: inline-block;	border-style: groove;border-radius: 5px;width: 35em;box-shadow: 10px 7px 9px #204f4a;} #header{background: lightblue;padding: 15px;font-size:1.15em;font-family: 'roboto';} #article{background: lightyellow;padding: 9px;	font-size:1em;border-style: groove;}</style><body>")
	afile.close()
	#print(heads)
	heads=heads.split('\t')
	#print(heads)
	for i in range(0,txtCounter):
		analyse_article('news'+str(i)+'.txt',heads[i])
		