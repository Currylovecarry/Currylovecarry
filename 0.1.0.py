# opencv-python
import cv2
import cv2 as cv
# mediapipe人工智能工具包
import mediapipe as mp
# 导入python绘图matplotlib
import matplotlib.pyplot as plt
#读取图像
img = cv.imread('curry.jpeg', 0)
#显示图像
cv.imshow('Original', img)
cv2.waitKey(0)
#在matplotlib
plt.imshow(img,cmap='gray')

