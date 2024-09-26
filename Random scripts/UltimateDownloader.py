from typing import List, Any
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile   #wooa look at all these libraries, WOOAOAOAAOAOA
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import urllib.request
import os
options = Options()
#User steps through webpage to grab and download an element and the program can
#repeat that procedure.


#to do, that requests user input, 2 parralel arrays, arr1:procedure type
#arr2 xpah input
#need:
#list grab -> href grab
#download element -> Src:grab
#step into
#button click
#Save website preset

def loadprofile(head):
    print("Loading Profile")
    if head == "y":
        options.add_argument("--headless")
        
    options.add_argument("--mute-audio")
    binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")  # yea if this ever breaks good luck
    # #profile = FirefoxProfile("C:\\r2q2awfq.default-release")
    scriptlocation = os.getcwd()
    profile = webdriver.FirefoxProfile(scriptlocation + "\\lcf557oe.Scraper")
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("media.volume_scale", "0.0")
    profile.set_preference('browser.download.folderList', 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir", 'G:\Downloads')
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")
    driver = webdriver.Firefox(options=options, firefox_profile=profile, firefox_binary=binary,  # or something might not be updated IDFK
                               executable_path=scriptlocation + "\\FirefoxWebDriver\\geckodriver.exe")
    print("Profile instantiated")
    return driver

def openlink(driver, link):
    divided = split(link)
    print(divided)
    driver.get(divided[1])

def getsomething(driver, path):
    divided = path.split(":")
    return driver.get(divided[1])
    
def split(procedure):
        ok = procedure.split
        return ok
        
def download(driver, var, procedure):
    try:
        divided = split(procedure)
        name = getsomething(divided[1])
        for a in var:
            urllib.request.urlretrieve(a, name)#urllib works
    except:print("failed to download")
     
def parselist(driver, xpath, var=[]): #drills down by one by opening list link and returns list
        newvar = []                  #of what it captures with the xpath variable
        for a in var:
            driver.get(a)
            newvar.append(driver.find_element_by_xpath(xpath))  #ex var=[l1,l2,l3] and l had acces to further lists
        return newvar                                           #call parse list newvar=[l1 contents array, l2 contents array] ect

#def saveprocedure(procedure=[], path=[]):
    #hal = "rouge"
            
#def readprocedures(proc,procedure,path):
   #mike = "mad"
    
def main():
    procedure =[]
    Contents = []
    #ynproc = "defaultread"
    imp = "DefaultString"
    #readprocedures(ynproc,procedure,path )
    #ynproc = input("Load a preset n for no/procedure name")
    #if ynproc != "n":
        #readprocedures(ynproc,procedure,path)
        #imp = "stop"

    #getting the procedure
    while imp != "stop":
        print("(stop to stop)Define Procedure")
        imp = input()
        if imp != "stop":
            procedure.append(imp)
            #print("Give Xpath if n/a give nothing")
            #imp = input()
            #path.append(imp)
    head = input("Run headless?y/n")
    driver = loadprofile(head)
    integrate = 0
    while integrate < len(procedure):
        if "dl" in procedure[integrate] : #download procedure is to get the name
            download(driver, Contents, procedure[integrate])
        if "ep" in procedure[integrate] : #entrypoint
            openlink(driver, procedure[integrate])
        if "pl" in procedure[integrate] : #parse a list
            contents = parselist(driver, procedure[integrate], Contents)
        if "gl" in procedure[interate] : #grab list
           Contents = getsomething(driver, procedure[integrate])
        integrate += 1
    
        
main()
    

