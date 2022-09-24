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

    # os.system("npm i")
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
    options.user_data_dir = "rawr3"
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--user-data-dir=rawr3')
    options.add_argument("--remote-debugging-port=38223")
    driver = uc.Chrome(options=options, version_main=105)  # version_main allows to specify your chrome version instead of following chrome global version
    driver.set_window_size(1920, 1080)
    a = ["stodolamarek1x", "stodolatomek1x", "stodolamaciek1x", "paruwczakp", "paruwczakq1", "paruwczakq2", "paruwczakq3", "janusz.mostowiak2137", "adasdrzewicx"]
    xx = "abcdefghijklkmnopqrstuvwxyz"
    xdz = "".join(random.sample(xx, 6))
    xd1 = "".join(random.sample(xx, 6))
    rawr = random.choice(a)+"+"+xdz+"@gmail.com"
    time.sleep(4)
    #driver.switch_to.window(driver.window_handles[0])
    xd = False
    time.sleep(4)

    emailrepl = "".join(random.sample(username_for, 8))
    usenrame = "".join(random.sample(username_for, long_username))
    passwd = "".join(random.sample(username_for, long_username))
    #emilyez = random.choice(a)+"+"+emailrepl+"@gmail.com"


    driver.execute_script('''window.open("http://bings.com","_blank");''')
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(0.5)
    driver.get("https://www.emailnator.com/")
    time.sleep(6)
    try:
      driver.find_element(By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]').click()
    except:
      pass
    time.sleep(0.5)
    try:
      driver.find_element(By.XPATH, '//*[@id="close-btn-ann"]').click()
    except:
      pass
    time.sleep(1.5)
    driver.find_element(By.XPATH, '//*[@id="custom-switch-domain"]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '/html/body/div/div/main/div[1]/div/div/div/div[2]/div/div[5]/div/button').click()
    time.sleep(2)
    emilyez = driver.find_element(By.XPATH, '/html/body/div/div/main/div[1]/div/div/div/div[2]/div/div[1]/input').get_attribute("value")
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])
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

    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div/main/div[1]/div/div/div/div[2]/div/div[3]/button").click()
    time.sleep(6)
    linkz = driver.find_element(By.XPATH, "/html/body/div/div/section/div/div/div[3]/div/div[2]/div[2]/div/table/tbody/tr[2]/td/a").get_attribute("href")
    time.sleep(0.5)
    driver.get(linkz)
    time.sleep(7)
    verifylink = driver.find_element(By.XPATH, "/html/body/div/div/section/div/div/div[3]/div/div/div[2]/div/div/table/tbody/tr/td/div/div/div[2]/a").get_attribute("href")
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    driver.get(verifylink)
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[2]/div/section/div[2]/form/div[2]/div/div/div/input").send_keys("".join(random.sample(username_for, 12)))
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
    print(driver.current_url)
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
    time.sleep(10)
    print(driver.current_url)
    time.sleep(23)
  except Exception as rawrzxx:
    print(rawrzxx)
    pass
    if(xxxtime<int(time.time())):
      quit()
    rawrzzzz()
rawrzzzz()
