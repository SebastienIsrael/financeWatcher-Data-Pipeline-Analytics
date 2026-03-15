import pandas as pd
import matplotlib.pyplot as plt

# 1. PRIMEIRO defina o estilo (Antes de qualquer plot)
plt.style.use('dark_background')

df = pd.read_csv('historico.csv')
df['DataHora'] = pd.to_datetime(df['DataHora'])

# 2. DEPOIS crie o gráfico definindo a cor da linha
# Use o parâmetro 'color' aqui dentro para o verde neon
ax = df.plot(x='DataHora', y='Cotacao', kind='line', 
             color='#00ff00', linewidth=2, figsize=(10, 6))

# 3. POR ÚLTIMO ajuste os detalhes de texto e grid
plt.title('Monitoramento Bitcoin - BRL', color='#00ff00')
plt.xlabel('Data/Hora')
plt.ylabel('Preço (R$)')
plt.grid(True, linestyle="--", alpha=0.2, color='gray')

plt.show()