import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

class CriacaoPublicacao(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_criacao_publicacao(self):
        self.browser.get('https://donare.azurewebsites.net/doador/aadf/')
        time.sleep(2)
        
        # Corrigindo as aspas dentro da string de XPath
        xpath = "//button[contains(@class, 'btn btn-primary') and contains(@onclick, \"openDonationPopup('ONG Conta Gotas', 'ContaGotas')\")]"
        doar_button = self.browser.find_element(By.XPATH, xpath)
        doar_button.click()
        time.sleep(2)
        
        doacao = self.browser.find_element(By.XPATH, '//input[@id="valorDoacao"]')
        doacao.click()
        time.sleep(2)

        valor_digitado = "100,00"

        for n in valor_digitado:
            doacao.send_keys(n)
            time.sleep(0.2)

        forma_pagamento_dropdown = self.browser.find_element(By.XPATH, '//select[@id="formaPagamento"]')
        select = Select(forma_pagamento_dropdown)
        select.select_by_visible_text("Depósito Bancário ou PIX")
        time.sleep(2)

        confirmar_doacao_button = self.browser.find_element(By.XPATH, "//button[contains(@class, 'btn btn-primary') and contains(@onclick, \"confirmarDoacao('aadf')\")]")
        confirmar_doacao_button.click()
        time.sleep(2)

        confirm_button = self.browser.find_element(By.XPATH, "//button[@class='btn btn-primary' and @onclick='confirmarDeposito()']")
        time.sleep(1)
        confirm_button.click()
        time.sleep(2)

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()
