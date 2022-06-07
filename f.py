

import requests

# print(dir(requests))

from bs4 import BeautifulSoup as bs

# print(dir(bs))

ua = {'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

r =requests.get('https://timesprayer.com/prayer-times-cities-egypt.html', headers = ua)

soup = bs(r.content,'html.parser')

print(soup.find(class_='col6 prayertable mobile').find_all('tr')[1].text)
print(soup.find(class_='col6 prayertable mobile').find_all('tr')[2].text)
print(soup.find(class_='col6 prayertable mobile').find_all('tr')[3].text)
print(soup.find(class_='col6 prayertable mobile').find_all('tr')[4].text)
print(soup.find(class_='col6 prayertable mobile').find_all('tr')[5].text)
print(soup.find(class_='col6 prayertable mobile').find_all('tr')[6].text)





# ==============
# https://timesprayer.com/prayer-times-cities-egypt.html
# https://timesprayer.com/prayer-times-in-port-said.html
# https://timesprayer.com/prayer-times-in-damietta.html
# https://timesprayer.com/prayer-times-in-marsa-matruh.html