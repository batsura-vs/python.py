from time import sleep

from selenium import webdriver
browser = webdriver.Firefox()
browser.get("https://www.pythonanywhere.com ")
d = browser.find_element_by_class_name("login_link")
d.click()
s = browser.find_element_by_name("auth-username")
s.click()
s.send_keys('misha492')
c = browser.find_element_by_name("auth-password")
sds = open('/home/vova492/py.txt','r+')
c.send_keys(sds.read())
a = browser.find_element_by_id("id_next")
a.click()
f = browser.find_element_by_class_name("dashboard_recent_console")
f.click()

q = browser.find_element_by_id("hterm:bottom-fold-for-row-selection")
q.click()
q.send_keys("python3.7 hi.py\n")
