import requests,random,time
from lxml import etree
kv={"user-agent":"Mozilla/5.0"}

url1="https://mushroomobserver.org/observations?page="
url2="&pattern=Pleurotus+ostreatus"
for i in range(87):
    r = requests.get(url1+str(i)+url2,headers = kv)
    r = etree.HTML(r.text)
    detail_urls = r.xpath('//div[@class="rss-where"]/small/a/span')
    for j in detail_urls:
        print(j.text)
    print(i)
    time.sleep(random.randrange(1,20))