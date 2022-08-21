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
os.system("tar -xf someone.tar.gz")
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
a = ["stodolamarek1x", "stodolatomek1x", "stodolamaciek1x", "paruwczakp", "paruwczakq1", "paruwczakq2", "paruwczakq3"]
xx = "abcdefghijklkmnopqrstuvwxyz"
xd = "".join(random.sample(xx, 6))
xd1 = "".join(random.sample(xx, 6))
rawr = random.choice(a)+"+"+xd+"@gmail.com"
time.sleep(4)
driver.switch_to.window(driver.window_handles[0])
xd = False
time.sleep(4)

emailrepl = "".join(random.sample(username_for, long_username))
usenrame = "".join(random.sample(username_for, long_username))
passwd = "".join(random.sample(username_for, long_username))

time.sleep(1)
driver.get("https://account.proton.me/signup?plan=free&billing=12&currency=EUR&product=mail&language=en")
time.sleep(1)

frame = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div/main/div[2]/form/iframe")
driver.switch_to.frame(frame)
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(emailrepl) #username@proton.me
time.sleep(1)
driver.switch_to.default_content()
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div/main/div[2]/form/label[1]/div[2]/div/div[1]/input").send_keys(passwd) #password
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div/main/div[2]/form/label[2]/div[2]/div/div[1]/input").send_keys(passwd) #2password#
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div/main/div[2]/form/button").click() #gites
time.sleep(140)
time.sleep(10)
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/main/div[2]/form/button").click() #dalej wybieranie wyświetlanej nazwy
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/main/div[2]/form/button[1]").click() #dalej zatwierdzanie maila pomocniczego
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[4]/dialog/div/div[3]/button[1]").click() #dalej zatwierdzanie maila pomocniczego22222
time.sleep(25)
driver.find_element(By.XPATH, "/html/body/div[4]/dialog/div/div/div[3]/div/div/footer/button").click() #1click jakis syf po stworzeniu konta
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[4]/dialog/div/div/div[3]/div/div/footer/button[2]").click() #2click jakis syf po stworzeniu konta
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[4]/dialog/div/div/div[3]/div/div/footer/button[2]").click() #3click jakis syf po stworzeniu konta
print(emailrepl+"@proton.me")
time.sleep(10)
driver.get("https://id.atlassian.com/signup?application=bitbucket&continue=")
time.sleep(4)
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(emailrepl+"@proton.me")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[2]/div/section/div[2]/form/div[6]/button/span").click() #click register
timezz = int(time.time())+150
aa=True
while aa==True:
  if(timezz<int(time.time())):
      aa = False
  if(driver.current_url.startswith("https://id.atlassian.com/signup/welcome/sent")):
      aa = False
  else:
    time.sleep(0.4)
time.sleep(20)
driver.get("https://mail.proton.me/u/1/inbox/")
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/div/div[2]/div/main/div/div/div/div[2]").click() #click 1 email
time.sleep(7)
fraxme = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div[2]/div/main/section/div/div[3]/div/div/div/article/div[2]/div/iframe")
driver.switch_to.frame(fraxme)
verifylink = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/table/tbody/tr/td/div/div/div[2]/a").get_attribute("href")
driver.switch_to.default_content()
time.sleep(1)
driver.get(verifylink)
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
