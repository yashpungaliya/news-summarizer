from collections import Counter
from nltk import *
import re
from nltk.stem import PorterStemmer
from nltk import ngrams
from nltk.corpus import stopwords
import glob


def analyse_article(filename,headline):
	f=open(filename,'r')
	afile=open("Material.html",'a')
	r=f.read()
	if len(r)>12000:
		return
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
	sorted_dict=sorted(dictionary.items(), key=lambda x: x[1],reverse=True)
	j=4
	top_news=""
	for x in sorted_dict:
		top_news+=x[0]+'.'+'\n'
		if j is 1:
			break
		j=j-1
		
	freq=Counter(all_tokens)
	
	f.close()	
	afile.write('<div class="col m4">'+
       '<div class="card small hoverable">'+
          '<div class="card-image waves-effect waves-block waves-light">'+
            '<img class="activator" src="myimg.png">'+
          '</div>'+
          '<div class="card-content">'+
            '<span class="card-title activator grey-text text-darken-4">'+headline+'</span>'+
             '</div>'+
          '<div class="card-reveal">'+
            '<span class="card-title grey-text text-darken-4">'+headline+'<i class="material-icons right">close</i></span>'+
            '<p>'+top_news+'</p>'+
          '</div>'+
        '</div>'+
      '</div>'+
      '<!-- end of col -->')
	f.close()
	afile.close()

def analyse_all():
	txtCounter = len(glob.glob1('/home/yash/Summer Projects/news-crawler',"*.txt"))
	txtCounter-=2
	h=open('allHeads.txt','r')
	heads=h.read()
	afile=open("Material.html",'w')
	afile.write('<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.0/jquery.min.js"></script><!DOCTYPE html><html><head><link href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.6/css/materialize.min.css" rel="stylesheet">  <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.6/js/materialize.min.js"></script>  <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.0.0-beta1/jquery.min.js"></script> <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet"></head><body>    <nav>        <div class="navbar-wrapper container">          <a href="#" class="brand-logo">InWords</a>          <ul class="right">            <li><a href="#">Home</a></li>            <li><a href="#">About</a></li>            <li><a href="#">Contact Us</a></li>            </ul>            </div>    </nav>'+
		'<div class="container">'+
		'<div class="row">')	
	afile.close()
	#print(heads)
	heads=heads.split('\t')
	#print(heads)
	for i in range(0,txtCounter):
		print("Summarizing article-"+str(i))
		analyse_article('news'+str(i)+'.txt',heads[i])
		
