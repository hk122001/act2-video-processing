import skvideo
import matplotlib.pyplot as plt
import cv2
import json

import os

#MAKE SURE TO SET PATH OF THE FFMPEG MODULE.
ffmpeg_path = "C:/Users/USER/Downloads/ffmpeg-2023-04-26-git-e3143703e9-essentials_build/bin/"
skvideo.setFFmpegPath(ffmpeg_path)

import skvideo.io
import skvideo.datasets

from skimage import data, color
from skimage.transform import rescale, resize, downscale_local_mean

videodata = skvideo.io.vread("meatthezoo.mp4")

def module1():
    print("module1 reached")
    framesToCalc = [int(len(videodata)/12)-1, int((len(videodata)/12)*2)-1, int((len(videodata)/12)*3)-1, int((len(videodata)/12)*4)-1, int((len(videodata)/12)*5)-1, int((len(videodata)/12)*6)-1, int((len(videodata)/12)*7)-1, int((len(videodata)/12)*8)-1, int((len(videodata)/12)*9)-1, int((len(videodata)/12)*10)-1, int((len(videodata)/12)*11)-1, int(len(videodata))-1]
    
    archName = "frames"
    with open(archName, "w") as f:
        json.dump(framesToCalc, f)

    #PIPE
    module2(archName)

def module2(archName):
    print("module2 reached")
    with open(archName, "r") as f:
        framesToCalc = json.load(f)
    
    os.remove(archName)
        
    def grab_frame(index):
        frame = videodata[index]
        return cv2.cvtColor(frame,cv2.COLOR_RGB2RGBA)

    images = []
    for i in framesToCalc:
        image = image = grab_frame(i)
        image_resized = resize(image, (256, 256))
        images.append(image_resized.tolist())

    archName = "resizedImages"
    with open(archName, "w") as f:
        json.dump(images, f)
    
    #PIPE
    module3(archName)

def module3(archName):
    print("module3 reached")
    with open(archName, "r") as f:
        images = json.load(f)

    os.remove(archName)
    
    fig, axes = plt.subplots(4, 3, figsize=(8, 8))
    ax = axes.ravel()
    for i in range(12):
        ax[i].imshow(images[i])
        ax[i].axis("off")
    fig.tight_layout()
    
    #PIPE
    module4()

def module4():
    print("module4 reached")
    plt.savefig("output.png")
    plt.show()

module1()
