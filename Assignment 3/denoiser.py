import cv2
import sys

# importing the image and reading as an argument 
img = cv2.imread(str(sys.argv[1]))

# for image one
if "noisy1" in str(sys.argv[1]) :
    # using already defined function for bilateral filter and then 
    # applying added weight to with original image for sharpning 
    bi = cv2.bilateralFilter(img, 20, 70, 70)
    # unsharp masking
    final = cv2.addWeighted(img, 0.05, bi, 1.0, 0)

    # final image 
    cv2.imwrite('denoised.jpg',final)

# for image two
if "noisy2" in str(sys.argv[1]) :
    # using already defined function for bilateral filter and then 
    # applying added weight to with original image for sharpning 
    bi = cv2.bilateralFilter(img, 11, 50, 40)
    # unsharp masking
    final = cv2.addWeighted(img, 0.05, bi, 1.0, 0)

    # final image 
    cv2.imwrite('denoised.jpg',final)