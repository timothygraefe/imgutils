# imgutils
Basic command line utilities to invoke PIL

1) src/genicons
  - Generate a set of 29 icon image files and JSON file needed for iOS application icons, based on an original PNG file:
  - Command "help" output:
usage: genicons.py [-h] [-b basefile] [-i iconfmts] [-V] [-D] [-W] [-J] imgfile

PNG Image Scaler

positional arguments:
  imgfile      Image file

optional arguments:
  -h, --help   show this help message and exit
  -b basefile  Base output file name
  -i iconfmts  Icon formats JSON file
  -V           verbose mode
  -D           display input image
  -W           write output images
  -J           write output JSON file

2) src/resize_image.py
  - Resize an image at the command line
  - Command "help" output:
usage: resize_image.py [-h] [-b basefile] [-H height] [-W width] [-D DPI] [-Q quality] [-C] [-V] imgfile

PNG Image Resize

positional arguments:
  imgfile      Image file

optional arguments:
  -h, --help   show this help message and exit
  -b basefile  Base output file name
  -H height    Output file height
  -W width     Output file width
  -D DPI       Output file DPI
  -Q quality   Output file quality
  -C           Commit the changes
  -V           Verbose mode

3) src/convert_images.py
  - Convert image file format
  - Command "help" output:
usage: convert_images.py [-h] [-F format] [-V] imgfile

File format converter

positional arguments:
  imgfile     Input image file

optional arguments:
  -h, --help  show this help message and exit
  -F format   Output file format [jpg|jpeg|png]
  -V          verbose mode

4) src/crop_image.py
  - Crop an image file
  - Command "help" output:
usage: crop_image.py [-h] [-b basefile] [-s start start] [-e end end] [-C] [-V] imgfile

Image Crop

positional arguments:
  imgfile         Image file

optional arguments:
  -h, --help      show this help message and exit
  -b basefile     Base output file name
  -s start start  Crop start point
  -e end end      Crop end point
  -C              Commit the changes
  -V              Verbose mode

