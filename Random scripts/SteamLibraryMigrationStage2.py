from typing import List, Any
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile   #wooa look at all these libraries, WOOAOAOAAOAOA
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from time import sleep
import os
import urllib.request           
import moviepy.editor
from moviepy.editor import *
options = Options()
aucount = 0
vicount = 0
def loadprofile(head):
    if head == "y":
        options.add_argument("--headless")
    options.add_argument("--mute-audio")
    print("Loading Profile")
    binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")  # yea if this ever breaks good luck
    # #profile = FirefoxProfile("C:\\r2q2awfq.default-release")
    scriptlocation = os.getcwd()
    profile = webdriver.FirefoxProfile(scriptlocation + "\\lcf557oe.Scraper")
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("media.volume_scale", "0.0")
    phoneset = "Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) FxiOS/1.0" \
               " Mobile/12F69 Safari/600.1.4"
    profile.set_preference('browser.download.folderList', 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir", 'G:\Downloads')
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")
    profile.DEFAULT_PREFERENCES['frozen']["general.useragent.override"] = phoneset

    driver = webdriver.Firefox(options=options, firefox_profile=profile, firefox_binary=binary,  # or something might not be updated IDFK
                               executable_path=scriptlocation + "\\FirefoxWebDriver\\geckodriver.exe")
    print("Profile instantiated")
    return driver
head = "n"
driver = loadprofile(head)
link = input("link")
driver.get(link)
input('login')
file = open(os.getcwd() +  "\\steam.txt", 'r')
splitparams = file.readlines()
Results = []
Failed = []

for a in splitparams:
    Results = a.split("/n", -1)

for b in Results:
    print(b)
    try:
        driver.get(b)
    except:Failed.append(b)
    try:
        date = driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[4]/div/div[2]/div/div[1]/div[2]/select[3]/option[70]")
        date.click()
        dl = driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[4]/div/div[2]/div/div[1]/div[3]/a[1]/span")
        dl.click()
    except:print("no")

    try:
        driver.implicitly_wait(2)
        Button = driver.find_element_by_css_selector('#add_to_wishlist_area > a:nth-child(1) > span:nth-child(1)')
        Button.click()                                
    except:Failed.append(b)
#/html/body/div[1]/div[7]/div[4]/div[1]/div[3]/div[4]/div[2]/div/div/div[1]/a/span
#add_to_wishlist_area
#btnv6_blue_hoverfade btn_medium
scriptlocation = os.getcwd()   
f = open(scriptlocation + "\\failed.txt", 'x')
for i in Failed:
    f.write(i)
    f.write("/n")
f.close()
driver.quit()
