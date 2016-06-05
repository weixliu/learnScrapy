#coding:utf-8
import scrapy
from tutorial.items import TutorialItem
import re
class FirstSpider(scrapy.Spider):
    name = "dytt"
    allowed_domains = ["dytt8.net", "ygdy8.net"]
    start_urls = [
        "http://www.ygdy8.net/",
        "http://www.dytt8.net/"
    ]
    
    def parse(self, response):
         urlMatch = re.match(r"http://www\.(dytt8|ygdy8)\.net(/\w{0,10}){0,10}/(\d){0,10}/(\d){0,10}\.\w{0,10}", response.url)
         if urlMatch != None:
             item = TutorialItem()
             self.loadItem(item, response)
             yield item
         else:
             next_pages = response.css("a::attr('href')").extract()
             for next_page in next_pages:
                 url = response.urljoin(next_page)
                 yield scrapy.Request(url, self.parse)

    def loadItem(self, item, response):
        content = response.body_as_unicode().encode('utf-8', 'ignore')
        movieName = re.findall(r'<div class="title_all"><h1><font color=#07519a>(.*?)</font></h1></div>', content, re.S)
        if (len(movieName) > 0):
            movieName = movieName[0] + ""
            movieName = movieName[movieName.find("《") + 3:movieName.find("》")]
        else:
            movieName = ""

        print(u"电影名称: " + movieName.decode('utf-8').strip())

        movieContent = re.findall(r'<div class="co_content8">(.*?)</tbody>',content , re.S)

        pattern = re.compile('<ul>(.*?)<tr>', re.S)
        movieDate = re.findall(pattern,movieContent[0])

        if len(movieDate) > 0:
            movieDate = movieDate[0].strip() + ''
        else:
            movieDate = ""

        print(u"电影发布时间: " + movieDate.decode('utf-8')[-10:])

        pattern = re.compile('<br /><br />(.*?)<br /><br /><img')
        movieInfo = re.findall(pattern, movieContent[0])

        if len(movieInfo) > 0:
            movieInfo = movieInfo[0]+''
            movieInfo = movieInfo.replace("<br />","")
            movieInfo = movieInfo.split('◎')
        else:
            movieInfo = ""

        print(u"电影基础信息: ")
        for item in movieInfo:
            print(item.decode('utf-8'))

        pattern = re.compile('<img.*? src="(.*?)".*? />', re.S)  
        movieImg = re.findall(pattern,movieContent[0])

        if (len(movieImg) > 0):
            movieImg = movieImg[0]
        else:
            movieImg = ""

        print(u"电影海报: " + movieImg.decode('utf-8'))

        pattern = re.compile('<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(.*?)">.*?</a></td>', re.S)
        movieDownUrl = re.findall(pattern,movieContent[0])

        if (len(movieDownUrl) > 0):
            movieDownUrl = ('@_@'.join(movieDownUrl))
        else:
            movieDownUrl = ""

        print(u"电影下载地址：" + movieDownUrl.decode('utf-8') + "")
        print("------------------------------------------------\n\n\n")
