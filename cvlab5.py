import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('input_img.jpg',cv2.IMREAD_GRAYSCALE)
if img is None:
    print("Error: Image not found.")
else:
    print("Image Loaded Successfully")
    plt.figure(figsize=(10,6))
    plt.subplot(3,3,1)
    plt.imshow(img,cmap='gray')
    plt.title('Original Grayscale Image')
    plt.axis('off')
    plt.subplot(3,3,2)
    