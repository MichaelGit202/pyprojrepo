from moviepy.editor import *
from moviepy.editor import VideoFileClip, concatenate_videoclips
from PIL import Image
from resizeimage import resizeimage
import os
from natsort import natsorted
import gc
print(Image.__file__)
direct = os.getcwd() + "\images"
filelist = []
batch = 100
print("Enter Batch size //reccomended 100//")
batch = int(input())
print("name")
name = input()

#do NOT run this from IDLE because the progress bar likes to slow down the
#whole damn program because it feels like it

for root, dirs, files in os.walk(direct):
    for file in files:
        filelist.append(os.path.join(root,file))


filelistsort = natsorted(filelist,reverse=False)

#convert to jpg  ---Dumb because it is
#scuffed = 0
#for a in filelistsort:
 #   image = Image.open(a)
  #  rgb_im = image.convert("RGB")
   # rgb_im.save(a + ".jpg")
   # os.remove(a)
    #filelistsort[scuffed] = a + ".jpg"  #I dont know why this crashes my pc
   # scuffed += 1
    


#get lowest size image
for a in filelistsort:
    image = Image.open(a)
    temp = image.size
    smallestWidth = 9999999
    smallestHeight = 9999999
    if temp[0] < smallestWidth:
        smallestWidth = temp[0]
    if temp[1] < smallestHeight:
        smallestHeight = temp[1]
print(smallestWidth)
print(smallestHeight)

#mabey a better way would be to
# calculate how many frames of each image you'd need and make that many copies
# use ffmpeg to make a whole ass video out of that
    

#videolist = [ImageClip(m).set_duration(.2
          #                             )
            # for m in filelistsort]




#Batch 
tempvidlst = []
videolist = []
j = 0
m = 0
while j < len(filelistsort):
    videolist.append(ImageClip(filelistsort[j]).set_duration(.2))
    print(j)
    print(m)
    if m == batch:
        fps = 60
        concat_clip = concatenate_videoclips(videolist, method="compose")
        concat_clip.write_videofile(os.getcwd() + "/tempvid" + str(j) +".mp4", fps=fps)
        tempvidlst.append(os.getcwd() + "/tempvid" + str(j) +".mp4")
        del videolist[:]
        videolist  = []
        m = 0
        gc.collect()
    j += 1
    m += 1




fps = 60
concat_clip = concatenate_videoclips(tempvidlst, method="compose") #<- cool stuff when method='chain' 
concat_clip.write_videofile("test.mp4", fps=fps)
