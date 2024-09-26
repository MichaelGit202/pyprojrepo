import zipfile
import os
import shutil
from datetime import datetime

path = os.getcwd() + '\\extract'
a = os.listdir(path)
l = 0
timecount = len(a)/25
while l < len(a):               #adds file path in additon to the name
    a[l] = path + "\\" + a[l]   #: ie: 1.file ->  c:\\users\\...1.file
    l += 1

start = datetime.now()

j = 0
while j < len(a):
    
    if j >= timecount:      
        os.system('cls')
        timecount += len(a)/500
        time = datetime.now() - start
        percent = (j/len(a)) * 100
        print(str(j) + "/" + str(len(a)) + "    " + str(percent) + "%")
        print(time)


    
    if "." in a[j]:         #<-is it a file it a file or a file directory
        if ".zip" in a[j]:  #is it a zip file?
            try:                          #zip.extractall(os.getcwd() + "\\extracted") broken
                fh = open(a[j], 'rb')
                z = zipfile.ZipFile(fh)
                for name in z.namelist():    #copy items from zipfile
                    outpath = os.getcwd() + "\\extracted"
                    z.extract(name, outpath)
                    if ".zip" in name:                  #so if its a zip we extract it and re-add it to the list
                        a.append(outpath + "\\" + name)  #to be later be extracted
            
                fh.close()
                z.close
            except:
                print(a[j] + " has failed to be processed")
                print(a[j], file=open("failed.txt", "a"))
                try:
                    shutil.move(a[j], os.getcwd() + "\\Failed")
                except:
                    print("Failed to move to failed dir", file=open("failed.txt", "a"))
                
        else:       
            try:
                print(a[j])
                shutil.move(a[j], os.getcwd() + "\\extracted")
            except:
                print(a[j] + " has failed to be processed")
                print(a[j], file=open("failed.txt", "a"))
                try:
                    shutil.move(a[j], os.getcwd() + "\\Failed")
                except:
                    print("Failed to move to failed dir", file=open("failed.txt", "a"))
                
    else:                   
        b = os.listdir(a[j])    #actions taken if directory add the contents to a
        l = 0
        while l < len(b):       
            b[l] = a[j] + "\\" + b[l]
            l += 1
        for c in b:
            a.append(c)
        
    j += 1


#delete all zips
path = os.getcwd() + '\\extracted'
a = os.listdir(path)
l = 0
while l < len(a):               #adds file path in additon to the name
    a[l] = path + "\\" + a[l]   #: ie: 1.file ->  c:\\users\\...1.file
    l += 1

for file in a:
    if ".zip" in file:
        os.remove(file)




#a = os.listdir(path)

#c = path + "\\" + a[0]
#b = os.listdir(path + "\\" + a[0])

#a = os.listdir(c + "\\" + b[0])

#with ZipFile(c + "\\" + b[0] + "\\" + a[0] + "\\" + "01.ahx.zip", 'r') as zip:
#     zip.extractall(os.getcwd() + "\\extracted")
