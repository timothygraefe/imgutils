#!/usr/bin/python3

import numpy as np
import json
import argparse
from PIL import Image

iconFormats = 'IconFormats.json'
jsonContentsFile = 'Contents.json'

def resize_image(img, basefile, oheight, owidth, newdpi, commit=False, verbose=False):

    # The size of the base image should be larger than the output size
    print('Input image size: width: {} height: {}'.format(img.size[0], img.size[1]))
    print('Input image file format: {}'.format(img.format))

    if verbose :
        print('Using input file {} with format  {}: '.format(img.filename, img.format))
        print('Using input file {} with mode    {}: '.format(img.filename, img.mode))
        print('Using input file {} with size    {}: '.format(img.filename, img.size))
        print('Using input file {} with DPI     {}: '.format(img.filename, img.info['dpi']))
        print('Using input file {} with palette {}: '.format(img.filename, img.palette))

    # Generate new file name, e.g.: myicon_iphone_29x29.png
    newfile = '{}_{}x{}.{}'.format(basefile, owidth, oheight, img.format.lower())

    print('New image file name: {}'.format(newfile))
    if not commit:
        print('Afraid to commit ...')
        return

    # Sampling options for resizing the image:
    #   PIL.Image.NEAREST (use the nearest neighbor)  -- DEFAULT
    #   PIL.Image.BILINEAR (linear interpolation)
    #   PIL.Image.BICUBIC (cubic spline interpolation)
    #   PIL.Image.LANCZOS (a high-quality downsampling filter)
    # Just using the default for now.
    resizedImage = img.resize((owidth, oheight))

    print('Saving new image file: {}'.format(newfile))
    if newdpi == 0:
        resizedImage.save(newfile)
    else:
        resizedImage.save(newfile, dpi=(newdpi, newdpi))

def main():
    parser = argparse.ArgumentParser(description='Image Crop')
    parser.add_argument('imgfile', metavar='imgfile', nargs=1, type=str, help='Image file')
    parser.add_argument('-b', metavar='basefile', nargs=1, type=str, help='Base output file name')
    parser.add_argument('-s', metavar='start', nargs=2, type=int, help='Crop start point')
    parser.add_argument('-e', metavar='end', nargs=2, type=int, help='Crop end point')
    parser.add_argument('-C', action='store_true', default=False, help='Commit the changes')
    parser.add_argument('-V', action='store_true', default=False, help='Verbose mode')
    args = parser.parse_args()

    verbose = (args.V == True) or False
    commit  = (args.C == True) or False

    imgfile = args.imgfile[0]

    try:
        img = Image.open(imgfile)

    except FileNotFoundError:
            print('Could not open base file {}'.format(imgfile))

    print('Using input image file: {}'.format(imgfile))

    if(args.b != None):
        basefile = args.b[0]
    else:
        basefile = imgfile.split('.')[0]

    if(args.s != None):
        oheight = args.H[0]
        print('Output file height: {}'.format(oheight))
    else:
        oheight = img.size[0]
        print('Using input file for height: {}'.format(height))

    if(args.W != None):
        owidth = args.W[0]
        print('Output file width: {}'.format(owidth))
    else:
        owdidth = img.size[1]
        print('Using input file for width: {}'.format(owdith))

    if(args.D != None):
        dpi = args.D[0]
        print('Output file DPI: {}'.format(dpi))
    else:
        dpi = 0

    resize_image(img, basefile, oheight, owidth, dpi, commit, verbose)

### ### ### ### ### ### ### ### 
if __name__ == '__main__':
    main()

