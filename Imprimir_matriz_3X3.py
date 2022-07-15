lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [7,8,9]
lista_principal = []
col = 0

lista_principal.append(lista1)
lista_principal.append(lista2)
lista_principal.append(lista3)

for li in range(len(lista_principal)):
    print('{} {} {}'.format(lista_principal[li][col], lista_principal[li][col + 1], lista_principal[li][col + 2]))
