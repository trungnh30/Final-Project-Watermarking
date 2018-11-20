import argparse
from gooey import Gooey, GooeyParser
import cv2 as cv
import numpy as np
import math

def psnr(img1,img2):
    image1=cv.imread(img1)
    image2=cv.imread(img2)
    mse = np.mean((np.subtract(image2, image1))**2)
    sqrtmse=math.sqrt(mse)
    #psnr
    psnr = 20*math.log10(255/sqrtmse)
    print('Giá trị PSNR là: %s' %(round(psnr,2)))
    return psnr
@Gooey(
       show_config=True,          # skip config screens all together
       default_size=(610, 530),   # starting size of the GUI
       program_name='Tính toán PSNR', # Defaults to script name
       image_dir='C:/Users/Trung/Desktop/steganography-master[PRODUCT]/icon')       #Icon for the program

def main():
    # Construct the argument parse and parse the arguments
    #ap = argparse.ArgumentParser()
    ap = GooeyParser(description="Nguyễn Hoàng Trung - D9DTVT")
    ap.add_argument("--input_image1", type=str, required=True, help="Đầu vào ảnh gốc", widget='FileChooser')
    ap.add_argument("--input_image2", type=str, required=False, help="Đầu vào ảnh cần so sánh", widget='FileChooser')
    args = ap.parse_args()
    psnr(args.input_image1,args.input_image2)
if __name__ == "__main__":
    main()