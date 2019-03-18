# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import scrapy
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from getChuxiao.resource import rescource
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
import random
import sys
# sys.path.append('../')


class heiSpiderMiddleware(object):
    def process_request(self, request, spider):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        if request.url == 'https://www.xiaoheihe.cn/games/index':
            try:
                self.page = input('输入你要爬取的第N页：')
            except EOFError:
                sys.exit()# exit the program
            self.driver.get(request.url)
            self.driver.implicitly_wait(5)
            btn = self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div/div[1]/h2/span/i') #“更多”按钮
            ActionChains(self.driver).click(btn).perform()      #使用perform()才能执行action
            time.sleep(2)
            btn2 = self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[6]/div[2]/div/div/div[2]/div/input') #翻页文本框
            btn2.clear()                #清空文本框
            time.sleep(1)
            btn2.send_keys(self.page)   #填写文本框
            time.sleep(1)
            btn2.send_keys(Keys.ENTER)  #回车
            time.sleep(2)
            html = self.driver.page_source
            # with open('test.txt','a',encoding='utf-8') as fp:
            #     fp.write(html)
            # print(html)
            self.driver.quit()
            return scrapy.http.HtmlResponse(url=request.url, body=html, encoding='utf-8',
                                            request=request)

class CustomUserAgentMiddleware(UserAgentMiddleware):
    def __init__(self,user_agent='Scrapy'):
        ua = random.choice(rescource.UserAgents)
        # print(ua)
        self.user_agent = ua



class GetchuxiaoSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class GetchuxiaoDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
