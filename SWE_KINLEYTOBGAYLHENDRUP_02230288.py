#'watch any anime'
from selenium import webdriver
from selenium. webdriver. chrome. service import Service
from selenium. webdriver. chrome. options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
import time

name = input('Enter your anime Title: ')

option = Options()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
#driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get('https://gogoanime.mom/')
driver.maximize_window()
search = driver.find_element('xpath','//*[@id="keyword"]')
search.send_keys(name)
time.sleep(2)
pyautogui.press('enter')
time.sleep(4)



