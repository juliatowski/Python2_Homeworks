import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time
import json
from selenium import webdriver
import re
import random
import os
from selenium.webdriver.common.keys import Keys

main_url = "https://finance.yahoo.com/news"
driver = webdriver.Chrome()
driver.get(main_url)
sleep_sec= 4

# accepts the terms field
driver.find_element_by_xpath("//button[@type='submit']").click()
# loop as long there get new posts loaded on the site. all posts are inside the "li" tag
init_li=0
new_li = 1
while new_li > init_li:
    init_li = len(driver.find_elements_by_tag_name("li"))
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    time.sleep(sleep_sec)
    new_li=len(driver.find_elements_by_tag_name("li"))


time.sleep(sleep_sec)
# gets all urls of posts including ads
posts_url = [x.get_attribute("href") for x in driver.find_elements_by_xpath("//h3/a")]
# gets only the urls which lead to a yahoo finance news site
articles_url = [x for x in posts_url if "https://finance.yahoo.com/news" in x]

print(len(posts_url),len(articles_url))

for x in articles_url:
    print(x)

#dir_save="yahoo_finance_news"
#try:
 #   os.mkdir(dir_save)
  #  print("directory created")
#except:
 #   print("directory exists")


#bsp für einen post
post_url ='https://finance.yahoo.com/news/commerce-secretary-gina-raimondo-china-trade-134452903.html'
driver.get(post_url)
#agreing to terms and conditions of webpage
button_agree = driver.find_elements_by_tag_name('Button')[0]
button_agree.click()
link_text=driver.find_elements_by_tag_name('a')[0]
link_text.click()

#Scraping for info
#title
title_s = driver.find_element_by_tag_name('h1')
#time
time_s= driver.find_element_by_tag_name('time')
#text content
text_s=driver.find_element_by_class_name('caas-body')
##knopf um ganzen text zu laden

#Source (Funktioniert nicht, eventuell von der main page abrufen)
#source_s= driver.find_element_by_css_selector("a[alt ='Reuters'][class='caas-img caas-loaded']")
source=[]
#source.append(source_s.text)
title=[]
title.append(title_s.text)
time=[]
time.append(time_s.text)
text=[]
text.append(text_s.text)

article_infos = pd.DataFrame({'Title':title,'Datetime': time})
#({'Title':title,'Source':source, 'Datetime': time, 'Name': name, 'Path':path})
                              
print(article_infos)

###hallo
