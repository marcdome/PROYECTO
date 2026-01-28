import requests
import pandas as pd
import time


API_KEY = "" # Hay que poner las claves personales 
API_ID = ""


# Lista de lenguajes y búsquedas precisas para la API

csv = pd.read_csv("data/tiobe_lenguajes.csv")
lenguajes = csv["Lenguaje"]
datos = []

for tech in lenguajes:
    pagina = 1
    total_ofertas = 0

    while True:
        url = f"https://api.adzuna.com/v1/api/jobs/es/search/{pagina}"
        params = {
            "app_id": API_ID,
            "app_key": API_KEY,
            "what": tech,
            "results_per_page": 50
        }

        response = requests.get(url, params=params)
        data = response.json()

        jobs = data.get("results", [])
        if not jobs:
            break

        # Contar demanda total solo una vez
        total_ofertas = data.get("count", 0)

        for job in jobs:
            salary_min = job.get("salary_min")
            salary_max = job.get("salary_max")

            salario_medio = None
            if salary_min is not None and salary_max is not None:
                salario_medio = (salary_min + salary_max) / 2

            datos.append({
                "tecnologia": tech,
                "titulo": job.get("title"),
                "empresa": job.get("company", {}).get("display_name"),
                "ubicacion": job.get("location", {}).get("display_name"),
                "salario_medio": salario_medio,
                "demanda_total": total_ofertas
            })
            print(f"Agregando {job.get("title")} a {tech}\n")
        pagina += 1
        time.sleep(1)
        time.sleep(1)  # evita ser bloqueado por la API

# Guardar resultados en CSV
    print(f"Total datos para {tech}: {len(datos)}")

df = pd.DataFrame(datos)
df.to_csv("data/adzuna_lenguajes.csv", index=False)
