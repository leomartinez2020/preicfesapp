from PIL import Image

def resize_image(imgfile, destination, quality):
    """ Dowsizes image for performance """
    foo = Image.open(imgfile)
    foo.save(destination, optimize=True, quality=quality)
