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

    # Rola a tela até o final da página
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(7)  # Aguarda 7 segundos na parte inferior

    # Rola de volta lentamente para o topo
    total_height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")
    window_height = driver.execute_script("return window.innerHeight;")
    num_scrolls_up = total_height // window_height

    for _ in range(num_scrolls_up):
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_UP)
        time.sleep(2)  # Ajuste conforme necessário para a velocidade desejada (aumentado para 2 segundos)

    # Aguarda um tempo extra para garantir que todas as publicações sejam carregadas
    time.sleep(2)

finally:
    # Fecha o navegador ao finalizar o teste
    driver.quit()
