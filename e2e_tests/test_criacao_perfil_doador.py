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