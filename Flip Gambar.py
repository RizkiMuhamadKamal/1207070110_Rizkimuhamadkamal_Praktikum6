import numpy as np #library untuk numpy
import cv2  #library untuk Open CV
import matplotlib.pyplot as plt #library untuk matplotlib

img = cv2.imread("Rizki.jpg")

img_height = img.shape[0] #tinggi gambar
img_width = img.shape[1] #lebar gambar
img_channel = img.shape[2] #channel gambar
img_type = img.dtype #tipe gambar

img_flip_horizontal = np.zeros(img.shape, img_type) #fungsi untuk variabel flip horizontal
img_flip_vertical = np.zeros(img.shape, img_type) #fungsi untuk variabel flip vertical
#fungsi untuk membalik gambar secara horizontal
for y in range(0, img_height):
    for x in range(0, img_width):
        for c in range(0, img_channel):
            img_flip_horizontal[y][x][c] = img[y][img_width-1-x][c]
#fungsi untuk membalik gambar secara vertical
for y in range(0, img_height):
    for x in range(0, img_width):
        for c in range(0, img_channel):
            img_flip_vertical[y][x][c] = img[img_height-1-y][x][c]
plt.imshow(img_flip_horizontal) #fungsi untuk memanggil gambae secara horizontal
plt.title("Flip Horizontal") #fungsi untuk memberi judul
plt.show() #fungsi untuk menampilkan gambar
plt.imshow(img_flip_vertical) #fungsi untuk memanggil gambae secara horizontal
plt.title("Flip Vertical")  #fungsi untuk memberi judul
plt.show() #fungsi untuk menampilkan gambar
