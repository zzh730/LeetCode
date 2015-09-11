__author__ = 'drzzh'
# !/usr/bin/env python
import urllib.request
import re
import time
import os


# Get the html page
# @ param url2, url link
# @ return string with web content
def getHtml2(url2):
    html2 = urllib.request.urlopen(url2).read().decode('utf-8')
    return html2


# Get the link that contains picture
# @ param html2, a string contains all the web page content
# @ return url link
def gettopic(html2):
    reg2 = r'http://www.douban.com/group/topic/\d+'
    topiclist = re.findall(reg2, html2)
    # only use one link to capture picture
    return topiclist[-1]


# Download the picture
# @ param topic_page, a sting of a web
# return image
def download(topic_page):
    reg3 = r'http://img6.douban.com/view/group_topic/large/public/.+\.jpg'
    imglist = re.findall(reg3, topic_page)
    i = 1
    for imgurl in imglist:
        # take picture's ID as file name
        img_numlist = re.findall(r'p\d{7}', imgurl)
        for img_num in img_numlist:
            address = os.path.expanduser('~/Documents/Python/douban/') + str(img_num) + '.jpg'
            urllib.request.urlretrieve(imgurl, address)
            time.sleep(1)
            i += 1
            print(imgurl)


# main function
def main():
    if not os.path.isdir(os.path.expanduser('~/Documents/Python/douban')):
        os.makedirs(os.path.expanduser('~/Documents/Python/douban'))
    page_end = int(input('Please enter a page to end：'))
    num_end = page_end * 25
    num = 0
    page_num = 1
    while num <= num_end:
        html2 = getHtml2('http://www.douban.com/group/godgoddess/discussion?start=%d' % num)
        topicurl = gettopic(html2)
        topic_page = getHtml2(topicurl)
        download(topic_page)
        num = page_num * 25
        page_num += 1

    else:
        print('Picture downloaded！')


if __name__ == '__main__':
    main()
