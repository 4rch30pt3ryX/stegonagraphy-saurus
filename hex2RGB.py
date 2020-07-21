#!usr/bin/env python3

"""
hexadecimal to RGB converter that takes sets of three and reverses them to
feed back out as hex RBG values as needed to appear as a string in a
bitmap file.
"""

import binascii

def bamf():
    baInput = input('to be converted: ')
    # convert to bytes, convert to Hex
    baski = bytes(baInput, encoding='utf-8')
    hexit = binascii.hexlify(baski)
    hexed = str(hexit)
    # split string to get rid of "b'%'"
    a,b,c = (hexed.split("'"))
    print(b)

    # adds padding to create even triads
    while len(b) % 6 != 0:
        b += '00'
        print(b)
    global rightStuff
    rightStuff = []
    
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
    print(rightStuff)

def rgbBgr():
    # convert hexidecimal RGB representation to RGB values
    for item in rightStuff:
        rgb = tuple(int(item[i:i+2], 16) for i in (0, 2, 4))
        print(rgb)   
    
bamf()
rgbBgr()
