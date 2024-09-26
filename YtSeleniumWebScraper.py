



from typing import List, Any
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile   
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time
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


def filenameformat(string):
    string = string.replace("\"", " ")
    string = string.replace("/", " ")
    string = string.replace(":", " ")
    string = string.replace("*", " ")
    string = string.replace("?", " ")
    string = string.replace('"', " ")
    string = string.replace("<", " ")
    string = string.replace(">", " ")
    string = string.replace("|", " ")
    return string

def fileexists(filename):
    return os.path.exists(filename)

def downloadlink(driver, rawvid, yn, splity):
    driver.get(rawvid)
    time.sleep(3)
    button = driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/button')
    button.click()
    time.sleep(2)
    j = 1
    while j != 0:
        try:
            vidplaya = driver.find_element_by_xpath('/html/body/div/div[2]/ytm-custom-control/div[1]')
            vidplaya.click()
            j = 0
        except:
            print("failed to play")
            if j == 5:
              driver.refresh()
              j = 1
        time.sleep(1)
    bod =  driver.find_element_by_xpath('/html/body/div/div[2]/ytm-custom-control/div[1]')
    #bod.click()
    unpausebutton = driver.find_element_by_xpath('/html/body/div/div[2]/ytm-custom-control/div[2]/div/div[3]/button[3]')
    unpausebutton.click()
    time.sleep(1)
    quality = driver.find_element_by_xpath('/html/body/div/div[2]/ytm-custom-control/div[2]/div/div[1]/button[2]')
    quality.click()
    try:
        seventwenty = driver.find_element_by_xpath('/html/body/div[2]/dialog/div[2]/ytm-select[2]/select/option[1]')
        seventwenty.click()                         
    except:
        try:
            seventwenty = driver.find_element_by_xpath('/html/body/div[2]/dialog/div[2]/ytm-select/select/option[1]')
            seventwenty.click()
        except:
            input("its fucking up and i dont know why, quality thing")
    time.sleep(1)
    okbutton= driver.find_element_by_xpath('/html/body/div[2]/dialog/div[3]/c3-material-button/button')
    okbutton.click()
    time.sleep(1)
    #button = driver.find_element_by_xpath('/html/body/div/div[2]/ytm-custom-control/div[2]/div/div[2]/button[2]')
    #button.click()
    time.sleep(3)
    rawvidname = "defaultVideName"
    RawVidName = driver.find_element_by_xpath("/html/body/ytm-app/div[1]/ytm-watch/ytm-single-column-watch-next-results-renderer/ytm-slim-video-metadata-section-renderer/ytm-slim-video-information-renderer/button/div/div/h2")
    RawVidName = RawVidName.text
    RawVidName = filenameformat(RawVidName)
    print(RawVidName)
    rawvid = driver.find_element_by_tag_name('video').get_attribute('src')
    driver.get(rawvid)
    time.sleep(1)
    download_file = driver.find_element_by_xpath('/html/body/video')
    if fileexists(rawvidname) == True: #+ ".mp4"
     vicount += 1
     urllib.request.urlretrieve(rawvid,"G:\\Downloads\\" + RawVidName + str(vicount) + ".mp4")
     if splity == "y":
         print("damn")
     else: convert_audio(yn, RawVidName)
      
    else:
        urllib.request.urlretrieve(rawvid, "G:\\Downloads\\" + RawVidName + ".mp4")
        return (convert_audio(yn, RawVidName))

def convert_audio(yn, RawVidName):
    if yn == "y":
        vidirect = "G:\\Downloads\\" + RawVidName + ".mp4"
        video = moviepy.editor.VideoFileClip(vidirect)
        audio = video.audio
        if fileexists(RawVidName + ".mp3") == True:
           count += 1
           audio.write_audiofile("G:\\Downloads\\" + RawVidName + str(aucount) + ".mp3")
           return "G:\\Downloads\\" + RawVidName + ".mp3"
        else:
            audio.write_audiofile("G:\\Downloads\\" + RawVidName + ".mp3")
            return ("G:\\Downloads\\" + RawVidName + ".mp3")
    else: print("no convert")

def playlist_git(driver, link):
    print("getting playlist")
    arrplay = []
    driver.get(link)
    time.sleep(3)
    Lzcall = driver.find_element_by_xpath("/html/body/ytm-app/div[1]/ytm-watch/ytm-single-column-watch-next-results-renderer/ytm-playlist/div/div/lazy-list")
    arrListelements = Lzcall.find_elements_by_tag_name("ytm-playlist-panel-video-renderer")
    for a in arrListelements:
        call = a.find_element_by_tag_name('a')
        partial = call.get_attribute('href')
        arrplay.append(str(partial))

    time.sleep(1)
    return arrplay

