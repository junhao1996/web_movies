import re
import random
import threading
import time

import requests
from sqlalchemy.orm import sessionmaker



from web_movie.model import Img
from web_movie.model.base import engine


def get_picture(data):
    url = "http://616pic.com/category?md=1&p="+str(data)
    Session = sessionmaker(bind=engine)
    ses = Session()

    r1 = requests.get(url)
    a = re.compile(r'data-original="(.*?)"', re.M)
    result = re.findall(a, r1.text)
    for url in result:
        local_name = url.split("/")[-1]
        print(local_name)
        img = Img(imgname = local_name)
        ses.add(img)
        ses.commit
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
        with open("/home/zhang/work/github/pacongdemo/web_movies/web_movie/static/img/"+local_name, "wb") as f:

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

def pachong():
    url = ""
    res = requests.get(url, stream=True)
    # 用流的方式来写入图片
    with open("1.jpg", "wb") as f:
        for i in res.iter_content(chunk_size=1024):
            f.write(i)


def work_do_sth(data, info):

    for i in data:
        get_picture(i)


if __name__ == "__main__":
    # a = get_picture()
    # set(a)

    a = time.time()
    data = [1, 2, 3]
    info = {
        'worker': 'pachong.work_do_sth',
        'chunk_size': 2
    }
    ww = Worker(mode="thread")
    resp = ww.work(data, info)


    # 直接爬取
    # for i in data:
    #     get_picture(i)

    # for i in list(range(1,7)):
    #     th1 = threading.Thread(target=get_picture, args=(i,))
    #     th1.start()



    # th1 = threading.Thread(target=get_picture, args=(1,))
    #
    # th1.start()
    # th2 = threading.Thread(target=get_picture, args=(2,))
    # th2.start()
    # th1.join()
    # th2.join()
    b = time.time()
    print(b-a)
    # 普通使用 29s
    # 使用多线程14s
