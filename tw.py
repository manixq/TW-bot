import time
import base64
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import random

max_h = 2
max_min = 30
num_villages = 2

def im_robot(browser):
	if (len(browser.find_elements_by_id("bot_check_image"))>0) :
		print("Im not a robot!")
		input("\nPress enter to exit ;)")
		exit()

def wait_for_page(browser, delay, name):
	im_robot(browser)
	try:
		element_present = EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, name))
		WebDriverWait(browser, delay).until(element_present)
	except TimeoutException:
		print("Could not found ", name)
		input("\nPress enter to exit ;)")
		exit()

def load_villages():
	villages = []
	with open("../target.txt") as data: 
		for line in data:
			ptr = line.split()
			villages.append(ptr)
	return villages

def farm(browser, element_name, warriors, village, max_h, max_min):
	#light
	elem = browser.find_element_by_name(element_name)
	elem.send_keys(warriors)
	
	#village
	elem = browser.find_element_by_name('input')
	elem.send_keys(village)
	time.sleep(1)
	
	#confirm
	browser.find_element_by_id("target_attack").click()
	time.sleep(1)
	im_robot(browser)
	
	#travel time conditional
	try:
		timer = browser.find_element_by_xpath('//*[@id="command-data-form"]/table[1]/tbody/tr[3]/td[2]').text
	except:
		browser.refresh()
		time.sleep(1)
		timer = browser.find_element_by_xpath('//*[@id="command-data-form"]/table[1]/tbody/tr[3]/td[2]').text
	if (int(timer.split(":")[0]) * 60 + int(timer.split(":")[1])) > (max_h * 60 + max_min):
		elem = browser.find_element_by_xpath("/html/body")
		elem.send_keys("5")
		wait_for_page(browser, 5, "Symulator")
		print("\nAttack on: ", village)
		print("\t time too long!: ", timer)
	else:
		browser.find_element_by_id("troop_confirm_go").click()
		print("\nAttack on: ", village)
		print("\t+send: ", warriors, " ", element_name)
		print("\t time: ", timer)
		wait_for_page(browser, 15, "Symulator")

def godela(browser):
	try:
		browser.find_element_by_id("event_shop_button")
	except:
		browser.find_element_by_class_name('menu-event-icon').click()
	while(1):
		try:
			browser.find_element_by_link_text('Wyzwij').click()
			print("A ty ile masz godeu?")
			time.sleep(5)
		except:
			 break;

f = open("../tribal_wars",'r')
l = f.readline()
p = f.readline()
f.close()

l = str(base64.decodebytes(l.encode('utf-8')).decode("utf-8"))
p = str(base64.decodebytes(p.encode('utf-8')).decode("utf-8"))

#bot starts work
#browser = webdriver.Firefox(executable_path=r"..\geckodriver.exe")
browser = webdriver.Chrome(executable_path=r"..\chromedriver.exe")

browser.get('https://www.plemiona.pl/')
time.sleep(1)

elem = browser.find_element_by_name('username')  
elem.send_keys(l)
elem = browser.find_element_by_name('password') 
elem.send_keys(p + Keys.RETURN)

#village
wait_for_page(browser, 5, "Świat 115")
browser.get("https://www.plemiona.pl/page/play/pl115")
villages = load_villages()

#place
elem = browser.find_element_by_xpath("/html/body")
elem.send_keys("5")
wait_for_page(browser, 5, "Symulator")


index = 0
light_num = 0
axe_num = 0
timeout = 0
village_count = num_villages
while(1):
	time.sleep(1)
	if timeout <= 0:
		village = villages[index][0]
		axes = int(villages[index][1])
		lk = int(villages[index][2])
		
		try:
			elem = browser.find_element_by_id('units_entry_all_axe')
		except NoSuchElementException:
			#place
			elem = browser.find_element_by_xpath("/html/body")
			elem.send_keys("5")
			wait_for_page(browser, 5, "Symulator")
		
		pre_axe = axe_num
		pre_light = light_num
		
		elem = browser.find_element_by_id('units_entry_all_axe')
		axe_num = int(elem.text[1:-1])
		
		elem = browser.find_element_by_id('units_entry_all_light')
		light_num = int(elem.text[1:-1])
		
		if pre_axe != axe_num or pre_light != light_num:
			print("\nAvailable units:")
			print("\tlight: ", light_num)
			print("\taxes: ", axe_num)
		
		if light_num >= lk:
			#lk
			farm(browser, "light", lk, village, max_h, max_min)
			index += 1
		elif  axe_num >= axes:
			#axes
			farm(browser, "axe", axes, village, max_h, max_min)
			index += 1
		else:
			#no warriors :(
			elem = browser.find_element_by_xpath("/html/body")
			elem.send_keys("d")
			wait_for_page(browser, 5, "Symulator")
			if(village_count > 0):
				village_count -= 1
			else:
				print("i ll wait...")
				min_time = random.randint(160,624)
				print(min_time, "sec")
				village_count = num_villages
				timeout = min_time
	#~ else:
	#ile masz godel function
		#godela(browser)
	if index == len(villages):
		index = 0
		timeout = 10
		print("\n====RESTART====\n")
	timeout = timeout - 1


wait_for_page(browser, 5, "Wyloguj")
browser.find_element_by_partial_link_text("Wyloguj").click()
browser.close()



