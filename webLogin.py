#coding=utf-8
import requests,time,json
from selenium import webdriver

def webLogin(email,passwd):
    chromeOptions = webdriver.ChromeOptions()
    #无界面
    # chromeOptions.add_argument('--headless')
    #关闭图片
    prefs = {"profile.managed_default_content_settings.images": 2}
    chromeOptions.add_experimental_option("prefs", prefs)
    #禁用gpu加速
    chromeOptions.add_argument('--disable-gpu')

    browser=webdriver.Chrome(options=chromeOptions)

    browser.get("https://www.nike.com/cn/zh_cn/")
    login=browser.find_element_by_css_selector("#AccountNavigationContainer > button")
    login.click()
    login1=browser.find_element_by_css_selector(".mobileNumberToEmailLoginLink > a")
    login1.click()
    username=browser.find_element_by_name("emailAddress")
    username.send_keys(email)
    password=browser.find_element_by_name("password")
    password.send_keys(passwd)
    loginbu=browser.find_element_by_css_selector(".loginSubmit > input")
    loginbu.click()
    time.sleep(5)
    acookies = browser.get_cookies()
    cookie=""
    if acookies != None:
        for i in acookies:
            cookie += (i['name'] + "=" + i['value'] + ";")
    browser.close()
    return cookie