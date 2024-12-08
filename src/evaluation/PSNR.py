 
from math import log10, sqrt 
import cv2 
import numpy as np 


def PSNR(original, compare_image): 
    mse = np.mean((original - compare_image) ** 2) 
    if(mse == 0):  # MSE is zero means no noise is present in the signal . 
                  # Therefore PSNR have no importance. 
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse)) 
    return psnr

def main(): 
     original_path = "../../data/original/image"
     compare_path = "../../results/regular_upsample/image"
     for i in range(3):
        original_img_path = original_path + str(i+1) + ".jpg"
        compare_img_path = compare_path + str(i+1) + ".jpg"

        original_image = cv2.imread(original_img_path)
        compare_image = cv2.imread(compare_img_path)
        
        value = PSNR(original_image, compare_image)
        print(f"PSNR value for image{i+1}: {value} dB")
        #higher the value of PSNR, the better is the quality of the image. (out of 100)
       
if __name__ == "__main__": 
    main()