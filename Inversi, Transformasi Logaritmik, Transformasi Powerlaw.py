import numpy as np #library untuk numpy
import cv2 #library untuk image io
import matplotlib.pyplot as plt #library untuk matplotlib

img = cv2.imread("Rizki.jpg")#fungsi untuk memanggil gambar dari library opencv
img_height = img.shape[0] #tinggi gambar
img_width = img.shape[1] #lebar gambar
img_channel = img.shape[2] #channel gambar
img_inversi = np.zeros(img.shape, dtype=np.uint8)
def inversi_grayscale(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = nilai - gray
            img_inversi[y][x] = (gray, gray, gray)
def inversi_rgb(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            red = nilai - red
            green = img[y][x][1]
            green = nilai - green
            blue = img[y][x][2]
            blue = nilai - blue
            img_inversi[y][x] = (red, green, blue)
inversi_grayscale(255)
plt.imshow(img_inversi)
plt.title("Inversi Grayscale")
plt.show()

inversi_rgb(255)
plt.imshow(img_inversi)
plt.title("Inversi RGB")
plt.show()
#Membuat variabel img_log untuk menampung hasil
img_log = np.zeros(img.shape, dtype=np.uint8)
def log(c):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = int(c * np.log(gray + 1))
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            img_log[y][x] = (gray, gray, gray)
log(30)
plt.imshow(img_log)
plt.title("Log")
plt.show()
#fungsi untuk Inversi & Log
#menambah variabel untuk inversi log
img_inlog = np.zeros(img.shape, dtype=np.uint8)
#fungsi untuk inversi log
def inlog(c):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = int(c * np.log(255 - gray + 1))
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            img_inlog[y][x] = (gray, gray, gray)
inlog(30)
plt.imshow(img_inlog)
plt.title("Inversi & Log")
plt.show()
#fungsi untuk nth power
img_nthpower = np.zeros(img.shape, dtype=np.uint8)
def nthpower(c, y):
    thc = c / 100
    thy = y / 100
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = int(thc * pow(gray, thy))
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            img_nthpower[y][x] = (gray, gray, gray)
nthpower(50, 100)
plt.imshow(img_nthpower)
plt.title("Nth Power")
plt.show()
#fungsi untuk nth Root power
img_nthrootpower = np.zeros(img.shape, dtype=np.uint8)
def nthrootpower(c, y):
    thc = c / 100
    thy = y / 100
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = int(thc * pow(gray, 1./thy))
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            img_nthpower[y][x] = (gray, gray, gray)
nthrootpower(50, 100)
plt.imshow(img_nthrootpower)
plt.title("Nth Root Power")
plt.show()