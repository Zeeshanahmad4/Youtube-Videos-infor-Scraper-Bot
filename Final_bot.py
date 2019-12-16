from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import csv
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


a = 1
b = 1
delay = 50

#protype of function
def append_data1(file_path, name):
    fieldnames = ['paragraph']

    with open(file_path, "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #writer.writeheader()
        writer.writerow({
            "paragraph": name
        })

def append_data(file_path, name,street,email,wbsite,phn):
    fieldnames = ['paragraph','stret','Email','Website','Phon']

    with open(file_path, "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #writer.writeheader()
        writer.writerow({
            "paragraph": name,
            "stret" : street,
            "Email" : email,
            "Website" : wbsite,
            "Phon" : phn,
        })


browser = webdriver.Chrome()
browser.set_page_load_timeout(10000)
with open("input.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print row
        url = row[0]
        browser.get(url)
        sleep(1)
        elem = browser.find_element_by_tag_name("body")
        lista = []
        elem = browser.find_element_by_tag_name("body")
        for i in range(200):
            elem.send_keys(Keys.PAGE_DOWN)
            elem.send_keys(Keys.PAGE_DOWN)
            elem.send_keys(Keys.PAGE_DOWN)
            sleep(0.3)
        post_elems = browser.find_elements_by_xpath("//*[@id='video-title']")
        print len(post_elems)
        for i in post_elems:
            links = i.get_attribute("href")
            print links
            append_data1("links.csv",links)


with open("links.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print row
        a += b
        print a 
        url = row[0]
        browser.get(url)
        myElem = WebDriverWait(browser, delay).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='container']/h1/yt-formatted-string")))
        name  = browser.find_element_by_xpath("//*[@id='container']/h1/yt-formatted-string").text
        name8 = name.encode('utf-8')
        link = browser.current_url
        html = browser.page_source
        soup = BeautifulSoup(html,"lxml")
        divTag = soup.find_all("yt-formatted-string", {"class": "style-scope ytd-toggle-button-renderer style-text"})
        likes  = divTag[0].text
        myElem = WebDriverWait(browser, delay).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='upload-info']/span")))
        date  = browser.find_element_by_xpath("//*[@id='upload-info']/span").text
        timea = soup.find_all("span", {"class": "ytp-time-duration"})
        timeb = timea[0].text
        print timeb
        append_data("output.csv",name8,link,likes,date,timeb,)


