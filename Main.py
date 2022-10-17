import requests
import shutil
import os
from  random import randint


def setUp():
    xs =0
    start=input("\twant to start wordle (yes or no):")
    while xs==0:
        if start =="yes":
            xs=1
        elif start == "no":
            xs=1
        else:
            start=input("\twant to start wordle (yes or no):")
    return start

def selectType():
    imgType = input("\t1.download Random Image\n\t2.Download Custome Image\n\t enter 1 or 2 :-")
    if imgType == '1':
        image_url = "https://picsum.photos/400"
    elif imgType == '2':
        image_url = input("enter Image URL to Donwload")
    else :
        print("Wrong Input Try Again")
        exit()
    return image_url



def downImg():
        imgNum =randint(0,100);
        filename = "Image_"+str(imgNum)+".jpg"
        r = requests.get(selectType(), stream = True)
        if r.status_code == 200:
            r.raw.decode_content = True
            with open(filename,'wb') as f:
                shutil.copyfileobj(r.raw, f)   
            print('Image sucessfully Downloaded: ',filename)
        else:
            print('Image Couldn\'t be retreived')


if setUp() == "yes":
    downImg()
