a = int(input("Coeficiente A: "))
b = int(input("Coeficiente B: "))
c = int(input("Coeficiente C: "))
d = int(input("Coeficiente D: "))
e = int(input("Coeficiente E: "))
f = int(input("Coeficiente F: "))

ce = c * e
bf = b * f

af = a * f
cd = c * d

ae = a * e
bd = b * d

x = (ce - bf) / (ae - bd)

y = (af - cd) / (ae - bd)

c = a * x + b * y
f = d * x + e * y

print(f"X = {x} || Y = {y}")

print(f"ax + by = {c}")
print(f"dx + ey = {f}")

