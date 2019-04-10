#coding=utf-8
import requests,time,json
from selenium import webdriver

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
login=browser.find_element_by_class_name("login-text")
login.click()
login1=browser.find_element_by_link_text("使用电子邮件登录。")
login1.click()
username=browser.find_element_by_name("emailAddress")
username.send_keys("549705907@qq.com")
password=browser.find_element_by_name("password")
password.send_keys("DAda549705907")
loginbu=browser.find_elements_by_tag_name("input")
loginbu[7].click()
time.sleep(5)
acookies = browser.get_cookies()
cookie=""
if acookies != None:
    for i in acookies:
        cookie += (i['name'] + "=" + i['value'] + ";")
print(cookie)
head={
"accept":"*/*",
"accept-encoding": "gzip, deflate, br",
"accept-language": "zh-CN,zh;q=0.9",
"cache-control": "no-cache",
"cache": cookie,
"pragma": "no-cache",
"referer": "https://www.nike.com/cn/zh_cn/e/nike-plus-membership",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
}


browser.close()
