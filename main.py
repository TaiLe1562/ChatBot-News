import json
import time
import flask
from flask import request, jsonify
import telegram
import requests
from bs4 import BeautifulSoup
from threading import Thread
import threading
import time
from flask import render_template

from flask_cors import CORS, cross_origin
CHATID = ["2125746685"]

# 1 Tin tức
def get_news():
    list_news = []
    r = requests.get("https://vnexpress.net/")
    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs = soup.find_all("h3", {"class": "title-news"})

    for new in mydivs:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_news.append(newdict)

    return list_news


# 2 Chinh tri
def get_chinhtri():
    list_chinhtri = []
    r = requests.get("https://vnexpress.net/thoi-su/chinh-tri")
    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs = soup.find_all("h3", {"class": "title-news"})

    for new in mydivs:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_chinhtri.append(newdict)

    return list_chinhtri


# 3 Thế giới
def get_thegioi():
    list_thegioi = []
    r = requests.get("https://vnexpress.net/the-gioi/")
    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs = soup.find_all("h3", {"class": "title-news"})

    for new in mydivs:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_thegioi.append(newdict)

    return list_thegioi


# 4 Kinh doanh
def get_kinhdoanh():
    list_kinhdoanh = []
    r = requests.get("https://vnexpress.net/kinh-doanh/")
    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs = soup.find_all("h3", {"class": "title-news"})

    for new in mydivs:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_kinhdoanh.append(newdict)

    return list_kinhdoanh


# 5 Khoa học
def get_khoahoc():
    list_khoahoc = []
    r = requests.get("https://vnexpress.net/khoa-hoc")
    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs = soup.find_all("h3", {"class": "title-news"})

    for new in mydivs:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_khoahoc.append(newdict)

    return list_khoahoc


# 6 Giai trí
def get_giaitri():
    list_giaitri = []
    r = requests.get("https://vnexpress.net/giai-tri")
    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs = soup.find_all("h3", {"class": "title-news"})

    for new in mydivs:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_giaitri.append(newdict)

    return list_giaitri


# 7 The thao
def get_thethao():
    list_thethao = []
    r = requests.get("https://vnexpress.net/the-thao/")
    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs = soup.find_all("h3", {"class": "title-news"})

    for new in mydivs:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_thethao.append(newdict)

    return list_thethao


# 8 Phap luat
def get_phapluat():
    list_phapluat = []
    r = requests.get("https://vnexpress.net/phap-luat/")
    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs = soup.find_all("h3", {"class": "title-news"})

    for new in mydivs:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_phapluat.append(newdict)

    return list_phapluat


# 9 Giao dục
def get_giaoduc():
    list_giaoduc = []
    r = requests.get("https://vnexpress.net/giao-duc/")
    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs = soup.find_all("h3", {"class": "title-news"})

    for new in mydivs:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_giaoduc.append(newdict)

    return list_giaoduc


# 10 Sức khỏe
def get_suckhoe():
    list_suckhoe = []
    r = requests.get("https://vnexpress.net/suc-khoe/")
    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs = soup.find_all("h3", {"class": "title-news"})

    for new in mydivs:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_suckhoe.append(newdict)

    return list_suckhoe


# 11 Du lich
def get_dulich():
    list_dulich = []
    r = requests.get("https://vnexpress.net/du-lich/")
    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs = soup.find_all("h3", {"class": "title-news"})

    for new in mydivs:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_dulich.append(newdict)

    return list_dulich


# 12 So hoa
def get_sohoa():
    list_sohoa = []
    r = requests.get("https://vnexpress.net/so-hoa/")
    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs = soup.find_all("h3", {"class": "title-news"})

    for new in mydivs:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_sohoa.append(newdict)

    return list_sohoa


# 13 Xe
def get_xe():
    list_xe = []
    r = requests.get("https://vnexpress.net/oto-xe-may/")
    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs = soup.find_all("h3", {"class": "title-news"})

    for new in mydivs:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_xe.append(newdict)

    return list_xe


# 14 Thoi sự
def get_thoisu():
    list_thoisu = []
    r = requests.get("https://vnexpress.net/thoi-su/")
    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs = soup.find_all("h3", {"class": "title-news"})

    for new in mydivs:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_thoisu.append(newdict)

    return list_thoisu


def News():
    return get_news()


def send_message(bot,title,data):
    for chatId in CHATID:
        bot.send_message(chat_id =chatId, text=title)
        for item in data:
            bot.send_message(chat_id =chatId, text=f'{item["link"]}')
            time.sleep(2)

TOKEN = "2144954679:AAFcnWDgg9hn9VHbE-IKogjg3Ecm2qmrze4"
app = flask.Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


BOT = telegram.Bot(token=TOKEN)
@app.route('/test', methods=['GET'])
@cross_origin()
def home():
    data = News()
    return data
@app.route('/myfilm', methods=['POST'])
def api_all():
    global BOT
    data = []
    title = ""
    news_type = request.form["news_type"]
    if news_type == None:
        news_type = "news"

    if news_type == "news":
        data = News()
        title = "tin tức"

    if news_type == "thethao":
        data = get_thethao()
        title = "thể thao"


    if news_type == "xe":
        data = get_xe()
        title = "xe"


    if news_type == "giaitri":
        data = get_giaitri()
        title = "giaitri"


    t1 = threading.Thread(target=send_message, args=(BOT,title,data,))
    t1.start()
    return jsonify(data)
# STARTadss
@app.route('/')
def defmain():
    return render_template('index.html')

app.run(host='0.0.0.0', port=7699)


