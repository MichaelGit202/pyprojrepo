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


def main():
        link = input("Link: ")
        head = input("run headless? y/n")
        driver = loadprofile(head)
        driver.get(link)
    #try:
        a = driver.find_elements_by_css_selector("td.playlistDownloadSong > a")
        links = [elem.get_attribute('href') for elem in a]
        #print(links)
        for i in links:
            driver.get(i)
            RawAudio = driver.find_element_by_id("audio").get_attribute("src")
            print(RawAudio)
            name = driver.find_element_by_xpath("/html/body/div/div[2]/div/p[3]/b[2]").text
            urllib.request.urlretrieve(RawAudio,"G:\\Downloads\\" + name + ".mp3")
            
        #https://vgmsite.com/soundtracks/game-soundtracks/album/super-mario-sunshine-game-rip/01.%2520Title%2520Screen.mp3
        #https://vgmsite.com/soundtracks/super-mario-sunshine-game-rip/hyivtzvzsq/01.%20Title%20Screen.mp3
        #input()
        driver.quit()
    #except:
        #input()
        #print("broke")
        #driver.quit()

main()





