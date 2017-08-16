import sys
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

#gui
from PyQt5 import QtCore, QtGui 
from gui import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import QtWidgets

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
	with open("../tw_setup/target.txt") as data: 
		for line in data:
			villages.append(line)
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
		#const_string = browser.find_element_by_xpath('//*[@id="command-data-form"]/table[1]/tbody/tr[3]/td[1]').text #xpath to "Duration" const string
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

def log_in(browser, world):
	f = open("../tw_setup/tribal_wars",'r')
	l = f.readline()
	p = f.readline()
	f.close()
	
	l = str(base64.decodebytes(l.encode('utf-8')).decode("utf-8"))
	p = str(base64.decodebytes(p.encode('utf-8')).decode("utf-8"))
	
	if browser == 0:
		browser = webdriver.Chrome(executable_path=r"../tw_setup/chromedriver.exe")
	else:
		browser = webdriver.Firefox(executable_path=r"../tw_setup/geckodriver.exe")

	browser.get('https://www.plemiona.pl/')
	time.sleep(1)

	elem = browser.find_element_by_name('username')  
	elem.send_keys(l)
	elem = browser.find_element_by_name('password') 
	elem.send_keys(p + Keys.RETURN)

	#village
	wait_for_page(browser, 5, "Świat 115")
	browser.get("https://www.plemiona.pl/page/play/" + world)
	return browser

def go_farm(browser_, world_, army_, villages_number_, wait_time_, max_range_):
	#bot starts work
	browser = log_in(browser_, world_)
	villages = load_villages()

	#place
	elem = browser.find_element_by_xpath("/html/body")
	elem.send_keys("5")
	wait_for_page(browser, 5, "Symulator")

	index = 0
	
	spear_num = 0
	sword_num = 0
	axe_num = 0
	light_num = 0
	scout_num = 0
	ram_num = 0
	cata_num = 0
	snob_num = 0
	
	wait_times = wait_time_.split(":")
	max_h = int(max_range_.split(":")[0])
	max_min = int(max_range_.split(":")[1])
	
	timeout = 0
	village_count = villages_number_
	while(1):
		time.sleep(1)
		if timeout <= 0:
			village = villages[index]
			
			spear = army_[0]
			sword = army_[1]
			axe = army_[2]
			light = army_[3]
			scout = army_[4]
			ram = army_[5]
			cata = army_[6]
			snob = army_[7]
			
			try:
				elem = browser.find_element_by_id('units_entry_all_axe')
			except NoSuchElementException:
				#place
				elem = browser.find_element_by_xpath("/html/body")
				elem.send_keys("5")
				wait_for_page(browser, 5, "Symulator")
			
			pre_spear = spear_num
			pre_sword = sword_num
			pre_axe = axe_num
			pre_light = light_num
			pre_scout = scout_num
			pre_ram = ram_num
			pre_cata = cata_num
			pre_snob = snob_num
			
			elem = browser.find_element_by_id('units_entry_all_spear')
			spear_num = int(elem.text[1:-1])
			elem = browser.find_element_by_id('units_entry_all_sword')
			sword_num = int(elem.text[1:-1])			
			elem = browser.find_element_by_id('units_entry_all_axe')
			axe_num = int(elem.text[1:-1])
			elem = browser.find_element_by_id('units_entry_all_light')
			light_num = int(elem.text[1:-1])			
			elem = browser.find_element_by_id('units_entry_all_spy')
			scout_num = int(elem.text[1:-1])			
			elem = browser.find_element_by_id('units_entry_all_ram')
			ram_num = int(elem.text[1:-1])			
			elem = browser.find_element_by_id('units_entry_all_catapult')
			cata_num = int(elem.text[1:-1])
			elem = browser.find_element_by_id('units_entry_all_snob')
			snob_num = int(elem.text[1:-1])
			
			if (pre_spear != spear_num or pre_sword != sword_num or 
				pre_axe != axe_num or pre_light != light_num or 
				pre_scout != scout_num or pre_ram != ram_num or 
				pre_cata != cata_num or pre_snob != snob_num):
				
				print("\nAvailable units:")
				print("\tspear: ", spear_num)
				print("\tsword: ", sword_num)
				print("\taxes: ", axe_num)
				print("\tlight: ", light_num)
				print("\tscout: ", scout_num)
				print("\tram: ", ram_num)
				print("\tcata: ", cata_num)
				print("\tsnob: ", snob_num)
			
			if light_num >= light and light != 0:
				#lk
				farm(browser, "light", light, village, max_h, max_min)
				index += 1
			elif  axe_num >= axe and axe != 0:
				#axes
				farm(browser, "axe", axe, village, max_h, max_min)
				index += 1
			elif  sword_num >= sword and sword != 0:
				#axes
				farm(browser, "sword", sword, village, max_h, max_min)
				index += 1
			elif  spear_num >= spear and spear != 0:
				#axes
				farm(browser, "spear", spear, village, max_h, max_min)
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
					min_time = random.randint(int(wait_times[0]),int(wait_times[1]))
					print(min_time, "sec")
					village_count = villages_number_
					timeout = min_time
		#~ else:
		#ile masz godel function
			#godela(browser)
		if index == len(villages):
			index = 0
			timeout = 10
			print("\n====RESTART====\n")
		timeout = timeout - 1

