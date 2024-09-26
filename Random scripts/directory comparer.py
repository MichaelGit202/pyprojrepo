import zipfile
import os.path
import shutil

def getAllFilePaths(path):
    a = os.listdir(path)
    l = 0
    while l < len(a):
        a[l] = path + "\\" + a[l]
        l += 1

    j = 0
    while j < len(a):
        try:
            if "." not in a[j]:
                b = os.listdir(a[j])
                l = 0
                while l < len(b):
                    b[l] = a[j] + "\\" + b[l]
                    l += 1
                for c in b:
                    a.append(c)
                a.remove(a[j])
        except:
                try:
                    print(a[j] + " failed")
                except:
                    print("Something failed and failed to print")
                a.remove(a[j])
                j += 1
            if(j == len(a)):
                for d in a:
                    if "." not in d:
                        j = 0
    
    print(a)
    return(a)


def compareOldDirToNew(oldDir, newDir):
    #Specialized in only finding items that are NOT in the new dir
    files = []
    #found = 0
    #for a in oldDir:
    #    old = a.split('\\')
     #   for b in newDir:
     #       new = b.split('\\')
    #        if old[len(old)- 1] in new[len(new)- 1]:
     #           found = 1
     #   if found == 0:
     #       files.append(a)
    #return files

    #get to the base directory
    print('olddir: ' + oldDir[0])
    print('newdir: ' + newDir[0])
    print('remove this from old dir strings to compare to newdir ex:')
    print('old: C:\\Users\\Mike\\Desktop\\olddir\\text.txt')
    print('remove: C:\\Users\\Mike\\Desktop\\olddir')
    print('remove this from old dir')
    print('PLEASE USE \ instead of \\')
    removeOld = input()
    print('remove this from new dir')
    removeNew = input()

    #removeOld.replace("\\" , r'\')
    #removeNew.replace("\\" , r'\')
                      
    i = 0
    while i < len(oldDir):
        oldDir[i] = oldDir[i].replace(removeOld, "", 1)
        i += 1

    i = 0
    while i < len(newDir):
        newDir[i] = newDir[i].replace(removeNew, "", 1)
        i += 1 

    print(oldDir)
    print(newDir)
    for a in oldDir:
        if a not in newDir:
            files.append(a)
    return files
        
                
                
    

print('oldPath:')
oldPath = input()
print('newPath:')
newPath = input()

oldDir = getAllFilePaths(oldPath)
newDir = getAllFilePaths(newPath)

missing = compareOldDirToNew(oldDir, newDir)
print('missing')
print(missing)

