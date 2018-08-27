from selenium import webdriver
import cv2

driver = webdriver.PhantomJS()
driver.set_window_size(1922, 1922)
driver.get('http://localhost:80/cgi-bin/polyline/polyline.py')
driver.save_screenshot('/var/www/html/polyline.png')
driver.close()



rate = 9
compression_params = [int(cv2.IMWRITE_PNG_COMPRESSION), rate]
img = cv2.imread('/var/www/html/polyline.png', cv2.IMREAD_UNCHANGED)
#cv2.imwrite('/var/www/html/polyline' + str(rate) + '.png', img, compression_params)
cv2.imwrite('/var/www/html/polyline.png', img, compression_params)
