from typing import List, Any
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile   #wooa look at all these libraries, WOOAOAOAAOAOA
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
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
element = driver.find_element_by_xpath('/html/body')
linkarr = []

j = 0
test = []
#No smart options and im not going to go recode this shit in java script so you get this
test.append(driver.find_element_by_css_selector("div.wishlist_row:nth-child(1) > a:nth-child(2)").get_attribute("href"))
test.append(driver.find_element_by_css_selector("div.wishlist_row:nth-child(2) > a:nth-child(2)").get_attribute("href"))
test.append(driver.find_element_by_css_selector("div.wishlist_row:nth-child(3) > a:nth-child(2)").get_attribute("href"))
test.append(driver.find_element_by_css_selector("div.wishlist_row:nth-child(4) > a:nth-child(2)").get_attribute("href"))
test.append(driver.find_element_by_css_selector("div.wishlist_row:nth-child(5) > a:nth-child(2)").get_attribute("href"))
test.append(driver.find_element_by_css_selector("div.wishlist_row:nth-child(6) > a:nth-child(2)").get_attribute("href"))
test.append(driver.find_element_by_css_selector("div.wishlist_row:nth-child(7) > a:nth-child(2)").get_attribute("href"))
test.append(driver.find_element_by_css_selector("div.wishlist_row:nth-child(8) > a:nth-child(2)").get_attribute("href"))
test.append(driver.find_element_by_css_selector("div.wishlist_row:nth-child(9) > a:nth-child(2)").get_attribute("href"))
test.append(driver.find_element_by_css_selector("div.wishlist_row:nth-child(10) > a:nth-child(2)").get_attribute("href"))
test.append(driver.find_element_by_css_selector("div.wishlist_row:nth-child(11) > a:nth-child(2)").get_attribute("href"))
test.append(driver.find_element_by_css_selector("div.wishlist_row:nth-child(12) > a:nth-child(2)").get_attribute("href"))
test.append(driver.find_element_by_css_selector("div.wishlist_row:nth-child(13) > a:nth-child(2)").get_attribute("href"))
test.append(driver.find_element_by_css_selector("div.wishlist_row:nth-child(14) > a:nth-child(2)").get_attribute("href"))
test.append(driver.find_element_by_css_selector("div.wishlist_row:nth-child(15) > a:nth-child(2)").get_attribute("href"))
while j < 1200:
    if driver.find_element_by_css_selector("div.wishlist_row:nth-child(15) > a:nth-child(2)").get_attribute("href") != test[len(test) - 1]:
        test.append(driver.find_element_by_css_selector("div.wishlist_row:nth-child(15) > a:nth-child(2)").get_attribute("href"))
    k = 0
    print(test)
    #while k < len(test):
    #    test[k] = test[k].get_attribute('href')
        
    #print(test)
   # for a in test:
   #     longth = len(test)
   #     if longth < len(linkarr):
   #         flag = false
    #        longth = longth * -1
     #       while longth != 0:
    #            if a == linkarr[len(linkarr) + longth]:
    #                flag = true
   #                 print("flag set true")
   #         if flag == false:
   #             linkarr.append(a)
   #             print("adding" + a)
    element.send_keys(Keys.ARROW_DOWN)
    sleep(.25)
    j += 1
#while j < 1200: #i should never be allowed to code again
#    test = driver.find_element_by_class_name("capsule").get_attribute('href')
#    print("what:?" + test)
#    if len(linkarr) >= 1: 
#        print("comparing " +  test + " to " + linkarr[len(linkarr) - 1])
#        if test != linkarr[len(linkarr) - 1]:
#            linkarr.append(test)
#            print("passed: " + test)
#    else:linkarr.append(test)
#    element.send_keys(Keys.ARROW_DOWN)
#    sleep(.25)
#    j += 1
driver.quit()
scriptlocation = os.getcwd()
f = open(scriptlocation + "\\steam.txt", 'x')
for i in test:
    f.write(i)
    f.write("/n")
f.close()
