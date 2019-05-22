import time
import sys

if sys.version_info[0] == 2:
    import ConfigParser as configparser
else:
    import configparser
from SeleniumHelper import SeleniumHelper
from selenium import webdriver
import re
import urllib.parse as parse
import json
from scrapper.Mapper import *


class LinkedinController(SeleniumHelper):
    TIMEOUT = 7
    data = {}

    def __init__(self, config=None, debug=False):
        self.mapper = Mapper()
        if debug:
            self.driver = webdriver.Chrome('c:/chromedriver.exe')
        else:
            self.driver = webdriver.PhantomJS()
            self.driver.set_page_load_timeout(self.TIMEOUT)
        if config:
            self.mode = 'LOGGED'
            # self.login(config)

    def login(self):
        self.loadPage("https://www.linkedin.com/login")
        self.waitAndWrite("#username", "karescrapper@gmail.com")
        self.submitForm(self.selectAndWrite("#password", "Kare14531453"))

    def performClicks(self):
        self.clickSelector('#contact-info-tab')
        self.clickMultiple('.hidden-view-more')
        self.clickMultiple('.toggle-show-more')
        self.clickMultiple('.see-action')
        self.clickMultiple('.see-more-less')
        if self.mode == 'LOGGED':
            self.clickMultiple('.see-more')
        else:
            self.clickMultiple('li.see-more label')
            self.clickMultiple('.recommendation label')
        time.sleep(0.3)

    def extractProfile(self, url):
        print('extract file')
        self.loadAndWait(url, self.CONTAINER[self.mode])
        self.performClicks()
        self.data = self.extractSection(self.mode)
        self.data['friendlyUrl'] = self.driver.current_url
        self.data['connId'] = self.get_conn_id()
        return self.data

    def search(self, keyword):
        result = {}
        i = 1
        while i < 100:
            self.loadPage(
                'https://www.linkedin.com/search/results/all/?keywords=' + keyword + '&origin=GLOBAL_SEARCH_HEADER&page=' + str(i))
            html = self.driver.page_source
            self.performClicks()
            find = re.findall("<code style=\"display: none\" id=\"bpr-guid-(.*?)\">([\s\S]*?)</code>", html)
            for data in find:
                filter = json.loads(parse.unquote(self.html_escape(data[1])))
                if filter['data']['$type'] == 'com.linkedin.restli.common.CollectionResponse' and filter['included']:
                    result = self.mapper.searchMapper(filter)
                    print(result)
            time.sleep(0.3)
            i = i + 1
        return result

    def profile(self, url):
        person = ""
        self.loadPage(url)
        print('Sayfa load edildi')
        html = self.driver.page_source
        find = re.findall("<code style=\"display: none\" id=\"bpr-guid-(.*?)\">([\s\S]*?)</code>", html)
        for data in find:
            if '*profile' in data[1]:
                person = json.loads(parse.unquote(self.html_escape(data[1])))
        return self.mapper.profileMapper(person)

    def saverequest(name, data):
        with open(name, 'w+') as file:
            file.write(data)
            file.close()

    def html_escape(self, text):
        return text.replace("&quot;", '"').replace('&apos;', "'").replace('&gt;', '>').replace('&lt;', '<')
