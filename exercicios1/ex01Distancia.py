import math
import matplotlib.pyplot as plt
import numpy as np

x1 = float(input("Digite o primeiro ponto da reta X P1:"))
x2 = float(input("Digite o primeiro ponto da reta X P2:"))
y1 = float(input("Digite o primeiro ponto da reta Y P1:"))
y2 = float(input("Digite o primeiro ponto da reta Y P2:"))

dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"A distancia entre eles é: {dist}")



