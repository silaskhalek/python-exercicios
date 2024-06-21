x = float(input('Digite a coordenada x: '))
y = float(input('Digite a coordenada y: '))

if x > 0 and y > 0:
    print('O ponto está no 1º quadrante.')
elif x < 0 and y > 0:
    print('O ponto está no 2º quadrante.')
elif x < 0 and y < 0:
    print('O ponto está no 3º quadrante.')
elif x > 0 and y < 0:
    print('O ponto está no 4º quadrante.')
else: 
    print('O ponto está localizado no eixo ou origem.')