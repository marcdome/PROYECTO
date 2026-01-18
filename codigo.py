import requests
from bs4 import BeautifulSoup
import pandas as pd

# Primera pagina web
juego = input("Dime el juego que quieres consultar: ") # Pedimos el juego
juego.replace(" ", "-")
juego.lower()
url = f"https://www.metacritic.com/game/{juego}/"
contenido = requests.get(url)
print(contenido.text)