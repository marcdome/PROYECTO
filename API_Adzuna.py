import requests
import pandas as pd
import time
import json

API_KEY = "5b5d7a3ac709455f1022920b276dccf7"
API_ID = "99936c6b"


# Lista de lenguajes y búsquedas precisas para la API
lenguajes = {
    "Python": "Python",
    "Java": "Java",
    "JavaScript": "JavaScript",
    "SQL": "SQL",
    "PHP": "PHP",
    "TypeScript": "TypeScript",
    "Kotlin": "Kotlin",
    "Rust": "Rust",
    "R": "R",
    "Ruby": "Ruby",
    "Go": "Go",
    "C++": "C++"}


datos = []

for tech, busc in lenguajes.items():
    pagina = 1
    total_ofertas = 0

    while True:
        url = f"https://api.adzuna.com/v1/api/jobs/es/search/{pagina}"
        params = {
            "app_id": API_ID,
            "app_key": API_KEY,
            "what": busc,
            "results_per_page": 50
        }

        response = requests.get(url, params=params)
        data = response.json()

        jobs = data.get("results", [])
        if not jobs or pagina > 2:
            break
        print(f"First job keys: {jobs[0].keys()}")  # Debug

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
            print(f"Agregado: {job.get('title')}")  # Debug

        pagina += 1
        time.sleep(1)  # Evitar rate limits
        time.sleep(1)  # evita ser bloqueado por la API

# Guardar resultados en CSV
    print(f"Total datos para {tech}: {len(datos)}")

df = pd.DataFrame(datos)
df.to_csv("data/adzuna_lenguajes.csv", index=False)
print(df.head())