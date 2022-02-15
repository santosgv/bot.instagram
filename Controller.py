import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from tkinter import messagebox
import requests

import Dao
from Dao import Usuario

class Instagem():
    def __init__(self):
        opcao = Options()
        opcao.headless = True
        self.driver = webdriver.Chrome() #options=opcao
        print("Current session is {}".format(self.driver.session_id))


    def login(self):
        usuario=Dao.Usuario().ler()
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)

        try:
            user_element = driver.find_element(By.XPATH,
                                               "//input[@name='username']")
            user_element.clear()
            time.sleep(random.randint(5, 10))
            user_element.send_keys(usuario[0])
            time.sleep(random.randint(5, 10))
            password_element = driver.find_element(By.XPATH,
                                                   "//input[@name='password']")
            password_element.clear()
            password_element.send_keys(usuario[1])
            time.sleep(random.randint(5, 10))
            password_element.send_keys(Keys.RETURN)
            time.sleep(random.randint(5, 10))
            self.driver.get('https://www.instagram.com')
            messagebox.showinfo("Logando", "Logando no instagram")

        except Exception as e:
            print(e)
            self.driver.close()
a=Instagem()
a.login()