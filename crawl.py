import urllib.request as req
import re
from bs4 import BeautifulSoup
import json


f= open("newsData.txt","w+")
def get_current_html(url):
	r=req.urlopen(url).read()
	data=r.decode("utf-8")
	soup=BeautifulSoup(data,'html.parser')
	article_heading=soup.find_all("h1",itemprop="headline")
	dateline=""
	dateline=soup.find("div",{"class":"ins_dateline"})
	if dateline is not None:
		dateline=dateline.text
		dateline=dateline.replace(":","-")
	head=article_heading[0].text.strip(' \t\n\r')
	head = head.replace(u"\u00A0", " ")
	head=head.replace(","," ")
	head=head.replace("-"," ")
	head=head.replace("'","")
	head=head.replace(":"," ")
	head=head.replace(";"," ")
	head=head.replace("%","pc")
	head=head.replace("Mr.","Mr")
	head = head.replace(":", " ")
	head=re.sub( '\s+', ' ', head ).strip()
	small_descript=""
	summary=""
	small_descript=soup.find_all("h2")
	if len(small_descript) is not 0:
		summary = small_descript[0].text.strip(' \t\n\r')
		summary = summary.replace(u"\u00A0", " ")
		summary = summary.replace(":", " ")
		summary = summary.replace("-", " ")
		summary = summary.replace("'", "")
		summary = summary.replace(",", " ")
		summary = summary.replace(";", " ")
		summary.replace("Mr.","Mr")
		summary.replace("Ms.","Ms")
		summary.replace("Mrs.","Mrs")
		summary = summary.replace("%", "pc")
		summary=re.sub( '\s+', ' ', summary ).strip()
	large_descript=""
	body=""
	large_descript=soup.find_all("div",itemprop="articleBody")
	if len(large_descript) is not 0:
		body=large_descript[0].text.strip(' \t\n\r')
		body = body.replace(u"\u00A0", "")
		body = body.replace("\"", " ")
		#body = body.replace("'", "")
		#body = body.replace("-", " ")
		body = body.replace(":", " ")
		body = body.replace("Mr.", "Mr")
		body = body.replace("Mrs.", "Mrs")
		body = body.replace("Ms.", "Ms")
		body = body.replace("Highlights", " ")
		body = body.replace(";", " ")
		#body = body.replace(","," ")
		#body = body.replace("%","pc")
		body = re.sub( '\s+', ' ', body ).strip()
	data={"head":head,"summary":summary,"body":body,"dateline":dateline}
	json_data = json.dumps(data)
	f.write(json_data+';')

def crawl_from_home():
	home_url="http://www.ndtv.com"
	r=req.urlopen(home_url).read()
	data=r.decode("utf-8")
	soup=BeautifulSoup(data,'html.parser')
	links=[]
	articles=soup.find_all("a",{"class":"item-title"})
	for article in articles:
		article=str(article)
		if "www.ndtv.com" in article and "home-prime" not in article and "video" not in article:
			m=re.search("href",article)
			start=m.start()+6
			l=article[start:]
			m=re.search(">",l)
			end=m.end()-2
			link=l[:end]
			links.append(link)
	print(links)			
	links=links[:-11]
	i=100	
	for l in links:
		get_current_html(l)
		i=i-1
		if i is 0:
			break
	


def head_list():
	string=""
	f=open("newsData.txt","r+")	
	file_data=f.read()
	arr=file_data.split(';')
	j=0
	for i in arr:
		k=str(j)
		art=""
		try:
			art=json.loads(i)['body']
			if len(art) > 10:
				print("File:"+k)		
				newsFile= open("news"+k+".txt","w+")
				newsFile.write(art)
				string+=json.loads(i)['head']+'\t'
				j=j+1
		except:
			print("Found All Links")	
		finally:
			#print("done")		
			f.close()		
	return string


def main():
	f= open("newsData.txt","w+")
	crawl_from_home()
	f.close()
	a=head_list()
	heads_file=open("allHeads.txt",'w')
	heads_file.write(a)
	heads_file.close()

