import os
import undetected_chromedriver as uc
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import random
import requests
print("aaa")

def uwu():
    # try:
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
        low_word = "abcdefghijklkmnopqrstuvwxyz"



        # random.choice(a)+"+"+emailrepl+"@gmail.com"


        driver.get("https://codemagic.io/signup")
        headersdomain = {'accept': 'application/ld+json'}
        responsedomain = requests.get('https://api.mail.tm/domains?page=1', headers=headersdomain)
        emil = "".join(random.sample(low_word, 13))+"@"+responsedomain.json()["hydra:member"][0]["domain"]
        myobj = {'address': emil,"password": "cloud"}
        headersreg = {'accept': 'application/ld+json'}
        responsereg = requests.post('https://api.mail.tm/accounts', headers=headersreg, json=myobj)
        driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/form/input[1]").send_keys("".join(random.sample(low_word, 13)))
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/form/input[2]").send_keys(emil)
        
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/form/button").click()
        time.sleep(15)

        myobjlog = {'address': emil,"password": "cloud"}
        headerslog = {'accept': 'application/ld+json'}
        responselog = requests.post('https://api.mail.tm/token', headers=headerslog, json=myobjlog)
        token = responselog.json()["token"]
        headersmess = {'accept': 'application/ld+json', "Authorization": "Bearer "+token}
        responsemess = requests.get('https://api.mail.tm/messages', headers=headersmess)
        headersmessz = {'accept': 'application/ld+json', "Authorization": "Bearer "+token}
        responsemessz = requests.get('https://api.mail.tm/messages/'+responsemess.json()["hydra:member"][0]["id"], headers=headersmess)
        verifylink = responsemessz.json()["text"].split("\n")[3].replace("Authentication key: *", "").replace("*","")
        print(verifylink)
        driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/form/input").send_keys(verifylink)
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/form/button").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div/span").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div/button").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[1]/div/label[4]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[3]/button").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div[1]/input").send_keys("https://bitbucket.org/dfggcvdrg/dfgcxvfdg/")
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div/label").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div[3]/div/button[8]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[3]/button").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/header/div[3]/div/div/button").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[2]/div/button/span/i").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[2]/div/div").click()
        time.sleep(1.5)
        driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[2]/div/div/div/div").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/header/div[3]/div/div/span/button").click()
        time.sleep(4)
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div/button[1]").click()
        time.sleep(20)
        
        



        
    # except:
    #     pass
    #     uwu()

uwu()
