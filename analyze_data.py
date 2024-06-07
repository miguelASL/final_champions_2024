import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Datos de Defensores
data_defensores = {
    'Defensor': ['Carvajal', 'Éder Militão', 'Nacho', 'Antonio Rüdiger', 'Ferland Mendy', 'Total'],
    'Asistencias de gol': [23, 0, 43, 41, 35, 142],
    'Pérdidas de balón': [9, 0, 10, 4, 6, 29],
    'Centros y corners': [13, 1, 8, 6, 9, 37],
    'Pases': [17, 1, 6, 6, 9, 39]
}

df_defensores = pd.DataFrame(data_defensores)

# Datos de Mediocampistas
data_mediocampistas = {
    'Mediocentro': ['Jude Bellingham', 'Toni Kroos', 'Luka Modric', 'Eduardo Camavinga', 'Federico Valverde', 'Lucas Vázquez', 'Aurélien Tchouaméni', 'Total'],
    'Asistencias de gol': [5, 2, 0, 1, 0, 1, 0, 9],
    'Pases acertados': [368, 882, 391, 501, 607, 271, 412, 3632],
    'Pases fallados': [200, 50, 150, 1, 3, 6, 8, 418],
    'Centros y corners': [14, 45, 32, 1, 10, 20, 5, 127],
}

df_mediocampistas = pd.DataFrame(data_mediocampistas)

# Datos de Delanteros
data_delanteros = {
    'Delantero': ['Vinícius Júnior', 'Rodrygo', 'Joselu', 'Total'],
    'Goles': [6, 5, 5, 16],
    'Tiros': [24, 28, 25, 77],
    'Bloqueos': [14, 8, 3, 25],
    'Tiros fuera': [11, 9, 16, 36]
}

df_delanteros = pd.DataFrame(data_delanteros)

# Función para análisis descriptivo
def analyze_and_print(df, title):
    print(f"Análisis Descriptivo de {title}:")
    print(df.drop(df.columns[0], axis=1).describe().apply(lambda x: x.apply("{:,.2f}".format))) # Uso de map en lugar de applymap

# Análisis descriptivo para Defensores
analyze_and_print(df_defensores, "Defensores")

# Análisis descriptivo para Mediocampistas
analyze_and_print(df_mediocampistas, "Mediocampistas")

# Análisis descriptivo para Delanteros
analyze_and_print(df_delanteros, "Delanteros")

# Gráficas
sns.set(style="whitegrid")
plt.figure(figsize=(12, 10))

# Defensores
plt.subplot(3, 1, 1)
sns.barplot(x='Defensor', y='Centros y corners', data=df_defensores[df_defensores['Defensor'] != 'Total'], palette="Blues")
plt.title('Centros y corners de Defensores')
plt.xlabel('Defensor')
plt.ylabel('Centros y corners')

# Mediocampistas
plt.subplot(3, 1, 2)
sns.barplot(x='Mediocentro', y='Pases acertados', data=df_mediocampistas[df_mediocampistas['Mediocentro'] != 'Total'], palette="Reds", label="Pases acertados")
sns.barplot(x='Mediocentro', y='Pases fallados', data=df_mediocampistas[df_mediocampistas['Mediocentro'] != 'Total'], palette="Oranges", label="Pases fallados")
plt.title('Pases de Mediocampistas')
plt.xlabel('Mediocentro')
plt.ylabel('Pases')
plt.legend()

# Delanteros
plt.subplot(3, 1, 3)
sns.barplot(x='Delantero', y='Tiros', data=df_delanteros[df_delanteros['Delantero'] != 'Total'], palette="Greens")
plt.title('Tiros de Delanteros')
plt.xlabel('Delantero')
plt.ylabel('Tiros')

plt.tight_layout()
plt.show()