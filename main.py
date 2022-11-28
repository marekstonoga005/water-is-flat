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
driver = uc.Chrome(options=options, version_main=107)
headers = {'Authorization': 'e54a4490de5045589e0c98283821c783'}
time.sleep(5)
def playvideo():
    try:
        if(driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[31]/div[2]/div[1]/button').get_attribute("title")=="Play (k)"):
            driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[31]/div[2]/div[1]/button').click()
    except:
        pass
def clickcookie():
    try:
        if(driver.find_element(By.XPATH, '/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]')):
            driver.find_element(By.XPATH, '/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]').click()
            print("xddd")
    except:
        pass

playvideo()
time.sleep(1)
rsp = requests.get('https://bluezczatu.hckrteam.com/link', headers = headers)
response = rsp.json()
driver.get(response["url"])
time.sleep(5)
clickcookie()
time.sleep(response["time"])

playvideo()
rsp = requests.get('https://bluezczatu.hckrteam.com/link', headers = headers)
response = rsp.json()
driver.get(response["url"])
time.sleep(response["time"])

playvideo()
rsp = requests.get('https://bluezczatu.hckrteam.com/link', headers = headers)
response = rsp.json()
driver.get(response["url"])
time.sleep(response["time"])

playvideo()
rsp = requests.get('https://bluezczatu.hckrteam.com/link', headers = headers)
response = rsp.json()
driver.get(response["url"])
time.sleep(response["time"])

playvideo()
rsp = requests.get('https://bluezczatu.hckrteam.com/link', headers = headers)
response = rsp.json()
driver.get(response["url"])
time.sleep(response["time"])

playvideo()
rsp = requests.get('https://bluezczatu.hckrteam.com/link', headers = headers)
response = rsp.json()
driver.get(response["url"])
time.sleep(response["time"])

playvideo()
rsp = requests.get('https://bluezczatu.hckrteam.com/link', headers = headers)
response = rsp.json()
driver.get(response["url"])
time.sleep(response["time"])

playvideo()
rsp = requests.get('https://bluezczatu.hckrteam.com/link', headers = headers)
response = rsp.json()
driver.get(response["url"])
time.sleep(response["time"])
driver.close()
