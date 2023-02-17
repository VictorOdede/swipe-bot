from selenium import webdriver
from time import sleep
from secret import username, password


class TinderBot():

	def __init__(self):
		self.driver = webdriver.Chrome()


	def login (self):


		#navigate to site
		self.driver.get('https://tinder.com/')

		#wait a few seconds
		sleep(5)

		#click on the fb login button
		fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button') 
		fb_btn.click()

		#switch btn the tinder & fb window
		base_window = self.driver.window_handles[0]
		pop_up = self.driver.window_handles[1]

		self.driver.switch_to.window(pop_up)

		#send email credentials
		email = self.driver.find_element_by_xpath('//*[@id="email"]')
		email.send_keys(username)

		#send password credentials
		passwrd = self.driver.find_element_by_xpath('//*[@id="pass"]')
		passwrd.send_keys(password)

		#click login
		login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
		login_btn.click()

		self.driver.switch_to.window(base_window)

		sleep(5)

		#get rid of the pop-ups
		popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
		popup_1.click()
		popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
		popup_2.click()


	#like a pic
	def like(self):
		like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
		like_btn.click()

	#dislike a pic
	def dislike(self):
		dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
		dislike_btn.click()


	#coninue swiping
	def auto_swipe(self):
		while True:
			sleep(1)
			try:
				self.like()

			except Exception:
				try:
					sleep(1)
					self.keep_swiping()
					
				except Exception:
					self.popup_3()


					
				




	def keep_swiping(self):
		kp_swiping = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
		kp_swiping.click()


	def popup_3(self):
		popup3_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
		popup3_btn.click()

	def popup_4(self):
		popup4_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/div[2]/button[2]')
		popup4_btn.click()




bot = TinderBot()
bot.login()
bot.auto_swipe()



		







