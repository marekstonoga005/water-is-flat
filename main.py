
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
options.add_argument("--window-size=1920,1080")
options.add_argument("--remote-debugging-port=38223")
driver = uc.Chrome(options=options, version_main=105)  # version_main allows to specify your chrome version instead of following chrome global version
driver.set_window_size(1920, 1080)
driver.get('https://gplinks.co/Vs7b')
time.sleep(20)
try:
    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[1]/div/article/div[3]/center/button").click()
except:
    print("error")
    pass
time.sleep(12)
try:
    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[1]/div/article/div[3]/center/a").click()
except:
    print("error")
    pass
time.sleep(21)
try:
    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[1]/div/article/div[3]/center/button").click()
except:
    print("error")
    pass
time.sleep(12)
try:
    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[1]/div/article/div[3]/center/a").click()
except:
    print("error")
    pass
time.sleep(21)
try:
    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[1]/div/article/div[3]/center/button").click()
except:
    print("error")
    pass
time.sleep(12)
try:
    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[1]/div/article/div[3]/center/a").click()
except:
    print("error")
    pass
time.sleep(11)
try:
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[4]/a").click()
except:
    print("error")
    pass
time.sleep(20)
try:
    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[1]/div/article/div[3]/center/button").click()
except:
    print("error")
    pass
time.sleep(12)
try:
    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[1]/div/article/div[3]/center/a").click()
except:
    print("error")
    pass
time.sleep(21)
try:
    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[1]/div/article/div[3]/center/button").click()
except:
    print("error")
    pass
time.sleep(12)
try:
    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[1]/div/article/div[3]/center/a").click()
except:
    print("error")
    pass
time.sleep(21)
try:
    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[1]/div/article/div[3]/center/button").click()
except:
    print("error")
    pass
time.sleep(12)
try:
    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[1]/div/article/div[3]/center/a").click()
except:
    print("error")
    pass
time.sleep(11)
try:
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[4]/a").click()
except:
    print("error")
    pass
time.sleep(20)
try:
    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[1]/div/article/div[3]/center/button").click()
except:
    print("error")
    pass
time.sleep(12)
try:
    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[1]/div/article/div[3]/center/a").click()
except:
    print("error")
    pass
time.sleep(21)
try:
    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[1]/div/article/div[3]/center/button").click()
except:
    print("error")
    pass
time.sleep(12)
try:
    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[1]/div/article/div[3]/center/a").click()
except:
    print("error")
    pass
time.sleep(21)
try:
    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[1]/div/article/div[3]/center/button").click()
except:
    print("error")
    pass
time.sleep(12)
try:
    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[1]/div/article/div[3]/center/a").click()
except:
    print("error")
    pass
time.sleep(11)
try:
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[4]/a").click()
except:
    print("error")
    pass
time.sleep(20)
try:
    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[1]/div/article/div[3]/center/button").click()
except:
    print("error")
    pass
time.sleep(12)
try:
    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[1]/div/article/div[3]/center/a").click()
except:
    print("error")
    pass
time.sleep(21)
try:
    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[1]/div/article/div[3]/center/button").click()
except:
    print("error")
    pass
time.sleep(12)
try:
    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[1]/div/article/div[3]/center/a").click()
except:
    print("error")
    pass
time.sleep(21)
try:
    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[1]/div/article/div[3]/center/button").click()
except:
    print("error")
    pass
time.sleep(12)
try:
    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[1]/div/article/div[3]/center/a").click()
except:
    print("error")
    pass
time.sleep(11)
try:
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[4]/a").click()
except:
    print("error")
    pass
time.sleep(20)
try:
    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[1]/div/article/div[3]/center/button").click()
except:
    print("error")
    pass
time.sleep(12)
try:
    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[1]/div/article/div[3]/center/a").click()
except:
    print("error")
    pass
time.sleep(21)
try:
    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[1]/div/article/div[3]/center/button").click()
except:
    print("error")
    pass
time.sleep(12)
try:
    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[1]/div/article/div[3]/center/a").click()
except:
    print("error")
    pass
time.sleep(21)
try:
    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[1]/div/article/div[3]/center/button").click()
except:
    print("error")
    pass
time.sleep(12)
try:
    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[1]/div/article/div[3]/center/a").click()
except:
    print("error")
    pass
time.sleep(11)
try:
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[4]/a").click()
except:
    print("error")
    pass
time.sleep(20)
