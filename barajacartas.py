import random


num_jugadores = int(
    input('¿Cuántos jugadores participareis en esta partida? 10'))
palos = ['Oros', 'Copas', 'Espadas', 'Bastos']
numeros = ['1', '2', '3', '4', '5', '6', '7', 'SOTA', 'CABALLO', 'REY']

baraja_espanola = []

for palo in (palos):
    for numero in (numeros):
        carta = '{} de {}'.format(numero, palo)
        baraja_espanola. append(carta)
'''num_carta = len(baraja_espanola)'''
'''for i in range(0, 40, 4):
    print('{}       {}      {}      {}'.format(baraja_espanola[i], baraja_espanola[i + 1], baraja_espanola[i + 2], baraja_espanola[i + 3]))'''

for i in range(0, 40, 4):
    for j in range(4):
        baraja_mezclada = random.sample(baraja_espanola, len(baraja_espanola))
'''print(baraja_mezclada)'''

mano = [baraja_mezclada[i::num_jugadores] for i in range(num_jugadores)]

inicio_partida = None
for i, mano in enumerate(mano, 1):
    print('Jugador', i, ':', mano)
    if '2 de Oros' in mano:
        inicio_partida = i

if inicio_partida is not None:
    print('El jugador', inicio_partida, 'empieza da partida')
else:
    print('La carta de 2 de oros no se encuentra, ¿Desea repartir de nuevo?')

'''print(baraja_espanola)'''
