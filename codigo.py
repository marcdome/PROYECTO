import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

PLATAFORMA = {1: "playstation-5", 2: "pc", 3: "xbox-series-x", 4: "nintendo-switch-2"}
# Primera pagina web

juego = input("Dime el juego que quieres buscar: ")
juego = juego.replace(" ", "-")
juego = juego.lower()
print(juego)
plataforma_ask = int(input("Elige la plataforma por el numero indicado:\n1 Play Station 5\n2 PC\n3 Xbox series X\n4 Nintendo Switch 2\t Opcion:"))
plataforma = PLATAFORMA[plataforma_ask]
url = f"https://www.metacritic.com/game/{juego}/critic-reviews/?platform={plataforma}"

driver = webdriver.Chrome()
driver.get(url)