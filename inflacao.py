
# importação das bilbiotecas necessárias e funções
from bcb import sgs # biblioteca que extrar os dados da inflação do banco central
import matplotlib.pyplot as plt
import mplcyberpunk

# função importa os dados do ipca
serie_ipca = sgs.get(433, start = "2023-01-01", end = "2025-02-01")


# Renomear o nome da coluna 433 para valores
serie_ipca.rename(columns={'433': 'valores'}, inplace=True)

# aplicar estilo cyberpunk
plt.style.use("cyberpunk")

# Criar o gráfico do IPCA
grafico = serie_ipca.plot(
    figsize=(10,5),
    title="IPCA ao longo do Tempo",
    legend=False,
    xlabel="Tempo (Meses)",
    ylabel="Inflação (%)",
    marker = "o"
)

# Adicionar rótulos nos pontos do gráfico
for valor, data in zip(serie_ipca['valores'], serie_ipca.index):
    grafico.annotate(f"{valor:.2f}%", xy=(data, valor),
    xytext=(0,10), textcoords="offset points", ha = "center", fontsize =10,color = "white")
    
# adicionar efeitos especiais do mplcyberpunk
mplcyberpunk.add_glow_effects()

# Exibir o gráfico
plt.show()

