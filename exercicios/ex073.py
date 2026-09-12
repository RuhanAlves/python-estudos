time = ('Flamengo', 'Palmeiras', 'Atletica Parananese', 'Fluminense', 'Bahia', 'Cruzeiro', 'Coritiba', 'Atletico-MG', 'RB Bragantino', 'São Paulo', 'Vitoria', 'Corinthians', 'Santos', 'Botafogo', 'Gremio', 'Mirassol', 'Vasco Da Gama', 'Internacional', 'Remo', 'Chapecoense-sc')
print(f'Cinco primeiros colocados do Brasileirão: \n{time[:5]}')
print(f'Últimos quatro colocados: \n{time[-4:]}')
#Falta a c, ordem alfabética
print(f'Times em ordem alfabética: \n{sorted(time)}')
for c in range (0, len(time)):
    if time[c] == 'Chapecoense-sc':
        print(f'A Chapecoense se encontra na {c + 1}ª posição')