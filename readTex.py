##Librarys
import feedparser
print('..............................................setup')
counter=0
import re
def count_substring(string, sub_string):
    #regex = '(?='+sub_string+')'
    # print(regex)
    return len(re.findall(regex,string))




strin =str("Madrid al cielo")
str="Madrid al cielo"

keywords = open('keywords.txt','r')
for keyword in keywords:
     #keyword=str(keyword)
     print(keyword)
     counter1=strin.count(keyword)
     if counter1 !=0:
          print (value,' ',keyword)
          counter2 = str1.count(keyword)
     else:
          print('no')
##Ficheros

keywords.close()
print('total=',counter)
 


