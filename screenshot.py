from selenium import webdriver

driver = webdriver.PhantomJS()
driver.set_window_size(1024, 768)
driver.get('http://localhost:80/cgi-bin/polyline.py')
driver.save_screenshot('polyline.png')
driver.close()
