def telegrafo(a):
    total = 0
    cadena = list(a.lower())

    for i in cadena:
        for j in range(97,123): 
            if i == chr(j):
                total = total + 10
        for k in range(48,58):
            if i == chr(k):
                total = total + 20
        for l in range(123,166): 
            if i == chr(l):
                total = total + 30
        for m in range(33, 48):
            if i == chr(m):
                total = total + 30
    return total


texto = "Feliz Aniversario!"
costo = telegrafo(texto)
print(f"Su mensaje cuesta ${costo}")