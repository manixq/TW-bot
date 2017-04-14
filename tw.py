import time
import base64
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

def im_robot(browser):
	if (len(browser.find_elements_by_id("bot_check_image"))>0) :
		print("Im not a robot!")
		exit()

def wait_for_page(browser, delay, name):
	im_robot(browser)
	try:
		element_present = EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, name))
		WebDriverWait(browser, delay).until(element_present)
		print("Found ", name)
	except TimeoutException:
		print("Could not found ", name)
		exit()

f = open("../tribal_wars",'r')
l = f.readline()
p = f.readline()
city_page = f.readline()
f.close()

l = str(base64.decodebytes(l.encode('utf-8')).decode("utf-8"))
p = str(base64.decodebytes(p.encode('utf-8')).decode("utf-8"))



#bot starts work
browser = webdriver.Firefox(executable_path=r"..\geckodriver.exe")

browser.get('https://www.plemiona.pl/')

elem = browser.find_element_by_name('username')  
elem.send_keys(l)
elem = browser.find_element_by_name('password') 
elem.send_keys(p + Keys.RETURN)

wait_for_page(browser, 5, "Świat 115")
browser.get("https://www.plemiona.pl//page/play/pl115")

wait_for_page(browser, 5, "Wyloguj")
browser.find_element_by_partial_link_text("Wyloguj").click()
browser.close()



