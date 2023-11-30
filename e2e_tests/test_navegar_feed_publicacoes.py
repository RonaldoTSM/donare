from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Inicializa o driver do navegador (certifique-se de ter o driver apropriado instalado e no PATH)
driver = webdriver.Chrome()

try:
    # Abre a página web
    driver.get("https://donare.azurewebsites.net/doador/tuzi/")  # Substitua isso pela URL real da sua aplicação

    # Move para o topo da página
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.HOME)
    time.sleep(1)  # Aguarda um momento após o movimento para o topo

    # Define a altura da janela de visualização
    window_height = driver.execute_script("return window.innerHeight;")
    
    # Rola a tela até o final da página
    total_height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")

    # Define a quantidade de rolagens (ajuste conforme necessário)
    num_scrolls = total_height // window_height

    for _ in range(num_scrolls):
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        time.sleep(2)  # Ajuste conforme necessário para a velocidade desejada (aumentado para 2 segundos)

    # Aguarda um tempo extra para garantir que todas as publicações sejam carregadas
    time.sleep(2)

finally:
    # Fecha o navegador ao finalizar o teste
    driver.quit()
