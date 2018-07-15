from bs4 import BeautifulSoup
import requests


# f = requests.get("http://www.qpmall.com")
# html = f.text
# imgs = BeautifulSoup(html).find_all("img",class_="lazy")

# for item in imgs:
#     print(item["data-original"])

def getImageUrls(url,ele,class_, source):
    # get请求
    f = requests.get(url=url)
    # html
    html = f.text
    # 元素
    eles = BeautifulSoup(html).find_all(ele,class_=class_)

    boxs = list()
    for item in eles:
        boxs.append(item[source])
    return boxs

result = getImageUrls("https://www.qpmall.com","img","lazy","data-original")


# 保存文件1
for (i,item) in enumerate(result):

    if i>10:
        break
    html = requests.get(url=item)


    name = "图片-"+str(i)+".jpg"
    with open(name, "wb") as file:
        file.write(html.content)
        file.flush()
        file.close()
    
    print("第%s张图片完成" % i)
    