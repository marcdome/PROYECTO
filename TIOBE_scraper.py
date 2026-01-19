import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.tiobe.com/tiobe-index/'

response = requests.get(url)

# Condición por si no encuentra la pagina web 
if response.status_code != 200:
    raise RuntimeError("No se ha encontrado la pagina")

soup = BeautifulSoup(response.text, 'html.parser')

# Buscamos la etuiqueta table donde esta la clasificación
table = soup.find('table', id='top20')

# Extraemos todo menos el encabezado
rows = table.find_all('tr')[1:]
print(rows)

data = []

for row in rows: #Iteramos sobre las filas
    cols = row.find_all('td')

    if len(cols) >= 6:  # Condición para el top 20
        posicion = cols[0].text.strip()
        nombre = cols[4].text.strip()
        porcentaje = cols[5].text.strip()
        data.append([posicion, nombre, porcentaje])

    elif len(cols) >= 3:  # Para los que no son del top 20
        posicion = cols[0].text.strip()
        nombre = cols[1].text.strip()
        porcentaje = cols[2].text.strip()
        data.append([posicion, nombre, porcentaje])

# Crear el DataFrame
df = pd.DataFrame(data, columns=['Posición', 'Lenguaje', 'Porcentaje'])

# Guardar en un archivo CSV
df.to_csv('data/tiobe_lenguajes.csv', index=False)
print("Datos guardados en data/tiobe_lenguajes.csv")