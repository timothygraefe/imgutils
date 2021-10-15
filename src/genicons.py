#!/usr/bin/python3

import numpy as np
import json
import argparse
from PIL import Image

iconFormats = 'IconFormats.json'
jsonContentsFile = 'Contents.json'

def create_icons(img, basefile='test', verbose=False, writeIcons=False, writeJson=False, fmtFile=iconFormats):
    # Create a dictionary that will be used to generate the JSON file.
    # Read the icon formats from JSON file:
    contents = {}
    contents['images'] = []

    # The size of the base image must be 1024 x 1024
    if(img.size != (1024, 1024)):
        print('Base image must be 1024x1024')
        return

    if(img.format != 'PNG'):
        print('Base image file format must be PNG')
        return

    if(verbose):
        print('Using input file {} with format  {}: '.format(img.filename, img.format))
        print('Using input file {} with mode    {}: '.format(img.filename, img.mode))
        print('Using input file {} with size    {}: '.format(img.filename, img.size))
        print('Using input file {} with palette {}: '.format(img.filename, img.palette))

    # Open a file with all the required icon formats.
    with open(fmtFile) as json_file:
        print('Loading JSON icon formats file: {}'.format(fmtFile))
        imgformats = json.load(json_file)
        for imgformat in imgformats['images']:
            idiom =   imgformat['idiom']
            scale =   imgformat['scale']
            sizestr = imgformat['size']
            pxscale = imgformat['pxscale']
            pxsize =  imgformat['pxsize']

            if(verbose):
                print('idiom:    ' + idiom)
                print('scale:    ' + scale)
                print('size:     ' + sizestr)
                print('pxscale:  ' + str(pxscale))
                print('pxsize:   ' + str(pxsize))
                print('')

            # Calculate the size in pixels.
            size = int(pxscale * pxsize)

            # Generate new file name, e.g.: myicon_iphone_29x29.png
            newfile = '{}_{}_{}x{}.png'.format(basefile, idiom, size, size)

            # For each icon format, take the base image and resize accordingly.
            # Sampling options for resizing the image:
            #   PIL.Image.NEAREST (use the nearest neighbor)  -- DEFAULT
            #   PIL.Image.BILINEAR (linear interpolation)
            #   PIL.Image.BICUBIC (cubic spline interpolation)
            #   PIL.Image.LANCZOS (a high-quality downsampling filter)
            # Just using the default for now.
            resizedImage = img.resize((size, size))
            contents['images'].append(
            {
                'filename' : newfile,
                'idiom'    : idiom,
                'scale'    : scale,
                'size'     : sizestr
            })

            # Save the new icon image files.
            if(writeIcons):
                print('Saving new icon image file: {}'.format(newfile))
                resizedImage.save(newfile)
            else:
                print('Generated new icon image: {}'.format(newfile))

    if(writeJson):
        # The JSON file has a special suffix for author and version info.
        contents['info'] = { 'author' : 'xcode', 'version' : 1 }
        print('Generating JSON file {}'.format(jsonContentsFile))
        with open(jsonContentsFile, 'w') as outfile:
            json.dump(contents, outfile, indent=2)

def main():
    parser = argparse.ArgumentParser(description='PNG Image Scaler')
    parser.add_argument('imgfile', metavar='imgfile', nargs=1, type=str, help='Image file')
    parser.add_argument('-b', metavar='basefile', nargs=1, type=str, help='Base output file name')
    parser.add_argument('-i', metavar='iconfmts', nargs=1, type=str, help='Icon formats JSON file')
    parser.add_argument('-V', action='store_true', default=False, help='verbose mode')
    parser.add_argument('-D', action='store_true', default=False, help='display input image')
    parser.add_argument('-W', action='store_true', default=False, help='write output images')
    parser.add_argument('-J', action='store_true', default=False, help='write output JSON file')
    args = parser.parse_args()

    verbose     = (args.V == True) or False
    show_image  = (args.D == True) or False
    write_icons = (args.W == True) or False
    write_json  = (args.J == True) or False

    imgfile = args.imgfile[0]

    if(args.b != None):
        basefile = args.b[0]
    else:
        print('Missing base file name')
        exit()

    if(args.i != None):
        fmtsFile = args.i[0]
    else:
        fmtsFile = iconFormats

    try:
        img = Image.open(imgfile)

    except FileNotFoundError:
            print('Could not open base file {}'.format(imgfile))

    print('Using base image file: {}'.format(imgfile))

    create_icons(img, basefile, verbose, write_icons, write_json, fmtsFile)
    if(show_image):
        img.show()

### ### ### ### ### ### ### ### 
if __name__ == '__main__':
    main()

