
char = [input("Letra: ")[0].lower() for _ in range(10)]
cons = [c for c in char if c.isalpha() and c not in 'aeiou']
print(f"Total: {len(cons)} \n"
      f"Consoantes: {cons}")