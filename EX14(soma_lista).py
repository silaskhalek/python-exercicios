lista_numeros = [10, 5, 8, 3, 7]
soma = 0

try:
    for numero in lista_numeros:
        soma += numero
    print(f'A soma dos elementos é {soma}')
except Exception as e:
    print(f'Ocorreu um erro: {e}')