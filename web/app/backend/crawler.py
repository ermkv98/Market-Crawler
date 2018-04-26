from selenium import webdriver
from time import sleep
from spider import *


def crawl_webpage(page_url):
    driver = webdriver.Chrome()
    driver.get(page_url)
    driver.find_element_by_xpath(JS_XPATH).click()
    sleep(CRAWLER_TIMEOUT)
    content = driver.find_element_by_xpath(CONTENT_XPATH).text
    content_header = driver.find_element_by_xpath(CONTENT_HEADER_XPATH).text
    return content, content_header
