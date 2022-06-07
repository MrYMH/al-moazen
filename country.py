from pywebio import start_server

# print(dir(start_server))

from pywebio.input import *

from pywebio.output import *

from pywebio.session import *

import requests

# print(dir(requests))

from bs4 import BeautifulSoup as bs

def salat():

    ua = {'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

    r =requests.get('https://timesprayer.com/prayer-times-in-port-said.html', headers = ua)

    soup = bs(r.content,'html.parser')

    put_text('مواقيت الصلاة فى مصر')

    put_image('https://gate.ahram.org.eg/Media/News/2021/11/8/19_2021-637719837258183109-818.jpg')

    put_html('<hr>')

    # input('choose your country')

    # country = input('choose your country').strip().lower()
    

    put_table([
        ["الصلاة" ,"التوقيت"],
        [put_text('الفجر') , put_text(soup.find(class_='info prayertable mobile').find_all('li')[0].text)],
        [put_text("الشروق") , put_text(soup.find(class_='info prayertable mobile').find_all('li')[1].text)],
        [put_text("الظهر") , put_text(soup.find(class_='info prayertable mobile').find_all('li')[2].text)],
        [put_text("العصر") , put_text(soup.find(class_='info prayertable mobile').find_all('li')[3].text)],
        [put_text("المغرب") , put_text(soup.find(class_='info prayertable mobile').find_all('li')[4].text)],
        [put_text("العشاء") , put_text(soup.find(class_='info prayertable mobile').find_all('li')[5].text)],
        
    ])
    # put_text(country)
    # print(f'you choosed {country}')

start_server(salat , port= 5777 , debug=True)