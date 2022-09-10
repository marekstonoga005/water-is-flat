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
os.system("tar -xf rawrrr.tar.gz")
os.system("rm -rf rawr")
os.system("cp -r rawrz rawr")
options = uc.ChromeOptions()
a = True
low_word = "abcdefghijklkmnopqrstuvwxyz"
upper_word = "ABDCEFGHIJKLMNOPQRSTUVWXYZ"
number = "1234567890"
symbols = "!@#$%&*"
username_for = low_word
password_for = low_word + upper_word + number + symbols
long_password = 16
long_username = 12
ass = "".join(random.sample(username_for, 12))
options.add_argument('--no-first-run --no-service-autorun --password-store=basic') #wlacz to jak juz nie bedzie dev test
options.user_data_dir = "rawr"
options.add_argument("--window-size=1920,1080")
options.add_argument('--user-data-dir=rawr')
options.add_argument("--remote-debugging-port=38223")
driver = uc.Chrome(options=options, version_main=103)  # version_main allows to specify your chrome version instead of following chrome global version
driver.set_window_size(1920, 1080)
a = ["stodolamarek1x", "stodolatomek1x", "stodolamaciek1x", "paruwczakp", "paruwczakq1", "paruwczakq2", "paruwczakq3"]
xx = "abcdefghijklkmnopqrstuvwxyz"
xd = "".join(random.sample(xx, 6))
rawr = "".join(random.sample(xx, 6))+"@rawr.com"
driver.get("https://flashfaucet.xyz/?r=15078")
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/a[2]").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/form/div/div[1]/input").send_keys(rawr)
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/form/div/div[2]/input").send_keys(xd)
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/form/div/div[3]/input").send_keys(xd)
time.sleep(60)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/form/div/div[6]/div/button").click()
time.sleep(5)
driver.get("https://flashfaucet.xyz/faucet")
while True:
    time.sleep(60)
    driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/div[1]/div[3]/div[1]/form/button").click()
    time.sleep(30)
