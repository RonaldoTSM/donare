import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys


class testLogin(unittest.TestCase):
    def setUp(self):
        
        self.browser = webdriver.Chrome()
        
    def test_login_ong(self):
        
        self.browser.get("https://donare.azurewebsites.net/")
        
        go_to_login_button = self.browser.find_element(By.XPATH, '//button[@class="login-button"]')
        go_to_login_button.click()
        time.sleep(2)
        
        login = "ContaGotas"
        password = "1234"
        
        
        nome_usuario_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, "username")))
        senha_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, "senha")))
        
        
        for n in login:
            nome_usuario_input.send_keys(n)
            time.sleep(0.2)
        self.assertEqual(login, "ContaGotas")
        time.sleep(1)
        
        for n in password:
            senha_input.send_keys(n)
            time.sleep(0.2)
        self.assertEqual(password, "1234")
        time.sleep(1)
        
        logar_button = self.browser.find_element(By.CLASS_NAME, 'login-button')
        logar_button.click()
        time.sleep(2)
        self.assertEqual()
        
        