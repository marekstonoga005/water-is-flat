import undetected_chromedriver as uc
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import json
import os
import requests
from selenium.webdriver.common.by import By
os.system("tar -xf rawrr.tar.gz")
os.system("rm -rf rawr")
os.system("cp -r rawrz rawr")
options = uc.ChromeOptions()
a = True
low_word = "abcdefghijklkmnopqrstuvwxyz"
options.add_argument('--no-first-run --no-service-autorun --password-store=basic') #wlacz to jak juz nie bedzie dev test
options.user_data_dir = "rawr"
options.add_argument("--window-size=1920,1080")
options.add_argument('--user-data-dir=rawr')
options.add_argument("--remote-debugging-port=38223")
driver = uc.Chrome(options=options, version_main=103)  # version_main allows to specify your chrome version instead of following chrome global version
driver.set_window_size(1920, 1080)
driver.get("https://nordalts.com/verifytest?"+"".join(random.sample(low_word, 12)))
rawr = 0
a = True
while(a==True):
  time.sleep(1)
  if(rawr==12):
    a = False
    driver.close()
  if(w.find_element(By.XPATH, '//*[@id="egg"]').text=="invalid id thingy yes (if you think its a mistake contact fisch on discord or smth idk)"):
    rawr = rawr+1
    driver.get("https://nordalts.com/verifytest?"+"".join(random.sample(low_word, 12)))
driver.close()
