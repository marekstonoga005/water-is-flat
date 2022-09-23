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
xxxtime = int(time.time())+900
def rawrzzzz():
  try:
    os.system("rm -rf rawrz")
    os.system("tar -xf volx.tar.gz")
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
    driver = uc.Chrome(options=options, version_main=105)  # version_main allows to specify your chrome version instead of following chrome global version
    driver.set_window_size(1920, 1080)
    a = ["stodolamarek1x", "stodolatomek1x", "stodolamaciek1x", "paruwczakp", "paruwczakq1", "paruwczakq2", "paruwczakq3"]
    xx = "abcdefghijklkmnopqrstuvwxyz"
    xdz = "".join(random.sample(xx, 6))
    xd1 = "".join(random.sample(xx, 6))
    rawr = random.choice(a)+"+"+xdz+"@gmail.com"
    time.sleep(4)
    driver.switch_to.window(driver.window_handles[0])
    xd = False
    time.sleep(4)

    emailrepl = "".join(random.sample(username_for, 8))
    usenrame = "".join(random.sample(username_for, long_username))
    passwd = "".join(random.sample(username_for, long_username))
    emilyez = random.choice(a)+"+"+emailrepl+"@gmail.com"
    time.sleep(1)
    # random.choice(a)+"+"+emailrepl+"@gmail.com"
    print(emilyez)
    time.sleep(2)
    driver.get("https://www.atlassian.com/software/bitbucket/bundle")
    time.sleep(5)
    driver.find_element(By.XPATH, "/html/body/main/div[3]/div/div[2]/div[5]/div/div/div[1]/span").click()
    time.sleep(4)
    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(emilyez)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="signup-submit"]').click() #click register
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

    os.system("echo 'gmel|"+emilyez+"' > a.txt")
    os.system("node index.js")
    f = open("a.txt", "r")
    verifylink = f.read()

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
    driver.find_element(By.XPATH, "/html/body/main/div/div[1]/div[1]/div[2]/form[1]/div[2]/input").send_keys(xdz+xd1)
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
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/section/div/form/div[1]/input").send_keys("https://bitbucket.org/ijdvcexokkbc/hdgxzk/src/master/")
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
    driver.get("https://circleci.com/auth/signup/")
    time.sleep(15)
    driver.find_element(By.XPATH, "/html/body/div/signup/div/form/div[1]/input").send_keys("".join(random.sample(username_for, 23))+"@gmail.com")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/signup/div/form/div[2]/input").send_keys("".join(random.sample(username_for, 8))+"A!1")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/signup/div/form/div[5]/button").click()
    time.sleep(20)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/form/section[1]/div[2]/div").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/form/section[1]/div[2]/div[2]/div/div[2]").click()
    time.sleep(0.5)

    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/form/section[2]/div[2]/div").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/form/section[2]/div[2]/div[2]/div/div[1]").click()
    time.sleep(0.5)

    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/form/section[3]/div[2]/div").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/form/section[3]/div[2]/div[2]/div/div[1]").click()
    time.sleep(0.5)

    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/form/section[4]/div[2]/div").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/form/section[4]/div[2]/div[2]/div/div[1]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div/button").click()
    time.sleep(2.5)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/section[4]/div/button").click()
    time.sleep(12)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/section/form/div/div/button[1]").click()
    time.sleep(25)

    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/section[1]/div/div[2]/button").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/section[1]/div/div[2]/div/div/ul/li").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/section[2]/div/div[2]/button").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/section[2]/div/div[2]/div/div/ul/li").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/section[3]/div/div[2]/button[1]/div[2]/div[2]/input").send_keys("master")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/button").click()
    time.sleep(33)
  except as rawrzxx:
    print(rawrzxx)
    pass
    if(xxxtime<int(time.time())):
      quit()
    rawrzzzz()
rawrzzzz()
