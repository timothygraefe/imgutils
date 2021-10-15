#!/usr/bin/python3

import numpy as np
import os
import sys
import argparse
from PIL import Image


def main():
    supported_formats = [ 'jpg', 'jpeg', 'png' ]

    parser = argparse.ArgumentParser(description='File format converter')
    parser.add_argument('imgfile', metavar='imgfile', nargs=1, type=str, help='Input image file')
    parser.add_argument('-F', metavar='format', nargs=1, type=str, help='Output file format [jpg|jpeg|png]')
    parser.add_argument('-V', action='store_true', default=False, help='verbose mode')
    args = parser.parse_args()

    verbose     = (args.V == True) or False

    imgfile = args.imgfile[0]

    if(os.path.exists(imgfile)):
        fparts = imgfile.split('.')
        base = fparts[0]
        ifmt = fparts[1].lower()
        print('Input file: base {} ifmt {}'.format(base, ifmt))
        if(not ifmt in supported_formats):
            print('Unsupported input file format')
            exit()

    if(args.F != None):
        ofmt = str(args.F[0]).lower()
        if(not ofmt in supported_formats):
            print('Unsupported output file format')
            exit()
    else:
        print('Missing output file format')
        exit()

    ofile = base + '.' + ofmt

    if(ifmt == ofmt):
        print('Input and output file formats are the same')
        exit()

    try:
        img = Image.open(imgfile)
    except FileNotFoundError:
            print('Could not open input file {}'.format(imgfile))

    print('Using input image file: {}'.format(imgfile))
    print('Converting file from {} to {}'.format(ifmt, ofmt))
    print('Input file: {} Output file: {}'.format(imgfile, ofile))

    rgb_im = img.convert('RGB')
    rgb_im.save(ofile)


### ### ### ### ### ### ### ### 
if __name__ == '__main__':
    main()

