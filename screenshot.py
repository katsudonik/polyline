from selenium import webdriver

driver = webdriver.PhantomJS()
driver.set_window_size(1922, 1922)
driver.get('http://localhost:80/cgi-bin/polyline/polyline.py')
driver.save_screenshot('/var/www/html/polyline.png')
driver.close()
