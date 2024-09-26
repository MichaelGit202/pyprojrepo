import os
from PIL import Image
direct = os.getcwd() + "\images"
filelist = []
#2do
#1st image of the stack determins the resolution and how the frames are stretched
#I take advantage of that with the 'average image'
def FrameGeneration(images, framelen):
    TotalImages = 1
    arraylength = 10 #I was going to make this dynamic but I don't think im gona have 10
    name = ""        #billion photos any time soon
    for a in range(0,len(images)):
        for b in range(0, framelen):
              image = Image.open(images[a])
              temp = image.size
              if yrn != "y":
                  if (temp[0] % 2) > 0:
                        temparr = list(temp) 
                        temparr[0] = temparr[0] - 1
                        temp = tuple(temparr)
                  if (temp[1] % 2) > 0:
                        temparr = list(temp) 
                        temparr[1] = temparr[1] - 1
                        temp = tuple(temparr)
                  
              image = image.resize(temp, resample=0, box=None)
              rgb_im = image.convert("RGB")
              name = str(TotalImages)
              print(str(int(name) + 1) + "/" + str(len(images) * framelen))

              for c in range(0, arraylength - len(str(TotalImages))):
                  name = "0" + name
                  
              rgb_im.save(os.getcwd() + "\\tempImages\\"  + name +".jpg")
              del(rgb_im)
              TotalImages += 1
    return str(name)

    
def Rendervid(lframe):
    import ffmpeg
    (
        ffmpeg
        .input(os.getcwd() + '/tempImages/%0'+ str(len(lframe)) + 'd.jpg', framerate=fps)
        .output('movie.mp4')
        .run()
    )


def averageSize(filelist):
    #smallest
    smallestWidth = 9999999
    smallestHeight = 9999999
    biggestWidth = -1
    biggestHeight = -1
    for a in filelist:
        image = Image.open(a)
        temp = image.size
        if temp[0] < smallestWidth:
            smallestWidth = temp[0]
        if temp[1] < smallestHeight:
            smallestHeight = temp[1]
    #biggest
    for a in filelist:
        image = Image.open(a)
        temp = image.size
        if temp[0] > smallestWidth:
            biggestWidth = temp[0]
        if temp[1] > smallestHeight:
            biggestHeight = temp[1]
    avgerage  = [int((biggestWidth + smallestWidth)/2), int((smallestHeight + biggestHeight)/2)]
    return avgerage

for root, dirs, files in os.walk(direct):
    for file in files:
        filelist.append(os.path.join(root,file))
print("length per frame[frames out of 60]")
framelen = input()
fps = 60
sz = []
print("use averaging teqnique? y or n")
yrn = input()
if yrn == "y":
    print(averageSize(filelist))
    sz = tuple(averageSize(filelist))
    if (sz[0] % 2) > 0:
        sc = list(sz)
        sc[0] += 1
        sz = tuple(sc)
    if (sz[1] % 2) > 0:
        sc = list(sz)
        sc[0] += 1
        sz = tuple(sc)
    img  = Image.new(mode = "RGB", size = sz)
    img.save(os.getcwd() + "\\tempImages\\"  + "0000000000" +".jpg")
else:
    print("Do you want to set a custom proportions for all? y or n")
    yn = input()
    if yn == "y":
        sd = [1920,1080]
        sd = list(sd)
        print("Width:")
        sd[0] = int(input())
        print("Height")
        sd[1] = int(input())
        if ((sd[0] % 2) > 0):
            sd[0] += 1
        if ((sd[1] % 2) > 0):
            sd[1] += 1

        sz = tuple(sd)
        print(sd)
    img  = Image.new(mode = "RGB", size = sz)
    img.save(os.getcwd() + "\\tempImages\\"  + "0000000000" +".jpg")
lframe = FrameGeneration(filelist, int(framelen))
Rendervid(lframe)
dir = os.getcwd() + "\\tempImages\\"
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))



        


