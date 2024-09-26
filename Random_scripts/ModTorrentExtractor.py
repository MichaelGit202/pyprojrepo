import zipfile
import os.path
import shutil

path = os.getcwd() + '\\extract'
a = os.listdir(path)
l = 0
while l < len(a):               #adds file path in additon to the name
    a[l] = path + "\\" + a[l]   #: ie: 1.file ->  c:\\users\\...1.file
    l += 1
    
j = 0
while j < len(a):
    if "." in a[j]:         #<-is it a file it a file or a file directory
        if ".zip" in a[j]:  #is it a zip file?
                                      #zip.extractall(os.getcwd() + "\\extracted") broken
            fh = open(a[j], 'rb')
            z = zipfile.ZipFile(fh)
            for name in z.namelist():    #copy items from zipfile
                outpath = path + "\\extracted"
                z.extract(name, outpath)
            fh.close()
            z.close
        else:       
            shutil.move(a[j], path + "\\extracted")
    else:                   
        b = os.listdir(a[j])    #actions taken if directory add the contents to a
        l = 0
        while l < len(b):       
            b[l] = a[j] + "\\" + b[l]
            l += 1
        for c in b:
            a.append(c)
        
    j += 1 
    





#a = os.listdir(path)

#c = path + "\\" + a[0]
#b = os.listdir(path + "\\" + a[0])

#a = os.listdir(c + "\\" + b[0])

#with ZipFile(c + "\\" + b[0] + "\\" + a[0] + "\\" + "01.ahx.zip", 'r') as zip:
#     zip.extractall(os.getcwd() + "\\extracted")
