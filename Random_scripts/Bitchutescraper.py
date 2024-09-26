#/html/body/div[5]/div[1]/div[5]/div[2]/div/div[2]/div/div/div[1]/div[1]/div/div/div/div[2]/video/source
from typing import List, Any
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile   #wooa look at all these libraries, WOOAOAOAAOAOA
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time
import os
import urllib.request           
import moviepy.editor
from moviepy.editor import *
options = Options()
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

driver = loadprofile("n")
jool = 0
vids = []
file = open(os.getcwd() +  "\\bitchute.txt", 'r')
vids = file.readlines()
input("fix script extension thing")
for a in vids:
    driver.get(a)
    time.sleep(3)
    RawVidName = "defaultVideName"
    RawVidName = driver.title
    rawvid = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[5]/div[2]/div/div[2]/div/div/div[1]/div[1]/div/div/div/div[2]/video/source").get_attribute('src')
    print(RawVidName)
    urllib.request.urlretrieve(rawvid, "G:\\Downloads\\" + RawVidName + ".mp4")
driver.quit()
