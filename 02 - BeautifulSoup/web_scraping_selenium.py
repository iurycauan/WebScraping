from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver

navegador = webdriver.Firefox()

navegador.get('https://www.walissonsilva.com/blog')

sleep(3)

elemento = navegador.find_element(By.TAG_NAME, 'input')

elemento.send_keys('data')