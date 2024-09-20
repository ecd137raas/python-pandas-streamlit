import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df = pd.read_csv('DadosUS.csv', sep=';')

# Convertendo as colunas de datas para o tipo datetime
df['Created Date'] = pd.to_datetime(df['Created Date'], format='%d/%m/%Y', errors='coerce')
df['Activated Date'] = pd.to_datetime(df['Activated Date'], format='%d/%m/%Y', errors='coerce')
df['Closed Date'] = pd.to_datetime(df['Closed Date'], format='%d/%m/%Y', errors='coerce')

# Ordenando o DataFrame pela coluna 'Created Date'
df_ordenado = df.sort_values(by='Created Date')

# Exibir as primeiras linhas do DataFrame ordenado
#df_ordenado.head()

# Filtrar os dados a partir de 2022
df_filtered = df_ordenado[df_ordenado['Activated Date'].dt.year >= 2023]

# Calcular o tempo médio entre 'Created Date' e 'Closed Date'
df_filtered['diff_days'] = (df_filtered['Closed Date'] - df_filtered['Activated Date']).dt.days

# Agrupar por mês e ano
df_filtered['year_month'] = df_filtered['Activated Date'].dt.to_period('M')
avg_time_per_month = df_filtered.groupby('year_month')['diff_days'].mean().reset_index()

# Converter year_month para datetime
avg_time_per_month['year_month'] = avg_time_per_month['year_month'].dt.to_timestamp()

# Plotar o gráfico de dispersão
plt.figure(figsize=(10,6))
plt.scatter(avg_time_per_month['year_month'], avg_time_per_month['diff_days'], color='blue', alpha=0.6)
plt.plot(avg_time_per_month['year_month'], avg_time_per_month['diff_days'], linestyle='-', color='blue', alpha=0.6)

# Adicionar rótulos e título
plt.xlabel('Mês/Ano')
plt.ylabel('Tempo Médio (Dias)')
plt.title('Tempo Médio entre "Activated Date" e "Closed Date" por Mês e Ano (A partir de 2022)')
plt.xticks(rotation=45)
plt.grid(True)

# Exibir o gráfico
plt.tight_layout()
plt.show()
