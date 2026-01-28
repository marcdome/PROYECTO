import pandas as pd
import matplotlib.pyplot as plt  

adzuna_data = pd.read_csv("data/adzuna_lenguajes.csv")
tiobe_data = pd.read_csv("data/tiobe_lenguajes.csv")
github_data = pd.read_csv("data/github_stats.csv")

# 1. ¿Los lenguajes más populares tienen más ofertas?
data = adzuna_data[["tecnologia", "demanda_total"]]
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

# 3. ¿Cual es la ciudad que tiene mas ofertas?

ciudades_filtradas = adzuna_data[~adzuna_data["ubicacion"].str.contains("España", na=False)]
ciudades_filtradas = ciudades_filtradas["ubicacion"]
def transformacion(p:str):
    parts = p.split(',')
    if len(parts) == 1:
        return parts[0].strip()
    else:
        for c in range(len(parts)):
           parts[c] = parts[c].strip()
        if len(parts[0]) > len(parts[1]):
            if parts[0] == "Barcelona":
                return parts[0]
            return parts[1]
        else:
            return parts[0]

adzuna_data["ubicacion"] = adzuna_data["ubicacion"].apply(transformacion)
ciudades_limpias = ciudades_filtradas.apply(transformacion)
conteo = ciudades_limpias.value_counts(ascending=False).head(11)
df_ciudades = conteo.reset_index(name="total")
df_ciudades.columns = ['ubicacion', 'total']
print(f"{df_ciudades} \n")

df_ciudades.set_index('ubicacion')['total'].plot(kind= 'bar')
plt.title('Ciudades con más ofertas de trabajo')
plt.xlabel('Ciudades')
plt.ylabel('Total')
plt.show()

# 4. ¿Que empresas ofertan más puestos de trabajo?

empresas = adzuna_data["empresa"]
empresas = empresas.value_counts().sort_values(ascending=False)
empresas = empresas.reset_index()
empresas.columns = ['empresa', 'total']
empresas = empresas.head(11)

empresas.set_index('empresa')['total'].plot(kind = 'bar')
plt.title("Empresas y su número total de ofertas")
plt.xlabel("Empresa")
plt.ylabel('Total de ofertas')
plt.show()

empresa_mas_ofertante = empresas.iloc[0]['empresa']
empresa_mas_ofertante1 = empresas.iloc[1]['empresa']
empresa_mas_ofertante2 = empresas.iloc[2]['empresa']
lista = [empresa_mas_ofertante, empresa_mas_ofertante1, empresa_mas_ofertante2]

for i in lista:
    empresas_filtradas = adzuna_data[adzuna_data["empresa"].str.contains(i, na=False)]
    ubicacion = empresas_filtradas["ubicacion"].iloc[0]
    empresas_filtradas = empresas_filtradas["tecnologia"].value_counts().sort_values(ascending=False)
    empresas_filtradas = empresas_filtradas.reset_index()
    empresas_filtradas.columns = ['Lenguaje', 'Total']
    print(f"{i}, se encuentra en {ubicacion}")
    print(f"{empresas_filtradas} \n")
    plt.figure(figsize=(10, 8))
    empresas_filtradas.set_index("Lenguaje")["Total"].plot(kind = "pie", labels=None, textprops={'fontsize': 11, 'weight': 'bold'})
    plt.title(i, fontsize=14, fontweight='bold')
    plt.ylabel('')
    total = empresas_filtradas['Total'].sum()
    etiquetas_leyenda = [f"{row['Lenguaje']} {row['Total']/total*100:.2f}%" for idx, row in empresas_filtradas.iterrows()]
    plt.legend(etiquetas_leyenda, bbox_to_anchor=(1.05, 1), loc='upper left', frameon=True)
    plt.tight_layout()
    plt.show()
    empresas_filtradas = adzuna_data

empresas_filtradas = adzuna_data[adzuna_data["empresa"].str.contains("Canonical", na=False)]
print(empresas_filtradas['titulo'])