def timeconvert(inTime): #converts sting:Hours:Minutes:Seconds to seconds int
    divided = inTime.split(":")
    print("Start")
    total = 0
    if len(divided) == 1:
        total += int(divided[0])
        print(divided)
        print("1")
        print(total)       
    elif len(divided) == 2:
        total += (int(divided[0]) * 60 + int(divided[1]))
        print(divided)
        print("2")
        print(total)  
    elif len(divided) == 3:
        total += (int(divided[0]) * 3600 + int(divided[1]) * 60 + int(divided[2]))
        print(divided)
        print("3")
        print(total)  
    else: return 0
    return total


def main():
    filelocate = ""
    splity = 'n'
    arrlink = []
    procedure = input("Single video(s), Playlist(p): ")
    yn = input("Convert to audio?y or n: ")
    link = input("Link: ")
    splity = input("Split the Video? Y/n (Does not work with playlist and non audio rn): ")
    cred = input("requires credentials? y/n") #when you have to login to access content
    head = input("run headless? y/n")
    if splity == "y":
        splitparams = []
        splittime = []
        splitname = []
        input("Did you fill in the txt doc in" + os.getcwd())
        file = open(os.getcwd() +  "\\splitparam.txt", 'r')
        splitparams = file.readlines()

        for a in splitparams:
            Time, Name = a.split("?")
            Name = Name.rstrip("\n")
            splittime.append(Time)  #this is stupid, but im not spending any more time on this 
            splitname.append(Name)  # It works by splitting up line(Time:name) into two parralel lists
                                    
    driver = loadprofile(head)
    if cred == "y":
        driver.get(link)
        input("press enter when done")
    if procedure == "s":
        print("Single")
        arrlink.append(link)
    elif procedure == "p":
       print("Playlist")
       arrlink=(playlist_git(driver, link))
    else: print("enter a valid procedure"), main()

    for vidlink in arrlink:
        time.sleep(1)
        #try:
        filelocate = downloadlink(driver, vidlink, yn, splity)
       # except: print("download Failed")

    if splity == "y":
        listlength = len(splitname)
        count = 0
        Aclip = AudioFileClip(filelocate)
        splittime.append(Aclip.duration)
        print(listlength)
        print(filelocate)
        while count < listlength:
                print(str(count) + "/" + str(listlength))
                print(timeconvert(splittime[count]))
                Part = Aclip.subclip(splittime[count], splittime[count + 1])
                name = 'G:\\Downloads\\' + filenameformat(splitname[count]) + ".mp3"
                Part.write_audiofile(name)
                count += 1
    driver.quit()

main()


  #  btnBack = (driver.find_element_by_xpath('/html/body/ytm-app/div[2]/ytm-watch/ytm-single-column-watch-next-results-renderer/ytm-playlist/div/ytm-playlist-controls/div[1]/c3-material-button[1]/button').get_attribute('disabled'))
  #  bntNextdisable = (driver.find_element_by_xpath('/html/body/ytm-app/div[2]/ytm-watch/ytm-single-column-watch-next-results-renderer/ytm-playlist/div/ytm-playlist-controls/div[1]/c3-material-button[2]/button').get_attribute('disabled'))
  #  bntnext = driver.find_element_by_xpath('/html/body/ytm-app/div[2]/ytm-watch/ytm-single-column-watch-next-results-renderer/ytm-playlist/div/ytm-playlist-controls/div[1]/c3-material-button[2]/button/div')
   # if btnBack == 'none':
   #     fristvid = ('/html/body/ytm-app/div[2]/ytm-watch/ytm-single-column-watch-next-results-renderer/ytm-playlist/div/div/lazy-list/ytm-playlist-panel-video-renderer[1]')
  #      firstvid.click()
   # print("lmao broke")
   # time.sleep(2)
   # while bntNextdisable != 'true':
   #     print("ok")
   #     currentindex = driver.current_url
   #     rawlink = getlink(driver, currentindex)
   #     arrayplay.append(rawlink)
   #     driver.get(currentindex)
    #    bntnext.click()

#TO DO
#optional allow for multiple singular video queries
#fix video remove

#link = input("Link: ")
#driver.get(link)
#time.sleep(3)
#button = driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/button')
#button.click()
#time.sleep(3)
#rawvid = driver.find_element_by_tag_name('video').get_attribute('src')

#driver.get(rawvid)  # its working
#time.sleep(4)
#actionChains = ActionChains(driver)
#download_file = driver.find_element_by_xpath('/html/body/video')
#urllib.request.urlretrieve(rawvid, 'videoname.mp4')
# download_file.click()
# actionChains.context_click(download_file).perform()
#time.sleep(1)
# actionChains.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
#video = moviepy.editor.VideoFileClip("C:\\Program Files (x86)\\Python Projects\\videoname.mp4")
#audio = video.audio
#audio.write_audiofile("G://Downloads// " + "audio.mp3")
#driver.quit()

#def getlink(driver, link):
  #  driver.get(link)
  #  time.sleep(3)
  #  button = driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/button')
   # button.click()
   # time.sleep(3)
   # return driver.find_element_by_tag_name('video').get_attribute('src')







