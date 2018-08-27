from selenium import webdriver
#import cv2
from PIL import Image
import sys
import os
import re

driver = webdriver.PhantomJS()
driver.set_window_size(1922, 1922)
driver.get('http://localhost:80/cgi-bin/polyline/polyline.py')
driver.save_screenshot('/var/www/html/polyline.png')
driver.close()


quality = 100
input_path = '/var/www/html/polyline'
output_path = '/var/www/html/polyline' + str(quality)

input_im = Image.open(input_path + ".png")
rgb_im = input_im.convert('RGB')
rgb_im.save(output_path + ".jpg",quality=quality)
