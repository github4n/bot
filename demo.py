# from buySnkre import BuySnkrs
from appLogin import LoginInit
import sqlite3
import re
import requests
import json

def getPostpayLink(productId, shoesLink):
    url = "https://api.nike.com/merch/products/v2/" + productId
    response = requests.get(url).json()
    postpayLink = shoesLink + "?LEStyleColor={styleColor}&LEPaymentType=Alipay".format(styleColor=response["styleColor"])
    return postpayLink

def buySet(shoesUrl):
    response = requests.get(shoesUrl).text
    launchId = re.findall(r"\"launchViewId\":\"(.*?)\"", response, re.S | re.I)[0]
    size = re.findall(r"\"sizes\":(.*?),\"_fetchedAt\"", response, re.S | re.I)[0]
    productId = re.findall(r"product\":{\"productId\":\"(.*?)\"", response, re.S | re.I)[0]
    shoesLink = re.findall(r"canonical\" href=\"(.*?)\"", response, re.S | re.I)[0]
    postpayLink = getPostpayLink(productId, shoesLink)
    stock = []
    outOfStock = []
    j_size = json.loads(size)
    for s in j_size:
        if j_size[s]["available"]:
            stock.append(j_size[s]["localizedSize"])
        else:
            outOfStock.append(j_size[s]["localizedSize"])
    stock.sort()
    outOfStock.sort()
    if len(outOfStock) > 0:
        print(" ".join(outOfStock) + "尺码缺货\n请选择" + " ".join(stock))
    else:
        print("所有尺码有货\n请选择" + " ".join(stock))

    shoesSize = 41
    skuId = ''
    for s in j_size:
        if j_size[s]["localizedSize"] == shoesSize:
            usShoesSize = s
            skuId = j_size[s]["skuId"]
    return shoesSize, launchId, skuId, productId, postpayLink

# shoesSize, launchId, skuId, productId, postpayLink = buySet("https://www.nike.com/cn/launch/t/air-jordan-720-proto-max-gym-red-black/")

def main():
    conn = sqlite3.connect("user.db")
    conn.text_factory = str
    c = conn.cursor()
    allUser = c.execute("SELECT * from user").fetchall()
    for user in allUser:
        refreshToken = user[3]
        username = user[4]
        passwd = user[2]
        ceshi=LoginInit(refreshToken, username, passwd)
        print (ceshi.sendRequestsToHost(data=ceshi.getLoginRequests()))



main()

