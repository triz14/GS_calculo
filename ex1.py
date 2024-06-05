import matplotlib.pyplot as plt
import numpy as np 

# Dados que ja possuimos
anos = np.array([0, 1, 2, 3])
num_animais = np.array([1190, 1155, 1030, 1015])

# Ajuste da curva quadrática(2º grau)
coeficiente = np.polyfit(anos, num_animais, 2)

# Função quadrática
def f_quadratica(t):
    return coeficiente[0] * t ** 2 + coeficiente[1] * t + coeficiente[2]

# Dados na curva ajustada
def ajustar_curva(f_quadratica, anos, num_animais, titulo = "Função quantidade de espécimes", legenda = "N(t)"):
    t = np.linspace(0, 10, 200)
    F = f_quadratica(t)

    plt.figure(figsize=(11,7))
    plt.plot(t, F, label = legenda)
    plt.scatter(anos, num_animais, color = "blue", label = "Dados informados")
    plt.title(titulo)
    plt.xlabel("Anos")
    plt.ylabel("Numeros espécimes")
    plt.legend()
    plt.grid(True)
    plt.show()

print(f"Coeficiente: a = {coeficiente[0]}, b = {coeficiente[1]}, c = {coeficiente[2]}")
print(f"Estimativas de animais no 5º ano : {f_quadratica(5)}")

ajustar_curva(f_quadratica, anos, num_animais)
    