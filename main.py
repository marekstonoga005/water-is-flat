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
os.system("tar -xf meow.tar.gz")
os.system("rm -rf rawr")
os.system("cp -r rawrz rawr")
os.system("npm i")
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
a = ["forzahorizon5.ml", "forzahorizon5.tk", "forzahorizon5.ga", "forzahorizon5.gq", "forzahorizon5.cf", "unturnedrp.tk", "unturnedrp.ml", "highrp.tk", "highrp.ml", "highrp.ga", "highrp.cf", "highrp.gq", "stolicarp.tk", "stolicarp.ml", "stolicarp.ga", "stolicarp.cf", "stolicarp.gq", "txtl.ml", "txtl.tk", "txtl.ga", "txtl.cf", "txtl.gq"]
xx = "abcdefghijklkmnopqrstuvwxyz"
xd = "".join(random.sample(xx, 6))
xd1 = "".join(random.sample(xx, 6))
rawr = xd+"@"+random.choice(a)
time.sleep(4)
driver.switch_to.window(driver.window_handles[0])
driver.get("https://id.atlassian.com/signup?application=bitbucket&continue=https%3A%2F%2Fbitbucket.org%2Faccount%2Fsignin%2F%3Fnext%3D%252F")
time.sleep(4)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[2]/div/section/div[2]/form/div[1]/div/div/div/input").send_keys(rawr)
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="signup-submit"]').click()
timez = int(time.time())+80
a=True
while a==True:
  if(timez<int(time.time())):
      a = False
  if(driver.current_url.startswith("https://id.atlassian.com/signup/welcome/sent")):
      a = False
  else:
      time.sleep(0.4)
time.sleep(60)
os.system("echo "+rawr+" > a.txt")
os.system("node index.js")
f = open("a.txt", "r")
egg = f.read()
driver.get(egg)
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[2]/div/section/div[2]/form/div[2]/div/div/div/input").send_keys("CloudKid")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[2]/div/section/div[2]/form/div[3]/div[1]/div/div/div/div/input").send_keys(ass+"!H")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[2]/div/section/div[2]/form/div[6]/button").click()
timezz = int(time.time())+80
aa=True
while aa==True:
  if(timezz<int(time.time())):
      aa = False
  if(driver.current_url.startswith("https://bitbucket.org/atlassianid/bb-signup/")):
      aa = False
  else:
    time.sleep(0.4)
time.sleep(1.5)
driver.find_element(By.XPATH, "/html/body/main/div/div[1]/div[1]/div[2]/form[1]/div[2]/input").send_keys(xd+xd1)
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/main/div/div[1]/div[1]/div[2]/form[1]/p/button").click()
timezz = int(time.time())+80
az=True
while az==True:
  if(timezz<int(time.time())):
      az = False
  if(driver.current_url.startswith("https://bitbucket.org/account/survey")):
      az = False
  else:
      time.sleep(0.4)
time.sleep(1.5)
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div[2]/div[5]/a/span/span/span").click()
time.sleep(2)
driver.get("https://bitbucket.org/repo/import")
time.sleep(4)
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/section/div/form/div[1]/input").send_keys("https://bitbucket.org/sdfuohdf/rawr/src/master//")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/section/div/form/div[4]/div[1]/div[2]/span/input[1]").send_keys("".join(random.sample(username_for, 6)))
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/section/div/form/div[4]/div[2]/input").send_keys("".join(random.sample(username_for, 6)))
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/section/div/form/div[5]/div/button").click()
time.sleep(21)




driver.get("https://circleci.com/signup/")
time.sleep(4)
try:
  driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/a[2]").click()
except:
  pass
time.sleep(2)
try:
  driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/section/div[2]/div/div/div[2]/div[3]/button").click()
except:
  pass
try:
  driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/section/div[2]/div/div/div[2]/div[3]/button").click()
except:
  pass
timezz = int(time.time())+45
az=True
while az==True:
  if(timezz<int(time.time())):
    try:
      driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/section/div[2]/div/div/div[2]/div[3]/button").click()
    except:
      pass
    try:
      driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/section/div[2]/div/div/div[2]/div[3]/button").click()
    except:
      pass
      az = False
  if(driver.current_url.startswith("https://bitbucket.org/site/oauth2/authorize")):
      az = False
  else:
      time.sleep(0.4)
time.sleep(4)
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/section/form/div/div/button[1]").click()

timezz = int(time.time())+55
az=True
while az==True:
  if(timezz<int(time.time())):
      az = False
  if(driver.current_url.startswith("https://app.circleci.com/projects/setup")):
      az = False
  else:
      time.sleep(0.4)
time.sleep(4)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/section[1]/div/div[2]/button").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/section[1]/div/div[2]/div/div/ul/li").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/section[2]/div/div[2]/button").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/section[2]/div/div[2]/div/div/ul/li").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/section[3]/div/div[2]/button[1]/div[2]/div[2]/input").send_keys("master")
time.sleep(7)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/button").click()
time.sleep(20)
