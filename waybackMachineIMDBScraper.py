#!/usr/bin/env python
# coding: utf-8

# IMDB Scraper from Wayback Machine

# In[ ]:


import sys
import requests as rq
from bs4 import BeautifulSoup as bs
import json
import pandas as pd
import csv
import re


# filmID input Ex: tt0120338

# In[ ]:


filmId= input("filmID: ")
film='https://www.imdb.com/title/'+filmId
filePath = input("File path: "+"r'")


# In[ ]:


with open(filePath+"/"+filmId+".csv", mode='w', newline='') as newFolder:
    newWriter = csv.writer(newFolder, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
    newWriter.writerow(['Year'+";"+'Month'+";"+'Day'+";"+'Hours'+";"+'Rating'+";"+'Toplam Oy'])
    newFolder.close()


# Part1

# In[ ]:


startTime='20070228'
finishTime='20070331'


# In[ ]:


url = 'http://web.archive.org/cdx/search/cdx?url='+film+'/&collapse=digest&from='+startTime+'&to='+finishTime+'&output=json'


# In[ ]:


urls = rq.get(url).text


# In[ ]:


parse_url = json.loads(urls)


# In[ ]:


url_list = []
for i in range(1,len(parse_url)):
    orig_url = parse_url[i][2]
    tstamp = parse_url[i][1]
    waylink = 'https://web.archive.org/web/'+tstamp+'/'+orig_url
    url_list.append(waylink)    


# In[ ]:


for i in range(len(url_list)):
    try:
        final_url=url_list[i]
        req = rq.get(final_url).text
        print(req)
        break
        soup = bs(req,'html.parser')
        classScraper = soup.find(class_='rating')
        tagScraper1 = classScraper.find_all('b')
        tagScraper2 = classScraper.find_all('a')
        print(final_url[28:42]+";"+tagScraper1[1].contents[0].replace('/10','')+";"+tagScraper2[2].contents[0].replace('votes','').replace(',',''))
        with open(filePath+"/"+filmId+".csv", mode='a', newline='') as newFolder:
            newWriter = csv.writer(newFolder, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
            newWriter.writerow([final_url[28:32]+";"+final_url[32:34]+";"+final_url[34:36]+";"+(final_url[36:38]+":"+final_url[38:40])+";"+tagScraper1[1].contents[0].replace('/10','')+";"+tagScraper2[2].contents[0].replace('votes','').replace(',','')])
            newFolder.close()
    except: 
        pass


# Part2

# In[ ]:


startTime='20070401'
finishTime='20080531'


# In[ ]:


url = 'http://web.archive.org/cdx/search/cdx?url='+film+'/&collapse=digest&from='+startTime+'&to='+finishTime+'&output=json'


# In[ ]:


urls = rq.get(url).text


# In[ ]:


parse_url = json.loads(urls)


# In[ ]:


url_list = []
for i in range(1,len(parse_url)):
    orig_url = parse_url[i][2]
    tstamp = parse_url[i][1]
    waylink = 'https://web.archive.org/web/'+tstamp+'/'+orig_url
    url_list.append(waylink)    


# In[ ]:


for i in range(len(url_list)):
    try:
        final_url=url_list[i]
        req = rq.get(final_url).text
        soup = bs(req,'html.parser')
        classScraper = soup.find(class_='general rating')
        tagScraper1 = classScraper.find_all('b')
        tagScraper2 = classScraper.find_all('a')
        print(final_url[28:42]+";"+tagScraper1[1].contents[0].replace('/10','')+";"+tagScraper2[0].contents[0].replace('votes','').replace(',',''))
        with open(filePath+"/"+filmId+".csv", mode='a', newline='') as newFolder:
            newWriter = csv.writer(newFolder, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
            newWriter.writerow([final_url[28:32]+";"+final_url[32:34]+";"+final_url[34:36]+";"+(final_url[36:38]+":"+final_url[38:40])+";"+tagScraper1[1].contents[0].replace('/10','')+";"+tagScraper2[0].contents[0].replace('votes','').replace(',','')])
            newFolder.close()
    except: 
        pass


# Part3

# In[ ]:


startTime='20080601'
finishTime='20091231'


# In[ ]:


url = 'http://web.archive.org/cdx/search/cdx?url='+film+'/&collapse=digest&from='+startTime+'&to='+finishTime+'&output=json'


# In[ ]:


urls = rq.get(url).text


# In[ ]:


parse_url = json.loads(urls)


# In[ ]:


url_list = []
for i in range(1,len(parse_url)):
    orig_url = parse_url[i][2]
    tstamp = parse_url[i][1]
    waylink = 'https://web.archive.org/web/'+tstamp+'/'+orig_url
    url_list.append(waylink)    


# In[ ]:


for i in range(len(url_list)):
    try:
        final_url=url_list[i]
        req = rq.get(final_url).text
        soup = bs(req,'html.parser')
        classScraper = soup.find(class_='meta')
        tagScraper1 = classScraper.find_all('b')
        tagScraper2 = classScraper.find_all('a')
        print(final_url[28:42]+";"+tagScraper1[0].contents[0].replace('/10','')+";"+tagScraper2[0].contents[0].replace('votes','').replace(',',''))
        with open(filePath+"/"+filmId+".csv", mode='a', newline='') as newFolder:
            newWriter = csv.writer(newFolder, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
            newWriter.writerow([final_url[28:32]+";"+final_url[32:34]+";"+final_url[34:36]+";"+(final_url[36:38]+":"+final_url[38:40])+";"+tagScraper1[0].contents[0].replace('/10','')+";"+tagScraper2[0].contents[0].replace('votes','').replace(',','')])
            newFolder.close()
    except: 
        pass


# Part4

# In[ ]:


startTime='20100101'
finishTime='20100930'


# In[ ]:


url = 'http://web.archive.org/cdx/search/cdx?url='+film+'/&collapse=digest&from='+startTime+'&to='+finishTime+'&output=json'


# In[ ]:


urls = rq.get(url).text


# In[ ]:


parse_url = json.loads(urls)


# In[ ]:


url_list = []
for i in range(1,len(parse_url)):
    orig_url = parse_url[i][2]
    tstamp = parse_url[i][1]
    waylink = 'https://web.archive.org/web/'+tstamp+'/'+orig_url
    url_list.append(waylink)    


# In[ ]:


for i in range(len(url_list)):
    try:
        final_url=url_list[i]
        req = rq.get(final_url).text
        soup = bs(req,'html.parser')
        classScraper = soup.find(class_='starbar-meta')
        tagScraper1 = classScraper.find_all('b')
        tagScraper2 = classScraper.find_all('a')
        print(final_url[28:42]+";"+tagScraper1[0].contents[0].replace('/10','')+";"+tagScraper2[0].contents[0].replace('votes','').replace(',',''))
        with open(filePath+"/"+filmId+".csv", mode='a', newline='') as newFolder:
            newWriter = csv.writer(newFolder, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
            newWriter.writerow([final_url[28:32]+";"+final_url[32:34]+";"+final_url[34:36]+";"+(final_url[36:38]+":"+final_url[38:40])+";"+tagScraper1[0].contents[0].replace('/10','')+";"+tagScraper2[0].contents[0].replace('votes','').replace(',','')])
            newFolder.close()
    except: 
        pass


# Part5

# In[ ]:


startTime='20101001'
finishTime='20110731'


# In[ ]:


url = 'http://web.archive.org/cdx/search/cdx?url='+film+'/&collapse=digest&from='+startTime+'&to='+finishTime+'&output=json'


# In[ ]:


urls = rq.get(url).text


# In[ ]:


parse_url = json.loads(urls)


# In[ ]:


url_list = []
for i in range(1,len(parse_url)):
    orig_url = parse_url[i][2]
    tstamp = parse_url[i][1]
    waylink = 'https://web.archive.org/web/'+tstamp+'/'+orig_url
    url_list.append(waylink)    


# In[ ]:


for i in range(len(url_list)):
    try:
        final_url=url_list[i]
        req = rq.get(final_url).text
        soup = bs(req,'html.parser')
        classScraper = soup.find(class_='star-box')
        tagScraper1 = classScraper.find_all('a')
        tagScraper2 = classScraper.find_all('span')
        print(final_url[28:42]+";"+tagScraper2[13].contents[0]+";"+tagScraper1[11].contents[0].replace(',','').replace('votes',''))
        with open(filePath+"/"+filmId+".csv", mode='a', newline='') as newFolder:
            newWriter = csv.writer(newFolder, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
            newWriter.writerow([final_url[28:32]+";"+final_url[32:34]+";"+final_url[34:36]+";"+(final_url[36:38]+":"+final_url[38:40])+";"+tagScraper2[13].contents[0]+";"+tagScraper1[11].contents[0].replace(',','').replace('votes','')])
            newFolder.close()
    except:
        pass
    


# Part6

# In[ ]:


startTime='20110801'
finishTime='20151213'


# In[ ]:


url = 'http://web.archive.org/cdx/search/cdx?url='+film+'/&collapse=digest&from='+startTime+'&to='+finishTime+'&output=json'


# In[ ]:


urls = rq.get(url).text


# In[ ]:


parse_url = json.loads(urls)


# In[ ]:


url_list = []
for i in range(1,len(parse_url)):
    orig_url = parse_url[i][2]
    tstamp = parse_url[i][1]
    waylink = 'https://web.archive.org/web/'+tstamp+'/'+orig_url
    url_list.append(waylink)    


# In[ ]:


for i in range(len(url_list)):
    try:
        final_url=url_list[i]
        req = rq.get(final_url).text
        soup = bs(req,'html.parser')
        classScraper = soup.find(class_='star-box-details')
        tagScraper1 = classScraper.find_all('span')
        print(final_url[28:42]+";"+tagScraper1[0].contents[0]+";"+tagScraper1[3].contents[0].replace(',',''))
        with open(filePath+"/"+filmId+".csv", mode='a', newline='') as newFolder:
            newWriter = csv.writer(newFolder, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
            newWriter.writerow([final_url[28:32]+";"+final_url[32:34]+";"+final_url[34:36]+";"+(final_url[36:38]+":"+final_url[38:40])+";"+tagScraper1[0].contents[0]+";"+tagScraper1[3].contents[0].replace(',','')])
            newFolder.close()
    except:
        pass


# Part7

# In[ ]:


startTime='20151214'
finishTime='20160106'


# In[ ]:


url = 'http://web.archive.org/cdx/search/cdx?url='+film+'/&collapse=digest&from='+startTime+'&to='+finishTime+'&output=json'


# In[ ]:


urls = rq.get(url).text


# In[ ]:


parse_url = json.loads(urls)


# In[ ]:


url_list = []
for i in range(1,len(parse_url)):
    orig_url = parse_url[i][2]
    tstamp = parse_url[i][1]
    waylink = 'https://web.archive.org/web/'+tstamp+'/'+orig_url
    url_list.append(waylink)    


# In[ ]:


for i in range(len(url_list)):
    try:
        final_url=url_list[i]
        req = rq.get(final_url).text
        soup = bs(req,'html.parser')
        classScraper = soup.find(class_='imdbRating')
        tagScraper1 = classScraper.find_all('span')
        print(final_url[28:42]+";"+tagScraper1[0].contents[0]+";"+tagScraper1[3].contents[0].replace(',',''))
        with open(filePath+"/"+filmId+".csv", mode='a', newline='') as newFolder:
            newWriter = csv.writer(newFolder, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
            newWriter.writerow([final_url[28:32]+";"+final_url[32:34]+";"+final_url[34:36]+";"+(final_url[36:38]+":"+final_url[38:40])+";"+tagScraper1[0].contents[0]+";"+tagScraper1[3].contents[0].replace(',','')])
            newFolder.close()
    except:
        pass


# Part8

# In[ ]:


startTime='20160107'
finishTime='20160126'


# In[ ]:


url = 'http://web.archive.org/cdx/search/cdx?url='+film+'/&collapse=digest&from='+startTime+'&to='+finishTime+'&output=json'


# In[ ]:


urls = rq.get(url).text


# In[ ]:


parse_url = json.loads(urls)


# In[ ]:


url_list = []
for i in range(1,len(parse_url)):
    orig_url = parse_url[i][2]
    tstamp = parse_url[i][1]
    waylink = 'https://web.archive.org/web/'+tstamp+'/'+orig_url
    url_list.append(waylink)    


# In[ ]:


for i in range(len(url_list)):
    try:
        final_url=url_list[i]
        req = rq.get(final_url).text
        soup = bs(req,'html.parser')
        classScraper = soup.find(class_='star-box-details')
        tagScraper1 = classScraper.find_all('span')
        print(final_url[28:42]+";"+tagScraper1[0].contents[0]+";"+tagScraper1[3].contents[0].replace(',',''))
        with open(filePath+"/"+filmId+".csv", mode='a', newline='') as newFolder:
            newWriter = csv.writer(newFolder, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
            newWriter.writerow([final_url[28:32]+";"+final_url[32:34]+";"+final_url[34:36]+";"+(final_url[36:38]+":"+final_url[38:40])+";"+tagScraper1[0].contents[0]+";"+tagScraper1[3].contents[0].replace(',','')])
            newFolder.close()
    except:
        pass


# Part9

# In[ ]:


startTime='20160127'
finishTime='2022'


# In[ ]:


url = 'http://web.archive.org/cdx/search/cdx?url='+film+'/&collapse=digest&from='+startTime+'&to='+finishTime+'&output=json'


# In[ ]:


urls = rq.get(url).text


# In[ ]:


parse_url = json.loads(urls)


# In[ ]:


url_list = []
for i in range(1,len(parse_url)):
    orig_url = parse_url[i][2]
    tstamp = parse_url[i][1]
    waylink = 'https://web.archive.org/web/'+tstamp+'/'+orig_url
    url_list.append(waylink)    


# In[ ]:


for i in range(len(url_list)):
    try:
        final_url=url_list[i]
        req = rq.get(final_url).text
        soup = bs(req,'html.parser')
        classScraper = soup.find(class_='imdbRating')
        tagScraper1 = classScraper.find_all('span')
        print(final_url[28:42]+";"+tagScraper1[0].contents[0]+";"+tagScraper1[3].contents[0].replace(',',''))
        with open(filePath+"/"+filmId+".csv", mode='a', newline='') as newFolder:
            newWriter = csv.writer(newFolder, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
            newWriter.writerow([final_url[28:32]+";"+final_url[32:34]+";"+final_url[34:36]+";"+(final_url[36:38]+":"+final_url[38:40])+";"+tagScraper1[0].contents[0]+";"+tagScraper1[3].contents[0].replace(',','')])
            newFolder.close()
    except:
        pass

