from bs4 import BeautifulSoup
import requests
import time

def parse(html_data):
    soup = BeautifulSoup(html_data, 'lxml')
    
    values = soup.findAll('div', attrs={'itemprop': 'review'})
    
    for value in values:
        author_tag = value.find('meta', attrs={'itemprop': 'author'})
        print(author_tag['content'])
        
        reviewRating_tag = value.find('div', attrs={'itemprop': 'reviewRating'})
        print(reviewRating_tag.meta['content'])    
        
        description_tag = value.find('meta', attrs={'itemprop': 'description'})
        print(description_tag['content'])   
        
        datePublished_tag = value.find('meta', attrs={'itemprop': 'datePublished'})
        print(datePublished_tag['content']) 

#file = open('iPhone.html', 'r', encoding='utf-8')
#data = file.read()
#file.close()

def get_next_page_url(html_data):
    soup = BeautifulSoup(html_data, 'lxml')
    tag = soup.find('a', attrs={'aria-label': 'Следующая страница'})
    
    if tag is None:
        return None
    else: 'https://market.yandex.by' + tag['href']
        

headers = {
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
   'Accept-Language' : 'en-US,en;q=0.9,ru;q=0.8,de;q=0.7',
   'Connection' : 'keep-alive',
   'Host' : 'market.yandex.by',
   'Sec-Fetch-Dest' : 'document',
   'Sec-Fetch-Mode' : 'navigate',
   'Sec-Fetch-Site' : 'same-origin',
   'Sec-Fetch-User' : '?1',
   'Upgrade-Insecure-Requests' : '1',
   'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
}    

url = 'https://market.yandex.by/product--smartfon-apple-iphone-12-128gb/722974019/reviews?lr=0&track=tabs'

while True:
   response = requests.get(url, headers = headers)
   response.encoding = 'utf-8'
   data = response.text
   parse(data)
   
   time.sleep(10)
   
   url = get_next_page_url(data)
   
   if url is None:
       break