import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

class CriacaoPerfilDoador(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_criacao_perfil_doador(self):
        self.browser.get("https://donare.azurewebsites.net/cadastro_doador/perfil_doador")  # Substitua pela URL real
        time.sleep(2)

        # Os elementos do seu formulário de registro de doadores podem ter IDs ou XPaths diferentes
        username_input = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="nome_de_usuario"]'))
        )
        full_name_input = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="nome_completo"]'))
        )
        cpf_input = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="CPF"]'))
        )
        birthdate_input = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="Nascimento"]'))
        )
        description_input = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//textarea[@id="descricao"]'))
        )
        cep_input = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="CEP"]'))
        )
        street_input = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="Rua"]'))
        )
        number_input = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="numero"]'))
        )
        complement_input = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="complemento"]'))
        )
        neighborhood_input = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="bairro"]'))
        )
        city_input = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="cidade"]'))
        )
        state_input = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="estado"]'))
        )
        phone_input = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="telefone"]'))
        )
        email_input = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="email"]'))
        )
        password_input = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="passwordInput"]'))
        )
        terms_checkbox = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, 'terms'))
        )
        interests_button = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, 'interessesButton'))
        )

        # Preencher os dados de registro do doador
        username = 'ronaldojacare'
        full_name = 'Ronaldo Carvalho dos Santos'
        cpf = '119.495.414-60'
        birthdate = '07121979'
        description = 'Gosto de fazer boas ações!'
        cep = '52071-640'
        street = ''
        number = ''
        complement = ''
        neighborhood = ''
        city = ''
        state = ''
        phone = '8199176-4163'
        email = 'ronaldo@email.com'
        password = '1234'

        # Preencher os campos do formulário com atrasos
        username_input.send_keys(username)
        time.sleep(1)
        full_name_input.send_keys(full_name)
        time.sleep(1)
        cpf_input.send_keys(cpf)
        time.sleep(1)
        birthdate_input.send_keys(birthdate)
        time.sleep(1)
        description_input.send_keys(description)
        time.sleep(1)
        cep_input.send_keys(cep)
        time.sleep(1)
        street_input.send_keys(street)
        time.sleep(1)
        number_input.send_keys(number)
        time.sleep(1)
        complement_input.send_keys(complement)
        time.sleep(1)
        neighborhood_input.send_keys(neighborhood)
        time.sleep(1)
        city_input.send_keys(city)
        time.sleep(1)
        state_input.send_keys(state)
        time.sleep(1)
        phone_input.send_keys(phone)
        time.sleep(1)
        email_input.send_keys(email)
        time.sleep(1)
        password_input.send_keys(password)
        time.sleep(1)

         # Marcar a caixa de termos
        terms_checkbox = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, 'terms'))
        )
        terms_checkbox.click()

        # Enviar o formulário
        interests_button = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, 'interessesButton'))
        )
        interests_button.click()

        # Aguarde até que a tela de interesses seja carregada
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="interest"]'))
        )

        # Simular a seleção de três interesses
        for i in range(3):
            interest_xpath = f'//div[@class="interest"][{i + 1}]'
            interest_element = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, interest_xpath))
            )
            interest_element.click()
            time.sleep(1)  # Atraso opcional para visualização

        # Clique no botão de concluir
        confirm_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-confirm"]'))
        )
        confirm_button.click()

        # Aguarde a conclusão da ação (pode adicionar verificações adicionais aqui)
        time.sleep(2)
         # Aceitar o pop-up de alerta
        self.browser.switch_to.alert.accept()

    
    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()