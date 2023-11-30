import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys


class testEdicaoPerfil(unittest.TestCase):
    def setUp(self):
        
        self.browser = webdriver.Chrome()
        
    def test_login_ong(self):
        
        self.browser.get("https://donare.azurewebsites.net/doador/aadf/")
        time.sleep(2)
        
        edicao_button = self.browser.find_element(By.XPATH, '//button[@id="editProfile" and @class="btn btn-primary"]')
        edicao_button.click()
        time.sleep(2)
        
        editar_nome_button = self.browser.find_element(By.XPATH, "//button[@type='button' and contains(@onclick, \"enableEdit('nome')\")]")
        editar_nome_button.click()
        
        time.sleep(2)
        
        
        input_nome = self.browser.find_element(By.XPATH, '//input[@id="nome"]')
        current_name = input_nome.get_attribute("value")


        for _ in current_name:
            input_nome.send_keys(Keys.BACKSPACE)
            time.sleep(0.2)

        novo_nome = "Arthur Duarte"
        
        for n in novo_nome:
            input_nome.send_keys(n)
            time.sleep(0.2)
        time.sleep(2)
        
        
        save_changes_button = self.browser.find_element(By.XPATH, "//button[@type='submit' and text()='Salvar Alterações']")
        save_changes_button.click()
        time.sleep(2)


        
def tearDown(self):
    self.browser.quit()

    if _name_ == "_main_":
        unittest.main()
          
