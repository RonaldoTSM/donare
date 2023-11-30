import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time


class criacaoPerfilOng(unittest.TestCase):
    def setUp(self):
        
        self.browser = webdriver.Chrome()
        
    def test_criacao_perfil_ong(self):
        
        self.browser.get("https://donare.azurewebsites.net/")
        time.sleep(2)
        
        ong_button = self.browser.find_element(By.ID, "ongButton")
        ong_button.click()
        time.sleep(2)
        
        user_name_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@id="nome_de_usuario"]')))
        ong_name_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@id="nome_completo"]')))
        cnpj_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@id="cnpj"]')))
        category_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//select[@id="categoria" and @name="categoria"]')))
        descripton_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//textarea[@id="descricao"]')))
        cep_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@id="cep"]')))
        street_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@id="rua"]')))
        number_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@id="numero"]')))
        complement_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@id="complemento"]')))
        phone_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@id="telefone" and @name="telefone"]')))
        email_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@id="email"]')))
        password_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@id="passwordInput"]')))
        
        
        nome = 'Samaritanos'
        ong = 'Samaritanos'
        cnpj = '12288745000107'
        categoria = 'PSR'
        descricao = 'Somos uma ONG dedicada à causa dos PSR, e temos como objetivo ajudar pessoas em situação de rua'
        cep = '52071640'
        numero = '50'
        complemento = 'apartamento 1201'
        telefone = '81991764163'
        email = 'samaratinos@email.com'
        senha = '1234'
        
        
        
        select = Select(category_input)  
        select.select_by_visible_text(categoria)
        terms_checkbox = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, 'terms')))
    
                
        
        for n in nome:
            user_name_input.send_keys(n)
            time.sleep(0.1)
        self.assertEqual(nome, 'Samaritanos')
        time.sleep(2)
        
        
        for n in ong:
            ong_name_input.send_keys(n)
            time.sleep(0.1)
        self.assertEqual(ong, 'Samaritanos')
        time.sleep(2)
        
        for n in cnpj:
            cnpj_input.send_keys(n)
            time.sleep(0.1)
        self.assertEqual(cnpj, '12288745000107')
        time.sleep(2)
        
        for n in descricao:
            descripton_input.send_keys(n)
            time.sleep(0.1)
        self.assertEqual(descricao, 'Somos uma ONG dedicada à causa dos PSR, e temos como objetivo ajudar pessoas em situação de rua')
        time.sleep(2)
        
        for n in cep:
            cep_input.send_keys(n)
            time.sleep(0.1)
        self.assertEqual(cep, '52071640')
        time.sleep(2)

        for n in numero:
            number_input.send_keys(n)
            time.sleep(0.1)
        self.assertEqual(numero, '50')
        time.sleep(2)

        for n in complemento:
            complement_input.send_keys(n)
            time.sleep(0.1)
        self.assertEqual(complemento, 'apartamento 1201')
        time.sleep(2)

        for n in telefone:
            phone_input.send_keys(n)
            time.sleep(0.1)
        self.assertEqual(telefone, '81991764163')
        time.sleep(2)

        for n in email:
            email_input.send_keys(n)
            time.sleep(0.1)
        self.assertEqual(email, 'samaratinos@email.com')
        time.sleep(2)

        for n in senha:
            password_input.send_keys(n)
            time.sleep(0.1)
        self.assertEqual(senha, '1234')
        time.sleep(2)
        
        terms_checkbox.click()
        time.sleep(2)

        create_ong_button = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//button[@id="dadosBancariosButton"]')))
        create_ong_button.click()
        time.sleep(2)
        
        
        self.browser.get('https://donare.azurewebsites.net/cadastro_ong/dados_bancarios/')
        
        nome_titular_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@id="nome_titular"]')))
        bank_account_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@id="conta"]')))
        agency_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@id="agencia"]')))
        bank_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@id="banco"]')))
        type_account_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@id="tipoConta"]')))
        agency_city = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@id="cidade"]')))
        agency_state_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@id="estado"]')))
        pix_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@id="pix"]')))
        observation_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//textarea[@id="obs"]'))) 
        
        
        conta_bancaria = '117882969'
        agencia = '111'
        banco = 'NUBANK'
        tipo_conta = 'Corrente'
        cidade_agencia = 'Recife'
        estado_agencia = 'PE'
        chave_pix = '12842003454'
        observacoes = 'conta bancaria da ONG samaritanos'
        
        
        
        for n in nome:
            nome_titular_input.send_keys(n)
            time.sleep(0.1)
        self.assertEqual(nome, 'Samaritanos')
        time.sleep(2)
    
        for n in conta_bancaria:
            bank_account_input.send_keys(n)
            time.sleep(0.1)
        self.assertEqual(conta_bancaria, '117882969')
        time.sleep(2)

        for n in agencia:
            agency_input.send_keys(n)
            time.sleep(0.1)
        self.assertEqual(agencia, '111')
        time.sleep(2)

        for n in banco:
            bank_input.send_keys(n)
            time.sleep(0.1)
        self.assertEqual(banco, 'NUBANK')
        time.sleep(2)

        for n in tipo_conta:
            type_account_input.send_keys(n)
            time.sleep(0.1)
        self.assertEqual(tipo_conta, 'Corrente')
        time.sleep(2)

        for n in cidade_agencia:
            agency_city.send_keys(n)
            time.sleep(0.1)
        self.assertEqual(cidade_agencia, 'Recife')
        time.sleep(2)

        for n in estado_agencia:
            agency_state_input.send_keys(n)
            time.sleep(0.1)
        self.assertEqual(estado_agencia, 'PE')
        time.sleep(2)

        for n in chave_pix:
            pix_input.send_keys(n)
            time.sleep(0.1)
        self.assertEqual(chave_pix, '12842003454')
        time.sleep(2)
        
        
        for n in observacoes:
            observation_input.send_keys(n)
            time.sleep(0.1)
        self.assertEqual(observacoes, 'conta bancaria da ONG samaritanos')
        time.sleep(2)
        
        send_information_button = self.browser.find_element(By.XPATH, '//button[@type="submit" and text()="Enviar Informações"]')
        send_information_button.click()
        time.sleep(2)


        self.browser.get('https://donare.azurewebsites.net/ong/Samaritanos/')
        time.sleep(4)


        
def tearDown(self):
    self.browser.quit()

if __name__ == "_main_":
    unittest.main()
        
                

