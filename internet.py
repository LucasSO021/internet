import matplotlib.pyplot as plt

# Dados fictícios de acesso à internet por estado (% da população)
acesso_por_estado = {
    "SP": 88,
    "RJ": 85,
    "MG": 80,
    "RS": 78,
    "PR": 76,
    "SC": 82,
    "BA": 65,
    "PE": 60,
    "CE": 62,
    "PA": 55,
    "MA": 50,
    "GO": 75,
    "DF": 90,
    "ES": 77,
    "AM": 58,
    "RN": 64,
    "PB": 63,
    "PI": 52,
    "AL": 54,
    "SE": 60
}

# Separando os dados para o gráfico
estados = list(acesso_por_estado.keys())
valores = list(acesso_por_estado.values())

# Criar o gráfico
plt.figure(figsize=(14, 7))
plt.bar(estados, valores, color='mediumseagreen')

# Títulos e legendas
plt.title("Acesso à Internet por Estado no Brasil (%)", fontsize=16)
plt.xlabel("Estados", fontsize=12)
plt.ylabel("Percentual da População com Acesso (%)", fontsize=12)
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Exibir os valores no topo de cada barra
for i, valor in enumerate(valores):
    plt.text(i, valor + 1, f'{valor}%', ha='center', fontsize=9)

# Finalizar
plt.tight_layout()
plt.savefig("acesso_internet_por_estado.png", dpi=300)
plt.show()
