import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class CriacaoTest(unittest.TestCase):
    def setUp(self):
        
        self.browser = webdriver.Chrome()
        
    def test_perfil_doador(self):
        
        self.browser.get("https://donare.azurewebsites.net/cadastro_doador/perfil_doador/")
        
        nome_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(By.ID, "nome_de_usuario"))
        nome_completo = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(By.ID, "nome_completo"))
        cpf = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(By.ID, "CPF"))
        data_nascimento = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(By.ID, "Nascimento"))
        descricao_textarea = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cadastroForm"]/div/textarea')))
        campo_data = self.browser.find_element_by_id("Nascimento")
        campo_cep = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cadastroForm"]/div/input[5]')))
        campo_rua = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(By.XPATH, '//*[@id="cadastroForm"]/div/input[6]'))
        
        # <input type="text" placeholder="Rua" required="">