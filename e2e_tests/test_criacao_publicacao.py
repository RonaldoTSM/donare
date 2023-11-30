import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class criacaoPublicacao(unittest.TestCase):
    def setUp(self):
        
        self.browser = webdriver.Chrome()
        
    def test_criacao_publicacao(self):
        
        self.browser.get('https://donare.azurewebsites.net/ong/ContaGotas/')
        
        title = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@class="form-control" and @placeholder="Título da Publicação"]')))
        descripton = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, "//textarea[@class='form-control'and @placeholder='Descrição da Publicação']")))
        time.sleep(3)
        
        
        titulo = "Ação no centro do Recife"
        descricao = "Hoje fomos fazer uma ação no centro do Recife, levando alimentos para pessoas em situação de rua!"
        
        for n in titulo:
            title.send_keys(n)
            time.sleep(0.2)
        self.assertEqual(titulo, "Ação no centro do Recife")
        time.sleep(2)
        
        for n in descricao:
            descripton.send_keys(n)
            time.sleep(0.2)
        self.assertEqual(descricao, "Hoje fomos fazer uma ação no centro do Recife, levando alimentos para pessoas em situação de rua!")
        time.sleep(2)
        
        publish = self.browser.find_element(By.XPATH, '//button[@class="btn btn-success" and text()="Publicar"]')
        publish.click()    
        time.sleep(4)
        
def tearDown(self):
    self.browser.quit()

    if _name_ == "_main_":
        unittest.main()