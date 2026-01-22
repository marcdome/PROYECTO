import requests
import pandas as pd
import time


# token personal de GitHub para hacer mas requests 
GITHUB_TOKEN = "" 

headers = {}
if GITHUB_TOKEN:
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}

# 1. Cargamos la lista de lenguajes generada por el script de TIOBE
try:
    df = pd.read_csv("data/tiobe_lenguajes.csv")
except FileNotFoundError:
    print("Error: El archivo 'data/tiobe_lenguajes.csv' no existe. ")
    exit()

# 2. Diccionario para mapear nombres de TIOBE a los que usa GitHub porque no coinciden exactamente
name_mapping = {
    "C programming language": "C",
    "Delphi/Object Pascal": "Pascal",
    "Visual Basic": "Visual Basic .NET",
    "C#": "csharp",                   
    "Ada programming language": "Ada", 
    "Assembly language": "Assembly",   
    "Scratch": "Scratch",             
    "C++": "cpp"
    #se pueden añadir mas mapeos si es necesario 
    }

repo_data = []

for index, row in df.iterrows():
    original_name = row['Lenguaje']
    
    # Usamos el nombre corregido si existe en el diccionario, si no, usamos el original
    query_name = name_mapping.get(original_name, original_name)
    
    # Construimos la URL de búsqueda en la API de GitHub
    # 'q=language:"Python"' busca repositorios donde el lenguaje PRINCIPAL sea Python
    url = f"https://api.github.com/search/repositories?q=language:\"{query_name}\""
    
    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            # 'total_count' nos dice cuántos repositorios existen en total
            count = data.get('total_count', 0)
            
            print(f"{original_name} (buscado como '{query_name}'): {count} repositorios")
            
            repo_data.append({
                'tecnologia': original_name, # Guardamos el nombre original para poder cruzar los datos luego
                'github_repos': count
            })
            
        elif response.status_code == 403:
            print("Error 403: Límite de peticiones excedido (Rate Limit).")

            break
        else:
            print(f"Error inesperado {response.status_code} para {original_name}")
            repo_data.append({
                'tecnologia': original_name, # Guardamos el nombre original para poder cruzar los datos luego
                'github_repos': 0
            })
            
    except Exception as e:
        print(f"Error de conexión para {original_name}: {e}")

    # Pausa de 2 segundos para no saturar la API y evitar bloqueos
    time.sleep(2) 

# 3. Guardar resultados en un archivo CSV
if repo_data:
    df_github = pd.DataFrame(repo_data)
    df_github.to_csv("data/github_stats.csv", index=False)
    print("\n¡Proceso terminado! Datos guardados en 'data/github_stats.csv'")
else:
    print("\nNo se han extraído datos. Revisa tu conexión o el token.")