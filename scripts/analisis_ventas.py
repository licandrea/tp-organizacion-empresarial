
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../datos/ventas.csv")

df["total"] = df["cantidad"] * df["precio"]

ventas_totales = df["total"].sum()

print("Ventas Totales:", ventas_totales)

ventas = df.groupby("producto")["total"].sum()

ventas.plot(kind="bar")

plt.title("Ventas por Producto")

plt.savefig("../resultados/grafico_ventas.png")

print("Gráfico generado correctamente")
