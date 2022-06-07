import requests

from bs4 import BeautifulSoup as bs

from tkinter import *

from tkinter import ttk

# print(dir(ttk))

root = Tk()

root.geometry('420x550')

root.title('مواقيت الصلاة')

root.configure(background='white')



def get():

    ua = {'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

    r =requests.get('https://timesprayer.com/prayer-times-cities-egypt.html', headers = ua)

    soup = bs(r.content,'html.parser')

    a1=soup.find(class_='col6 prayertable mobile').find_all('td')[1].text
    a2=soup.find(class_='col6 prayertable mobile').find_all('td')[3].text
    a3=soup.find(class_='col6 prayertable mobile').find_all('td')[5].text
    a4=soup.find(class_='col6 prayertable mobile').find_all('td')[7].text
    a5=soup.find(class_='col6 prayertable mobile').find_all('td')[9].text
    a6=soup.find(class_='col6 prayertable mobile').find_all('td')[11].text

    tv.insert(parent='', index=0, id=0 , text='', values=('الفجر', a1))
    # tv.insert(parent='', index=1, id=1 , text='', values=('الشروق', a2))
    tv.insert(parent='', index=2, id=2 , text='', values=('الظهر', a3))
    tv.insert(parent='', index=3, id=3 , text='', values=('العصر', a4))
    tv.insert(parent='', index=4, id=4 , text='', values=('المغرب', a5))
    tv.insert(parent='', index=5, id=5 , text='', values=('العشاء', a6))



# ======== logo ======================

logo = PhotoImage(file='app-image-6074bc8ea765a.jpg')

lab_logo = Label(root,image=logo)

lab_logo.place(x=70, y=5)

# ================== treeveiw ====================

style = ttk.Style()

style.configure('mystyle.Treeview',font=('calibri',13),rowheight=40)

tv= ttk.Treeview(root,style='mystyle.Treeview')

tv['columns']=('Name', 'Time')

tv.column('#0',width=0, stretch =NO)

tv.column('Name' , anchor=CENTER, width=80)

tv.column('Time' , anchor=CENTER, width=80)

tv.heading('#0', text='', anchor=CENTER)

tv.heading('Name', text='الصلاة', anchor=CENTER)

tv.heading('Time', text='التوقيت', anchor=CENTER)

tv.place(x=10 , y=230 , width =300, height=250)

b = Button(root , text='اظهار مواقيت الصلاة', bg='white', fg='black', bd=1, relief=SOLID , command=get)

b.place(x=100, y=500)




root.mainloop()




