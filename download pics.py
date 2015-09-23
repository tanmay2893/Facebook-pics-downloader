from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time,urllib,os
base_url = "https://www.facebook.com"
browser = webdriver.Chrome('./chromedriver')
browser.get(base_url)
element = browser.find_element_by_id("email")
element.send_keys("xxxxxx@xxxx.com")
element = browser.find_element_by_id("pass")
element.send_keys("*************")
browser.find_element_by_id("u_0_n").click()
name='***'#type id of your friend 
path=name
if not os.path.exists(path):
    os.makedirs(path)
url="https://www.facebook.com/"+name+"/photos_albums"
browser.get(url)
print 'Waiting for 10 seconds.....'
time.sleep(20)
html_source=browser.page_source
soup=BeautifulSoup(html_source)
div=soup.find_all(attrs={"class":"_5h60 _30f"})
html=div[1]
table=html.find('table')
td=table.find_all('td')
l=[]
for i in range(len(td)):
    try:
        l+=[td[i].find('a')['href']]
    except:
        break
print l
c=len(l)
q=[]
f=0
for j in range(c):
    if l[j]=='#':
        continue
    browser.get(str(l[j]))
    html_source=browser.page_source
    soup=BeautifulSoup(html_source)
    div=soup.find_all(attrs={"class":"_53s fbPhotoCurationControlWrapper fbPhotoStarGridElement fbPhotoStarGridNonStarred _53s fbPhotoCurationControlWrapper"})
    x=len(div)
    z=[]
    for i in range(x):
        f+=1
        #z+=[div[i].find('a')['href']]
        v=str((div[i].find(attrs={"class":"tagWrapper"})).find('i'))
        m=v.find('url')
        t=v[m+4:-8].replace('amp;','')
        z+=[t]
        print 'Downloading....'
        urllib.urlretrieve(t,path+'\\'+str(f)+'.jpg')
    q+=[z]
#div=soup.find(attrs={"class":"fbPhotosRedesign _4d-"})
#e=browser.find_element_by_class_name("_3i9")
'''
second=0
while second<=60:
    #browser.executeScript("window.scrollBy(0,200)", "");
    browser.execute_script("window.scrollBy(0,200)", "");
    second+=1
    try:
        element = browser.find_element_by_class_name("fbTimelineScrubber")
        break
    except:
        continue
#element=browser.find_element_by_class_name("selected")
element= browser.find_element_by_xpath("//li[@data-key='way_back']")
#e=browser.find_elements_by_css_selector(".fbTimelineScrubber > li")
'''
