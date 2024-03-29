import requests
from bs4 import BeautifulSoup
from selenium import webdriver

response = requests.get('https://www.airbnb.com.br/')

site = BeautifulSoup(response.text, 'html.parser')

print(site.prettify())