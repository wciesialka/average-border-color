from PIL import Image
import argparse

def main(img:Image,border_size:int):
    """
    Calculate average color image's border.

    Calculate average color of the n outside pixels on image.

    Parameters:
        img (PIL.Image): Image to process
        border_size (int): Width of border
    """
    pass

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Get the average color of the outside pixels on an image.")
    parser.add_argument("-s","--size",type=int,default=1,required=False,help="Border size.")
    parser.add_argument("image",type=argparse.FileType("rb"),required=True,help="Image to process.")
    args = parser.parse_args()
    img = Image.open(args.image)
    args.image.close()
    main(img=img,border_size=args.size)
    
