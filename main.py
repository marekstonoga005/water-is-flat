import os
print("rawr")
import undetected_chromedriver as uc
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random
import requests

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
driver = uc.Chrome(options=options, version_main=107)
headersdomain = {'accept': 'application/ld+json'}
responsedomain = requests.get('https://api.mail.tm/domains?page=1', headers=headersdomain)
emil = "".join(random.sample(low_word, 13))+"@"+responsedomain.json()["hydra:member"][0]["domain"]
myobj = {'address': emil,"password": "cloud"}
headersreg = {'accept': 'application/ld+json'}
responsereg = requests.post('https://api.mail.tm/accounts', headers=headersreg, json=myobj)
driver.get('https://dashboard.render.com/register?next=/')
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/form/span[1]/input").send_keys(emil)
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/form/span[2]/input").send_keys("".join(random.sample(low_word, 13))+"H1!")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/form/button").click()
time.slepe(20)
myobjlog = {'address': emil,"password": "cloud"}
headerslog = {'accept': 'application/ld+json'}
responselog = requests.post('https://api.mail.tm/token', headers=headerslog, json=myobjlog)
token = responselog.json()["token"]
headersmess = {'accept': 'application/ld+json', "Authorization": "Bearer "+token}
responsemess = requests.get('https://api.mail.tm/messages', headers=headersmess)
headersmessz = {'accept': 'application/ld+json', "Authorization": "Bearer "+token}
responsemessz = requests.get('https://api.mail.tm/messages/'+responsemess.json()["hydra:member"][0]["id"], headers=headersmess)
verifylink = responsemessz.json()["text"].split("\n")[4]
driver.get(verifylink)
for _ in range(20):
    driver.get("https://dashboard.render.com/select-repo?type=web")
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/form/div/div[1]/div/div/input").send_keys("https://github.com/fdsjocxojv/fuzzy-pancake")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/form/div/div[2]/button").click()
    time.sleep(10)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div[1]/div/div/div/div/div/form/div[1]/div[2]/div/div/div[1]/input").send_keys("".join(random.sample(low_word, 13)))
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div[1]/div/div/div/div/div/form/div[6]/div[2]/div/div/div/div/div/input").send_keys(Keys.BACK_SPACE+Keys.BACK_SPACE+Keys.BACK_SPACE+Keys.BACK_SPACE+"npm run build")
    time.sleep(1)
    driver.execute_script("window.scrollBy(0,1500)", "")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div[1]/div/div/div/div/div/form/div[10]/div/button").click()
    time.sleep(10)
