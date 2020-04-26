
##funciones
##def find_words(text, search):
  ##  """Find exact words"""
   ## dText   = text.split()
   ## dSearch = search.split()

##    found_word = 0

  ##  for text_word in dText:
    ##    for search_word in dSearch:
      ##      if search_word == text_word:
        ##        found_word += 1

##    if found_word == len(dSearch):
  ##      return lenSearch
    ##else:
      ##  return False

##coding=utf-8
# -*- coding: utf-8 -*-


# HTML String
html = """
<html>
<body>
<h1>ENREDESE APRENDIENDO</h1>
<br></br>
"""
htmlend="""
</body>
</html>
"""

# Write HTML String to file.html
recomendations = open("news.html", "w")
recomendations.write(html)

    


##Librarys
import feedparser
import webbrowser


print('..............................................setup')
counter=0

def find_words(text, search):
    ##str2--int numero de veces que aparece en text, una de las palabras de search
    dText   = text.split()
    dSearch = search.split()
    found_word = 0
    for text_word in dText:
        for search_word in dSearch:
            if search_word == text_word:found_word += 1
    return found_word

##Ficheros
news = open('news.txt', 'w')
print('start reading rss')
feeds = open('feeds.txt','r')
found_word=0
found_word_des=0
found_word_title=0
counter=0
#Recorre Feeds
for feed in feeds:
	print ('\n\n\n NEW FEEED===============' + feed)
	noticias = feedparser.parse(feed)
        #print ('des: ' + noticias.feed.description + '\n')
	##print('title: ' + noticias.entries[0].title + '\n')

	#Recorre Noticias
        for noticia in noticias.entries:               
                #if noticia.date <
                print (noticia.date_parsed)
                title = str(noticia.title.encode('utf-8'))
                ##print('-title: ' + title)
                ##print(noticia)
                print('-des: ', noticia.description)
                print('-title: ', noticia.title)
                ##keywords=keywordsfile.readlines()
                ##print(keywords)
                keywords = open('keywords.txt','r')
                for keyword in keywords:
                        ##keyword=str(keyword)
                        print(keyword)
                        ##list_of_words = title.split()
                        found_word_title=find_words(keyword,title)
                        found_word_des=find_words(keyword,noticia.description)
                        if found_word_title !=0 or found_word_des !=0:
                                print('yes', found_word_title,found_word_des)
                                #value = title.count(keyword)
                                print(noticia.link)
                               # print (value)
                                counter=counter+found_word_title+found_word_des
                                news.write(noticia.link + 'x \n')

                                htmlurl='<strong>' +keyword+'</strong> <span><a href="'+ noticia.link +'"> '+ noticia.title +'</a> - '+ noticia.description[:150] + '<br></br><br></br><br></br> -' 
                                print(htmlurl)
                                htmlurl=str(htmlurl.encode('utf-8'))
                                recomendations.write(htmlurl)
                        else:
                                print('no')
                keywords.close()
                
news.close()
print('total=',counter)
recomendations.write(htmlend)

recomendations.close()
webbrowser.open('file:///Users/jgilpena/test/news.html')


