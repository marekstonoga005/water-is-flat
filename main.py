if __name__ == "__main__":
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
    # os.system("rm -rf rawrz")
    # os.system("tar -xf volx.tar.gz")
    # os.system("rm -rf rawr")
    # os.system("cp -r rawrz rawr")
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
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--remote-debugging-port=38223")
    driver = uc.Chrome(options=options, version_main=106)
    passwd = "".join(random.sample(low_word, 12))+"H!1"



    driver.get("https://www.datacamp.com/")

    driver.set_window_size(1920, 1080)



    time.sleep(12)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/header/div[1]/div[1]/div[2]/form/fieldset[1]/label/div/input").send_keys("".join(random.sample(low_word, 12))+"@cldkid.com")
    time.sleep(0.5)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/header/div[1]/div[1]/div[2]/form/fieldset[2]/label/div/input").send_keys("".join(random.sample(low_word, 12))+"Ah!1")
    time.sleep(0.5)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/header/div[1]/div[1]/div[2]/form/button").click()
    time.sleep(7)
    driver.get("https://app.datacamp.com/workspace")

    time.sleep(3)

    driver.find_element(By.XPATH, "/html/body/main/div[1]/div[2]/div/div/div/div/a").click()
    time.sleep(4)
    driver.find_element(By.XPATH, "/html/body/main/div[1]/div[2]/div/div/main/div/div[2]/div[2]/section/section[1]/div[1]/button").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/section/div/div[2]/form/div/div/div/div[2]/div/input").send_keys("https://github.com/n2dhektor/upgraded-octo-funicular")
    time.sleep(0.5)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/section/div/div[2]/form/div/div/div/div[4]/div[1]/div[2]/label").click()
    time.sleep(0.5)
    try:
        driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/section/div/div[2]/form/footer/button[2]").click()
    except:
        pass
    time.sleep(1)
    try:
        driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/section/div/div[2]/form/footer/button[2]").click()
    except:
        pass
    time.sleep(8)
    driver.find_element(By.XPATH, "/html/body/main/div[1]/div/div/div/div/div[2]/div[1]/div[1]/button[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/main/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[1]/button").click()
    time.sleep(8)
    driver.get("https://app.datacamp.com/workspace/overview")
    time.sleep(4)
    driver.find_element(By.XPATH, "/html/body/main/div[1]/div[2]/div/div/main/div/div[2]/div[2]/section/section[1]/div[1]/button").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/section/div/div[2]/form/div/div/div/div[2]/div/input").send_keys("https://github.com/n2dhektor/upgraded-octo-funicular")
    time.sleep(0.5)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/section/div/div[2]/form/div/div/div/div[4]/div[1]/div[2]/label").click()
    time.sleep(0.5)
    try:
        driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/section/div/div[2]/form/footer/button[2]").click()
    except:
        pass
    time.sleep(1)
    try:
        driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/section/div/div[2]/form/footer/button[2]").click()
    except:
        pass
    time.sleep(8)
    driver.find_element(By.XPATH, "/html/body/main/div[1]/div/div/div/div/div[2]/div[1]/div[1]/button[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/main/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[1]/button").click()
    time.sleep(8)
    driver.get("https://app.datacamp.com/workspace/overview")
    time.sleep(4)
    driver.find_element(By.XPATH, "/html/body/main/div[1]/div[2]/div/div/main/div/div[2]/div[2]/section/section[1]/div[1]/button").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/section/div/div[2]/form/div/div/div/div[2]/div/input").send_keys("https://github.com/n2dhektor/upgraded-octo-funicular")
    time.sleep(0.5)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/section/div/div[2]/form/div/div/div/div[4]/div[1]/div[2]/label").click()
    time.sleep(0.5)
    try:
        driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/section/div/div[2]/form/footer/button[2]").click()
    except:
        pass
    time.sleep(1)
    try:
        driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/section/div/div[2]/form/footer/button[2]").click()
    except:
        pass
    time.sleep(8)
    driver.find_element(By.XPATH, "/html/body/main/div[1]/div/div/div/div/div[2]/div[1]/div[1]/button[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/main/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[1]/button").click()
    time.sleep(8)
    driver.get("https://app.datacamp.com/workspace/overview")
    time.sleep(4)
    driver.find_element(By.XPATH, "/html/body/main/div[1]/div[2]/div/div/main/div/div[2]/div[2]/section/section[1]/div[1]/button").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/section/div/div[2]/form/div/div/div/div[2]/div/input").send_keys("https://github.com/n2dhektor/upgraded-octo-funicular")
    time.sleep(0.5)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/section/div/div[2]/form/div/div/div/div[4]/div[1]/div[2]/label").click()
    time.sleep(0.5)
    try:
        driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/section/div/div[2]/form/footer/button[2]").click()
    except:
        pass
    time.sleep(1)
    try:
        driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/section/div/div[2]/form/footer/button[2]").click()
    except:
        pass
    time.sleep(8)
    driver.find_element(By.XPATH, "/html/body/main/div[1]/div/div/div/div/div[2]/div[1]/div[1]/button[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/main/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[1]/button").click()
    time.sleep(8)
    driver.get("https://app.datacamp.com/workspace/overview")
    time.sleep(4)
    driver.find_element(By.XPATH, "/html/body/main/div[1]/div[2]/div/div/main/div/div[2]/div[2]/section/section[1]/div[1]/button").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/section/div/div[2]/form/div/div/div/div[2]/div/input").send_keys("https://github.com/n2dhektor/upgraded-octo-funicular")
    time.sleep(0.5)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/section/div/div[2]/form/div/div/div/div[4]/div[1]/div[2]/label").click()
    time.sleep(0.5)
    try:
        driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/section/div/div[2]/form/footer/button[2]").click()
    except:
        pass
    time.sleep(1)
    try:
        driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/section/div/div[2]/form/footer/button[2]").click()
    except:
        pass
    time.sleep(8)
    driver.find_element(By.XPATH, "/html/body/main/div[1]/div/div/div/div/div[2]/div[1]/div[1]/button[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/main/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[1]/button").click()
    time.sleep(8)
    driver.get("https://app.datacamp.com/workspace/overview")


