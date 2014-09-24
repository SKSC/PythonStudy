import urllib2
import httplib
import mysql.connector
from mysql.connector import errorcode
import re
import types
import time
import sys
import os.path
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool as ThreadPool

url="http://www.sassandbide.com/sitemap.xml"
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36"

def insertDB(item):
    config = {
              'user': 'root',
              'password':'',
              'database':'sass'
              }
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print "Something is wrong with your login"
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print "Database does not exists"
        else:
            print (err)
    cursor = cnx.cursor()
    add_item =("INSERT INTO itemInfo " 
               "(Name, Des, Detail, Color, Info, imageBox, Image, Size, Prize, URL) "
               "VALUES (%(name)s, %(desc)s, %(detail)s, %(color)s, %(info)s, %(imageBox)s, %(image)s, %(size)s, %(prize)s, %(url)s)")
    try:
        data_item = {
                     "name"      : str(item['title']),
                     "desc"      : str(item['desc']),
                     "detail"    : str(item['detail']),
                     "color"     : str(item['color']),
                     "info"      : str(item['info']),
                     "imageBox"  : str(item['imageBox']),
                     "image"     : str(item['image']),
                     "size"      : str(item['size']),
                     "prize"     : str(item['prize']),
                     "url"       : str(item['url']),
                     }
    except UnicodeEncodeError:
        print str(item['title'])
    else:
        try:
            cursor.execute(add_item, data_item)
            cnx.commit()
            cursor.close()
            cnx.close()
        except mysql.connector.errors.DataError:
            print str(item['title'])
    
def polishAtt(name, detail, color,info,imageBox, image,size, prize,url):
    item = {
            'title'  : '',
            'desc'   : '',
            'detail' : detail,
            'color'  : color,
            'info'   : '',
            'prize'  : prize,
            'imageBox' : imageBox,
            'image'  :'',
            'size'   :'',
            'url'    :url,
            }
    if type(name) is types.StringType:
        item['title'] = name
    else:
        item['title'] = name['title']
        item['desc']  = name ['desc']
        
    if type(info) is types.StringType:
        item['info']=info
    else:
        for i in range(0,len(info)):
            item['info']+= "\n"+info[i]
    if type(image) is types.StringType:
        item['image']=image
    else:
        for i in range(0,len(image)):
            item['image']+="\n"+image[i]
    if type(size) is types.StringType:
        item['size']=size
    else:
        for i in range (0,len(size)):
            item['size']+="\n"+size[i]
    return item

def fetch(url):
    try:
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        content = response.read()
    except urllib2.HTTPError,httplib.BadStatusLine:
        print url
        return False
    else:
        return content

def parserSitemap(sitemap):
    m=re.compile("http://backoffice\S*?html");
    clothSite=m.findall(sitemap)
    return clothSite
    
def parserName(content):
    soup = BeautifulSoup(content)
    itemName = soup.find_all('div', class_='product-name')
    try:
        soup = BeautifulSoup(str(itemName[0]))
    except IndexError:
        return False
    else:
        itemName = {
                    'title' : soup.h1.string,
                    'desc' : soup.p.string,
                    }
        return itemName
    
def parserDetail(content):
    soup = BeautifulSoup(content)
    itemDetail = soup.find_all('div', class_='box-collateral box-description')
    try:
        soup = BeautifulSoup(str(itemDetail[0]))
        itemDetail = soup.find_all('div')
        soup = BeautifulSoup(str(itemDetail[1]))
    except IndexError:
        return "Detail does not exist"
    else:
        itemDetail = soup.div.get_text()
        return itemDetail.strip()
    
def parserColour(content):
    soup = BeautifulSoup(content)
    itemColor = soup.select('fieldset[class="product-options"]')
    try:
        soup = BeautifulSoup(str(itemColor[0]))
        itemColor = soup.select('option[selected="selected"]')
        soup = BeautifulSoup(str(itemColor[0]))
        itemColor = soup.option.get_text()
    except IndexError:
        return "color not exists"
    else:
        return itemColor

def parserInfo(content):
    soup = BeautifulSoup(content)
    try:
        itemInfo = soup.find_all("div",id="tab-1")
        soup = BeautifulSoup(str(itemInfo[0]))
    except IndexError:
        return "Info does not exist"
    else:
        itemInfo = (soup.find_all('p',limit = 2))
        info = []
        for i in range(0,len(itemInfo)):
            soup = BeautifulSoup(str(itemInfo[i]))
            info.append(soup.p.get_text())
        return info
    
def parserImage(content):
    soup = BeautifulSoup(content)
    itemImage = soup.find_all("ul",class_="overview")
    try:
        soup = BeautifulSoup(str(itemImage[0]))
    except IndexError:
        return "Image does not exist"
    else:
        itemImage = soup.select("a[href]")
        imageurl=[]
        for item in itemImage:
            soup = BeautifulSoup(str(item))
            imageurl.append(soup.a['href'])
        itemImage = downloadImage(imageurl)
        return itemImage 

def parserImageContainer(content):
    soup = BeautifulSoup(content)
    itemImage = soup.find_all("a",class_="MagicZoom")
    imageurl = []
    try:
        imageurl.append(str(itemImage[0]['href']))
    except IndexError:
        return "Image does not exist"
    else:
        itemImage = downloadImage(imageurl)
        return itemImage 
    
def parserSize(content):
    size = re.compile('"label":[\S\s]*?,')
    #the size in first place is not the correct one
    itemSize = size.findall(content)
    size= []
    for i in range(1,len(itemSize)):
        size.append(itemSize[i][9:len(itemSize[i])-2])
    if len(size) <= 1:
        return "Size does not exist"
    else:
        return size

def parserPrice(content):
    soup = BeautifulSoup(content)
    itemPrice = soup.find_all("span",class_="price special-price")
    if itemPrice ==[]:
        itemPrice = soup.find_all("span",class_="price")
    try:
        soup = BeautifulSoup(str(itemPrice[0]))
    except IndexError:
        return False
    else:
        itemPrice = soup.span.get_text().strip()
        return itemPrice
    
def downloadImage(imageurl):
    imagePath=[]
    for url in imageurl:
        filename = os.path.basename(url)
        socket = urllib2.urlopen(urllib2.Request(url))
        data = socket.read()
        socket.close()
        file = open('/Users/Path/'+filename, 'w')
        file.write(data)
        file.flush()
        file.close()
        imagePath.append(filename)
    return imagePath
    
def runThread(url):
    content = fetch(url)
    if content !=False:
        name    = parserName(content)
        if name !=False:
            detail  = parserDetail(content)
            color   = parserColour(content)
            info    = parserInfo(content)
            imageBox = parserImageContainer(content)
            image   = parserImage(content)
            size    = parserSize(content)
            prize   = parserPrice(content)
            item = polishAtt(name, detail, color,info,imageBox, image,size, prize,url)
            insertDB(item)
        
def main():
    start = time.time()
    reload(sys)
#    sys.setdefaultencoding('utf-8')
    sitemap = fetch(url)
    clothSite = parserSitemap(sitemap)
    print "total "+str(len(clothSite))
    pool = ThreadPool(8)
    pool.map(runThread, clothSite)
    pool.close() 
    pool.join() 
    print "done"
    print str(time.time()-start)

    
main()