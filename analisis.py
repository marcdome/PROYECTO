import pandas as pd
import matplotlib.pyplot as plt  

azuna_data = pd.read_csv("data/adzuna_lenguajes.csv")
tiobe_data = pd.read_csv("data/tiobe_lenguajes.csv")
github_data = pd.read_csv("data/github_stats.csv")

# 1. ¿Los lenguajes más populares tienen más ofertas?
data = azuna_data[["tecnologia", "demanda_total"]]
data = data.drop_duplicates()
data = data.sort_values("demanda_total", ascending= False)

# Graficar demanda_total por tecnologia
data.set_index('tecnologia')['demanda_total'].plot(kind='bar')
plt.title("Demanda Total por Lenguaje de Programación")
plt.xlabel("Lenguaje de programación")
plt.ylabel("Demanda Total")
plt.show()

data2 = tiobe_data[["Lenguaje", "Porcentaje"]]
data2["Porcentaje"] = data2["Porcentaje"].str.rstrip('%').astype(float)

data2.set_index('Lenguaje')['Porcentaje'].plot(kind = 'bar')
plt.title('Posiciones de los lenguajes más populares')
plt.xlabel("Lenguaje de programación")
plt.ylabel("Popularidad")
plt.show()

# 2. ¿Los lenguajes mas populares tiene más repositorios?

data3 = github_data.sort_values("github_repos", ascending=False)

data3.set_index('tecnologia')['github_repos'].plot(kind = 'bar')
plt.title('Repositorios de Github por cada lenguaje')
plt.xlabel('Lenguaje de programación')
plt.ylabel('Total de repositorios')
plt.show()