def time_attack(browser_, world_, victims_):
	#bot starts work
	browser = log_in(browser_, world_)

	#place
	elem = browser.find_element_by_xpath("/html/body")
	elem.send_keys("5")
	wait_for_page(browser, 5, "Symulator")
	
	army_ = victims_[1]
	spear = army_[0]
	sword = army_[1]
	axe = army_[2]
	light = army_[3]
	scout = army_[4]
	ram = army_[5]
	cata = army_[6]
	snob = army_[7]
	
	elem = browser.find_element_by_name('spear')
	elem.send_keys(spear)
	elem = browser.find_element_by_name('sword')
	elem.send_keys(sword)
	elem = browser.find_element_by_name('axe')
	elem.send_keys(axe)
	elem = browser.find_element_by_name('spy')
	elem.send_keys(scout)
	elem = browser.find_element_by_name('light')
	elem.send_keys(light)
	elem = browser.find_element_by_name('ram')
	elem.send_keys(ram)
	elem = browser.find_element_by_name('catapult')
	elem.send_keys(cata)
	elem = browser.find_element_by_name('snob')
	elem.send_keys(snob)
	
	#village
	elem = browser.find_element_by_name('input')
	elem.send_keys(victims_[0])
	time.sleep(1)
	
	#confirm
	browser.find_element_by_id("target_attack").click()
	
	time.sleep(1)
	attack_time = victims_[2]
	attack_time = attack_time.split(":")
	if len(attack_time < 4):
		attack_time[3] = 0
	
	while(1):
		current_time = browser.find_element_by_xpath('//*[@id="date_arrival"]/span').text[10:]
		current_time = current_time.split(":")
		if int(attack_time[0]) == int(current_time[0]) and int(attack_time[1]) == int(current_time[1]) and int(attack_time[2]) == int(current_time[2]):
			ms = float(attack_time[3]) / 1000.0
			if ms > 0.01:
				time.sleep(ms)
			browser.find_element_by_id("troop_confirm_go").click()
			break
		time.sleep(0.01)
		print(attack_time, "      ", current_time)

class MyDialog(QDialog):
	def __init__(self, parent=None):
		super(MyDialog, self).__init__()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.victims = []
	
	def go_farm(self):
		browser_ = self.ui.viewer.currentIndex()
		world_ = self.ui.world_edit.text()
		army_ = [self.ui.spear_box.value(),
			self.ui.sword_box.value(),
			self.ui.axe_box.value(),
			self.ui.light_box.value(),
			self.ui.scout_box.value(),
			self.ui.ram_box.value(),
			self.ui.cata_box.value(),
			self.ui.snob_box.value()]
		villages_number_ = self.ui.villages_box.value()
		wait_time_ = self.ui.wait_time_edit.text()
		max_range_ = self.ui.max_range_edit.text()
		self.hide()
		try:
			go_farm(browser_, world_, army_, villages_number_, wait_time_, max_range_)
		except:
			print("error")
		self.show()
	
	def time_attack(self):
		browser_ = self.ui.viewer.currentIndex()
		world_ = self.ui.world_edit.text()
		army_ = [self.ui.spear_box.value(),
			self.ui.sword_box.value(),
			self.ui.axe_box.value(),
			self.ui.light_box.value(),
			self.ui.scout_box.value(),
			self.ui.ram_box.value(),
			self.ui.cata_box.value(),
			self.ui.snob_box.value()]
		attack_time_ = self.ui.attack_at_edit.text()
		victim_ = self.ui.attack_on_edit.text()
		self.victims.append(victim_)
		self.victims.append(army_)
		self.victims.append(attack_time_)
		self.hide()
		try:
			time_attack(browser_, world_, self.victims)
		except:
			print("error")
		self.victims = []
		self.show()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MyDialog()
	ui = Ui_Dialog()
	window.ui.attack_button.clicked.connect(window.time_attack)
	window.ui.go_farm_button.clicked.connect(window.go_farm)
	window.show()
	sys.exit(app.exec_())




