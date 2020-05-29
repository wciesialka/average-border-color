from PIL import Image
import argparse

def average_border_color(img:Image,border_size:int):
    """
    Calculate average color image's border.

    Calculate average color of the n outside pixels on image.

    Parameters:
        img (PIL.Image): Image to process
        border_size (int): Width of border

    Returns:
        average_color (tuple): Average color of outside pixels.
    """
    img = img.convert('RGBA')
    size = img.size
    w = size[0]
    h = size[1]
    maxdim = max(*size)
    mindim = min(*size)
    if(border_size > (mindim//2)):
        raise ValueError(f"Border size ({border_size}) cannot be larger than half the minimum dimension of an image ({mindim//2}).")
    n = 0
    r = 0
    g = 0
    b = 0
    a = 0
    for offset in range(border_size):
        # top/bottom
        for x in range(w):
            # top
            y = offset
            px = img.getpixel((x,y))
            r += px[0]
            g += px[1]
            b += px[2]
            a += px[3]
            # bottom
            
            y = h-1-offset
            px = img.getpixel((x,y))
            r += px[0]
            g += px[1]
            b += px[2]
            a += px[3]

            n += 2
        # left/right
        for y in range(r+1,h-(r+1)): # don't get the corners
            # left
            px = img.getpixel((r,y))
            r += px[0]
            g += px[1]
            b += px[2]
            a += px[3]
            # right
            px = img.getpixel((w-1-r,y))
            r += px[0]
            g += px[1]
            b += px[2]
            a += px[3]

            n += 2

    return (r//n,g//n,b//n,a//n)

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Get the average color of the outside pixels on an image.")
    parser.add_argument("-s","--size",type=int,dest="border_size",default=1,required=False,help="Border size.")
    parser.add_argument("image",type=argparse.FileType("rb"),help="Image to process.")
    args = parser.parse_args()
    img = Image.open(args.image)
    avg = average_border_color(img=img,border_size=args.border_size)
    args.image.close()
    print(avg)
    
