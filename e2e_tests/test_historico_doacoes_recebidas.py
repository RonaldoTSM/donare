from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inicializa o driver do navegador (certifique-se de ter o driver apropriado instalado e no PATH)
driver = webdriver.Chrome()

try:
    # Abre a página web
    driver.get("https://donare.azurewebsites.net/ong/ContaGotas/")

    # Encontrar o elemento do container da direita
    right_container = driver.find_element(By.CLASS_NAME, 'right-column')

    # Use JavaScript para obter a altura total do container
    total_height = driver.execute_script("return arguments[0].scrollHeight;", right_container)

    # Número de rolagens desejado
    num_scrolls = 10

    # Intervalo de tempo entre rolagens
    scroll_delay = 1  # segundos

    for _ in range(num_scrolls):
        # Calcula a posição de rolagem para cada passo
        scroll_position = total_height * (_ + 1) / num_scrolls

        # Rola o container da direita para a posição calculada usando JavaScript
        driver.execute_script("arguments[0].scrollTop = arguments[1]", right_container, scroll_position)

        # Aguarda o intervalo de tempo entre rolagens
        time.sleep(scroll_delay)

    # Aguarde um tempo (10 segundos, conforme solicitado)
    time.sleep(10)

finally:
    # Fecha o navegador ao finalizar o teste
    driver.quit()
