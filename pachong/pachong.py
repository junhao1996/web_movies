import re
import time

from urllib import request
from lxml import etree
import requests
from sqlalchemy.orm import sessionmaker
from worker.worker import Worker
from bs4 import BeautifulSoup

from web_movie.model import Img, Movie
from web_movie.model.base import engine


def get_picture(data):
    url = "http://616pic.com/category?md=1&p=" + str(data)
    Session = sessionmaker(bind=engine)
    ses = Session()

    r1 = requests.get(url)
    a = re.compile(r'data-original="(.*?)"', re.M)
    result = re.findall(a, r1.text)
    for url in result:
        local_name = url.split("/")[-1]
        print(local_name)
        img = Img(imgname=local_name)
        ses.add(img)
        print("111")
        ses.commit()
        #
        # # 用流的方式实现
        # res = requests.get(url, stream=True)
        # # 用流的方式来写入图片
        # with open("/home/zhang/图片/"+local_name, "wb") as f:
        #     for i in res.iter_content(chunk_size=1024):
        #         f.write(i)

        res = requests.get(url)
        # print(type(res))
        # print(res.content)
        with open("/home/zhang/work/github/pacongdemo/web_movies/web_movie/static/img/" + local_name, "wb") as f:

            for i in res:
                f.write(i)

    # print(res.text)
    print(result)
    # print(type(res.content))
    # data - objurl = "http://imgsrc.baidu.com/imgad/pic/item/10dfa9ec8a136327701bf8109b8fa0ec08fac71a.jpg"
    return result


def find():
    str_search = input("请输入查找的类型：")
    word = str_search
    url = 'http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=' + word
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}
    res = requests.get(url, headers=headers)
    a = re.findall('"objURL":"(.*?)"', res.text, re.S)
    print(a)
    for i, j in enumerate(a):
        with open("/home/zhang/图片/" + str(i) + '.jpg', 'wb') as f:
            if j.startswith("http"):
                res = requests.get(j)
                f.write(res.content)
                print("正在下载。。。" + str(i) + "/" + str(len(a) - 1))


def get_movie(movie_id):
    uu = "https://www.80s.tw/movie/" + str(movie_id)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}
    res = requests.get(uu, headers=headers)
    # request得到数据

    # print(res.text)
    # url = urlopen('https://www.80s.tw/movie/22618').read()

    # url = request.urlopen('https://www.80s.tw/movie/22938').read()
    # print(url)
    # # res = requests.get(url).text
    # # r = url.content
    # a = etree.HTML(url)
    # # 二进制转utf-8
    # b = etree.tostring(a, encoding="utf-8", pretty_print=True, method="html")
    # s = b.decode("utf-8")

    # with open("/home/zhang/图片/"+"1.txt","w") as f:
    #     f.write(res.text)

    # html_data = a.xpath('//img/@src')
    # for i in html_data:
    #     print(i)
    # data2 = a.xpath("//span/text()")

    soup = BeautifulSoup(res.text, "lxml")
    # soup = BeautifulSoup(open('/home/zhang/图片/1.txt'))
    # 打开文件

    s1 = soup.select(".info")[0].get_text()
    print(s1)
    s2 = soup.find_all("h1", class_="info")
    print(s2)
    s2 = soup.find("div", class_='info').h1.get_text()
    # s3 = soup.find_all('a')
    s4 = soup.find("div", class_='info').a.text
    s5 = soup.find("div", class_='info').text
    print(type(s5))
    # 剧情content   t1
    t1 = soup.select("#movie_content")[0].get_text()
    print(t1)
    print("**********")
    t2 = soup.select('span[class:"font_888"]')
    # t3 = soup.select("a[href='/actor/528']")
    # print(t3[0].get_text(), 111111)

    # for i in t2:
    #     print(i.text)
    print("t2")
    # 演员actor   t4
    t4 = soup.select("#minfo .info a")
    for i in t4[0:5]:
        print(i.get_text())
    # 演员actor   t4

    for i in t4:
        print(i.get_text())
    actor = ""
    for i in t4[0:5]:
        print(i.get_text())
        actor = actor + " " + i.get_text()
    # language
    language = t4[9].get_text()
    print(language)
    print(t4[7].get_text())

    t5 = soup.select("#minfo .info span")
    # print(t5)
    for i in t5:
        print(i.text)
        print("**********8")
    #     time
    time1 = t5[16].text.split(' ')[1]
    print(time1)
    # logintime
    logintime = t5[14].text.split(r'：')[1]
    print(logintime)
    # 图片地址
    t6 = soup.select(".img img")
    url = str(t6[0]).split('"')[3]
    img_url = "http:" + url
    pachong(img_url)

    # print(s5)
    # print(s2)
    # print(s4)
    # for i in t5:
    #     print(i.text)
    #     print("**********8")

    movie_type = t5[6].text.split(' ')[0].split("：")[1]
    # print(time1)

    Session = sessionmaker(bind=engine)
    sss = Session()
    # sss.add(Movie(title=s2, content=t1, actor=actor, logintime=logintime, movie_type=movie_type, time=time1))
    # sss.commit()


def pachong(img_url):
    url = img_url[-10:]
    print(123456789)
    print(url)
    res = requests.get(img_url, stream=True)

    Session = sessionmaker(bind=engine)
    ses = Session()
    ses.add(Img(imgname=url))
    ses.commit()
    # res = requests.get(img_url, stream=True)
    # 用流的方式来写入图片
    with open("/home/zhang/图片/" + str(url), 'wb') as f:
        for i in res.iter_content(chunk_size=1024):
            f.write(i)


def work_do_sth(data, info):
    for i in data:
        get_picture(i)

        # print(a)


if __name__ == "__main__":
    # a = get_picture()
    # set(a)
    for i in range(50):
        a = i + 22650
        get_movie(a)

    # a = time.time()
    # data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # info = {
    #     'worker': 'pachong.work_do_sth',
    #     'chunk_size': 2
    # }
    # ww = Worker(mode="thread")
    # resp = ww.work(data, info)
