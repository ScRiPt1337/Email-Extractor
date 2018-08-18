#!/usr/bin/python
from bs4 import BeautifulSoup
import requests
import requests.exceptions
import urllib2
from fake_useragent import UserAgent
from Tkinter import *
import ttk
import threading


def download(url):
    response = urllib2.urlopen(url)
    webContent = response.read()
    f = open('hel.html', 'w')
    f.write(webContent)
    f.close
    f1 = open('hel.html', 'r')
    f2 = open('hell.html', 'w')
    for line in f1:
        f2.write(line.replace('&#064;', '@'))
    f1.close()
    f2.close()
    with open('hell.html', 'r') as f_input:
        hell = re.findall(r'\b([a-z0-9-_.]+?@[a-z0-9-_.]+)\b', f_input.read(), re.I)
        gol = str(hell)
        f = open('email.txt', 'a')
        f.write(gol)
        f.close
        s = open("email.txt").read()
        s = s.replace('\'', '\n')
        s = s.replace(']', '')
        s = s.replace('[', '')
        s = s.replace(',', '\n')
        s = s.replace('\n\n', '')
        s = s.replace(' ', '')
        f = open("email.txt", 'w')
        f.write(s)
        f.close()


def trade_spider(max_pages, url):
    page = 1
    ua = UserAgent()
    header = {'User-Agent': str(ua.chrome)}
    print(header)
    while page <= max_pages:
        download(url)
        source_code = requests.get(url, allow_redirects=False, headers=header)
        plain_text = source_code.text.encode('ascii', 'replace')
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.find_all("a"):
            href = str(link.get('href'))
            print(href)
            try:
                download(href)
                get_single_item_data(href)
            except:
                pass

        page += 1


def get_single_item_data(item_url):
    ua = UserAgent()
    header = {'User-Agent': str(ua.chrome)}
    print(header)
    try:
        download(item_url)
        source_code = requests.get(item_url, headers=header)
        plain_text = source_code.text.encode('ascii', 'replace')
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.findAll("a"):
            href = link.get('href')
            print (href)
            try:
                download(href)
                single_item_data(href)
            except:
                pass
    except:
       pass

def single_item_data(item_url):
    ua = UserAgent()
    header = {'User-Agent': str(ua.chrome)}
    print(header)
    try:
        download(item_url)
        source_code = requests.get(item_url, headers=header)
        plain_text = source_code.text.encode('ascii', 'replace')
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.findAll("a"):
            href = link.get('href')
            print (href)
            try:
                download(href)
            except:
                pass
    except:
       pass
def show_entry_fields():
    attck = e1.get()
    thread = threading.Thread(target=trade_spider, args=(1, attck))
    thread.daemon = True  # Daemonize thread
    thread.start()
class progress():
    def __init__(self, parent):
            self.progressbar = ttk.Progressbar(master, orient=HORIZONTAL,length=200,mode="determinate",takefocus=True,maximum=100)
            self.progressbar.grid()
            self.t = threading.Thread()
            self.t.__init__(target = self.progressbar.start, args = ())
            self.t.start()
master = Tk()
master.geometry('400x200')
C = Canvas(master, bg="blue", height=250, width=300)
filename = PhotoImage(file = "sheth-dragon-logo.png")
background_label = Label(master, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
Label(master, text="Website url: ").grid(row=0, sticky=E)
master.title("endless email extrator")
e1 = Entry(master)
e1.grid(row=0, column=1)
Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Start', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
status = Label(master, text="Coded by LuciF3R", bd=1, relief=SUNKEN, anchor=W)
status.grid(row=2, columnspan=1)
new = progress(master)
mainloop( )


