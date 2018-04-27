from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from time import sleep
from .spider import *


def crawl_webpage(page_url):
    driver = webdriver.Remote(
        command_executor='http://chromedriver:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME)
    driver.get(page_url)
    driver.find_element_by_xpath(JS_XPATH).click()
    sleep(CRAWLER_TIMEOUT)
    content = driver.find_element_by_xpath(CONTENT_XPATH).text
    content_header = driver.find_element_by_xpath(CONTENT_HEADER_XPATH).text
    driver.close()
    return content, content_header
