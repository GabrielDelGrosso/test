lista = []

lista.append(('produto 1 ', 10))
lista.append(('produto 2', 50))
lista.append(('produto 3', 40))


total = sum([float(y) for x, y in lista])
print(total)