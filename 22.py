from bs4 import BeautifulSoup

file = open('for_parsing.html', 'r', encoding='utf-8')
data = file.read()
file.close()

soup = BeautifulSoup(data, 'lxml')

values = soup.findAll('a')

for value in values:
    name = value.text
    print(name)