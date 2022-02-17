import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from tkinter import messagebox
from threading import *




class Instagem():
    def login(self,usuario,senha):
       opcao = Options()
       opcao.headless = True
       self.driver = webdriver.Chrome()  # options=opcao
       messagebox.showinfo("Current session is {}".format(self.driver.session_id))
       driver = self.driver
       driver.get("https://www.instagram.com")
       time.sleep(3)

       try:
           user_element = driver.find_element(By.XPATH,
                                              "//input[@name='username']")
           user_element.clear()
           time.sleep(random.randint(5, 10))
           user_element.send_keys(usuario)
           time.sleep(random.randint(5, 10))
           password_element = driver.find_element(By.XPATH,
                                                  "//input[@name='password']")
           password_element.clear()
           password_element.send_keys(senha)
           time.sleep(random.randint(5, 10))
           password_element.send_keys(Keys.RETURN)
           time.sleep(random.randint(5, 10))
           self.driver.get('https://www.instagram.com')
           messagebox.showinfo("Logando", "Logando no instagram")
       except Exception as e:
           messagebox.showinfo("erro", f"{e}")
           self.driver.close()

    def logar(self):
        with open("Contas.txt", 'r', encoding='utf-8') as arq:
            users = arq.readlines()
            users = list(map(lambda x: x.replace('\n', ''), users))
            users = list(map(lambda x: x.split(','), users))
            for user in users:
                self.login(user[0],user[1])

    def Postagem(self, LINK):
        try:
            WebDriverWait(self.driver.get(f'{LINK}'), 5)
            messagebox.showinfo("Post", "acessando a postagem")
            time.sleep(5)

        except Exception as p:
            messagebox.showinfo('Erro',f'{p}')
            self.driver.close()

    def Comenta(self, quantidade_comentario, tempo_de_descanco_em_segundos):
        global i
        try:
            i = 0
            Arquivo = open("Comentarios.txt", encoding='utf-8')
            comentarios = Arquivo.readlines()
            while i < quantidade_comentario:
                comentario = random.choice(comentarios)
                self.driver.find_element(By.CLASS_NAME, 'Ypffh').click()
                self.driver.find_element(By.CLASS_NAME, 'Ypffh').send_keys(comentario, Keys.ENTER)
                i += 1
                messagebox.showinfo("Comentando", f'{i}')
                time.sleep(tempo_de_descanco_em_segundos)



        except Exception as mse:
            messagebox.showinfo(f'ocorreu a Exessao mse', f'{mse}')
            self.driver.close()

        finally:
            messagebox.showinfo('O script terminou', f' comentando {i}')
            self.driver.close()

    def Marca_Amigo(self, quantidade_comentario, tempo_de_descanco_em_segundos):
        global a
        try:
            a = 0
            Arquivo = open("Amigos.txt", encoding='utf-8')
            Amigo = Arquivo.readlines()
            while a < quantidade_comentario:
                comentarioamigo = random.choice(Amigo)
                messagebox.showinfo('O boot esta', f' comentando')
                self.driver.find_element(By.CLASS_NAME, 'Ypffh').click()
                time.sleep(2.3)
                self.driver.find_element(By.CLASS_NAME, 'Ypffh').send_keys(comentarioamigo, Keys.TAB)
                time.sleep(2.3)
                self.driver.find_element(By.CLASS_NAME, 'Ypffh').send_keys(Keys.ENTER)
                a += 1
                messagebox.showinfo(f'o amigo {comentarioamigo} Marcado total {a}')
                time.sleep(tempo_de_descanco_em_segundos)



        except Exception as e:
            messagebox.showinfo(f'ocorreu a exessao E ', f'{e}')
            self.driver.close()

        finally:
            messagebox.showinfo('O script terminou', f' total de comentarios {a}')
            self.driver.close()

    def threading(self):
        t1 = Thread(target=self.logar())
        t1.start()
