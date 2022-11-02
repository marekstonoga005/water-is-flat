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

subprocess.call(['/bin/bash', '-i', '-c', "curl -sS https://platform.sh/cli/installer | php"])
import requests
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
driver.get("https://auth.api.platform.sh/register?trial_type=general")
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[3]/div/input").send_keys(emil)
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[4]/button").click()
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
# rawr = requests.get('https://www.emailnator.com/', headers=headersdomain)
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
                verifylink = rawrzz.text.split("\n")
driver.get(verifylink[38].split('href="')[1].split('"')[0].replace("amp;", ""))
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/input").send_keys("".join(random.sample(low_word, 13))+"H1!")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[5]/button").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[4]/button").click()
time.sleep(2)
x1 = "".join(random.sample(low_word, 8))
x2 = "".join(random.sample(low_word, 8))
print(x1)
print(x2)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/input").send_keys(x1)
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/input").send_keys(x2)
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[6]/button").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div[2]/div/div[1]").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/input").send_keys("".join(random.sample(low_word, 13)))
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[5]/button").click()
time.sleep(9)
from threading import Thread
driver.get("https://console.platform.sh/-/users/"+x1+"-"+x2+"/settings/tokens")
print(x1)
print(x2)
print(driver.current_url)
time.sleep(8)
driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div/div/div[1]/button").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div/div/div[3]/form/div[2]/div/input").send_keys("".join(random.sample(low_word, 13)))
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div/div/div[3]/form/button[1]").click()
time.sleep(4)
api = driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div/div/div[1]/code").text
driver.get("https://console.platform.sh/projects/create-project")
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/div/div/div/div/div/button[2]").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/div/div/div/div/div[1]/div[1]/div/input").send_keys("".join(random.sample(low_word, 13)))
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/div/div/div/div/div[1]/div[3]/div[1]/div/div/div/div[1]").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/div/div/div/div/div[1]/div[3]/div[1]/div/div/div[2]/div/div[3]/div[2]/div[3]").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/div/div/div/div/div[2]/button[2]").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[3]/div[2]/button[2]").click()
time.sleep(120)
driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[2]/div[2]/span/button").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div/div[2]/div/div[1]/div/aside/button[2]/div").click()
time.sleep(2)
os.system("export PLATFORMSH_CLI_TOKEN=bork")
print(api)
import subprocess
a = driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div/div[2]/div/div[1]/section/div[2]/div/div/pre").text
repo = driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div/div[2]/div/div[1]/section/div[3]/div/div/pre").text
os.system("pwd")
os.system("rm -rf cockyyrawr")
print(a)
os.system("echo 'git.eu-5.platform.sh ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDHVvr73G2u1j0s0RqixwpIGsTKagv3vMErXj/ixorbbuuNFmln8l2OqLo9cvg6QmO8OJFpY1xdOAIQ1hfzcZud+LCdMAxvsC7lz9VMb26Vchuc7o+lq0+w8ORAlKqlFfl2MpLtbEuuRaellXaTlQ36cSKwuCHOfzqsKDyb+Umpm+bYk6ICLnJyiEldo1cs8cAQNIgXRmPiJ2Ws/OamfJi/b1CajNZr6Q3gs7oqRbWBt9mgDFU9sFDMWDmmBAvDQj2azSk2i1hFQ4/lzczt6vQH9vusnESPCJfAiMJb60868BhuvOV9oxITItzwgNDFJltL8LNadZ4x6VvMmPV0DpJb' >> $HOME/.ssh/known_hosts")
def xddd():
    subprocess.call(['/bin/bash', '-i', '-c', "export PLATFORMSH_CLI_TOKEN="+api+" && mkdir cockyyrawr && cd cockyyrawr && git init && "+a+" && wget https://github.com/n2dhektor/fictional-octo-waddle/raw/main/f.tar.gz && tar -xf f.tar.gz && rm f.tar.gz && git add . && git commit -m 'hi' && platform push -q"])
t = Thread(target=xddd)
t.start()
time.sleep(60)

