#!usr/bin/env python3

"""
hexadecimal to RGB converter that takes sets of three and reverses them to
feed back out as hex RBG values as needed and then injects the command into the .bmp
per pixel.
 ***Requires PIL/Pillow module***
Intent for this version is to accept multiple commands as arguments and
separate them with LF (line feed) and CR (carriage return) ascii characters.
argv[1] = number of individual commands needed
example "C:\>$  python img_FUN_002.py 2" will allow dfor 2 unique commands
"""

import binascii
from PIL import Image
from sys import argv

def howMany():
    global allCmd
    global path
    multiCmd = []
    amt = int(argv[1])
    path = str(argv[2])
    while amt != 0:
        bamf()
        amt -= 1
        multiCmd.append(rightStuff)
    print(multiCmd)
    allCmd = []
    for subList in multiCmd:
        for item in subList:
            allCmd.append(item)
    print(allCmd)
              
def bamf():
    baInput = input('to be converted: ')
    # convert to bytes, convert to Hex
    baski = bytes(baInput, encoding='utf-8')
    hexit = binascii.hexlify(baski)
    hexed = str(hexit)
    # split string to get rid of "b'%'"
    a,b,c = (hexed.split("'"))
    
    # adds padding to create even triads
    while len(b) % 6 != 0:
        b += '00'
        print(b)
    global rightStuff
    rightStuff = []
    # These two appended hex rbg codes add a Carriage Return and Line Feed to
    # indicate the following data is handled separately in a new command
    rightStuff.append('0A0000')
    rightStuff.append('0D0A0D')
    while len(b) != 0:
        # grabbing each pair for the triad
        revitA = b[0:2]
        revitB = b[2:4]
        revitC = b[4:6]
        revIt = revitC+revitB+revitA
        rightStuff.append(revIt)
        # splits string to process the next triad
        revitS = revitA+revitB+revitC
        d, b = b.split(revitS)
    rightStuff.append('000000')
    return rightStuff

def rgbBgr():
    # convert hexidecimal RGB representation to RGB values
    global rgbList
    rgbList = []
    for item in allCmd:
        rgb = tuple(int(item[i:i+2], 16) for i in (0, 2, 4))
        rgbList.append(rgb)
    print(rgbList)

def convert():
    # insert command as pixels in the bmp file
    try:
        img = Image.open(path)
    except IOError as msg:
        print(msg)

    # This plants the commands at the beginning so CLi doesn't choke
    # on all the bitmap junk
    maxY = img.size[1:]
    for i in maxY:
        yMax = i
    x = 0; y = yMax - 1    
    for item in rgbList:
        img.putpixel( (x,y), item)
        x += 1
    img.save(path)
    
howMany()
rgbBgr()
convert()
