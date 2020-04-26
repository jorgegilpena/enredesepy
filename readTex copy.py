string = "Python is awesome Madrid Jobandtalent, isn't it?"
substring = "is"

keywords = open('keywords.txt','r')

for keyword in keywords:
    keywordstr=str(keyword)
    count = string.count(keywordstr)
    print (count,' ',keywordstr)


# print count
print("The count is:", count)
