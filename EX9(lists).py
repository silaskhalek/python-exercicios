
numeros = [1,2,3,4,5,6,7,8,9,10]
nomes = ['Silas','Paloma','Joathan','Kaleby']
dobs = [2000,2024]

numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
    print(numero)

nomes = ['Silas','Paloma','Joathan','Kaleby']
for nome in nomes:
    print(nome)

dobs = [2000,2024]
for dob in dobs:
    print(dob)

soma_impares = 0
for i in range(1, 11, 2):
    soma_impares += i
print(soma_impares)

for i in range(10, -1, -1):
    print(i)

numero_tabuada = int(input('Digite um número para a tabuada: '))
for i in range(1,11):
    resultado = numero_tabuada * i
    print(f'{numero_tabuada} x {i} = {resultado}')

lista_numeros = [10, 5, 8, 3, 7]
soma = 0

try:
    for numero in lista_numeros:
        soma += numero
    print(f'A soma dos elementos é {soma}')
except Exception as e:
    print(f'Ocorreu um erro: {e}')

lista_valores = [15,20,25,30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor 
    media = soma_valores / len(lista_valores)
    print(f'Média dos valores é: {media}')
except ZeroDivisionError:
    print('A lista está vazia, não é possível calcular a média.')
except Exception as e:
    print(f'Ocorreu um erro: {e}')


