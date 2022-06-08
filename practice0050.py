import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS'] #正常顯示中文
plt.rcParams['axes.unicode_minus'] = False #正常顯示－號

#爬蟲
month, high, low = [],[],[]
url = "https://www.twse.com.tw/exchangeReport/FMSRFK?response=html&date=20210101&stockNo=0050"
content = requests.get(url).text
#print(content)
sp = BeautifulSoup(content, "lxml")
datas = sp.select("table")[0]
title = datas.find("div").text.replace(" ","")
rows = datas.select("tbody tr")
for row in rows:
    cols = row.select("td")
    month.append(int(cols[1].text))
    high.append(float(cols[2].text))
    low.append(float(cols[3].text))

#繪製表格
plt.plot(month, high, 'g--*', color="r", linewidth=2.0, label="最高價")
plt.plot(month, low, marker="o", color="g", linewidth=2.0, label="最低價")
plt.legend()
plt.title(title)
plt.xlabel("月份")
plt.ylabel("金額")
plt.show()