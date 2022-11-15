
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
driver.get("https://google.com/")
def render(driver, duration):
    import time
    from IPython.display import clear_output, display, Javascript, HTML
    from ipykernel import comm

    clear_output()

    display(HTML(f"""
        <img id='image'>
        <script>
            const $img = document.querySelector('#output-area #image');
            google.colab.kernel.comms.registerTarget('i', (comm, message) => {{
                $img.src = message.data.i;
            }});
        </script>
    """))

    start_time = time.time()
    while True:
        b64 = driver.get_screenshot_as_base64()
        comm.Comm(target_name='i', data={'i': f"data:image/png;base64,{b64}"})
        time.sleep(0.1)
        if time.time() - start_time >= duration:
            break
time.sleep(10)
print("x")
render(driver, duration=10)
