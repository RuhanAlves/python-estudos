time = ('Flamengo', 'Palmeiras', 'Atletica Parananese',
        'Fluminense', 'Bahia', 'Cruzeiro', 'Coritiba',
        'Atletico-MG', 'RB Bragantino', 'São Paulo',
        'Vitoria', 'Corinthians', 'Santos', 'Botafogo',
        'Gremio', 'Mirassol', 'Vasco Da Gama', 'Internacional',
        'Remo', 'Chapecoense-sc')
print(f'Cinco primeiros colocados do Brasileirão: {time[:5]}\n')
print(f'Últimos quatro colocados: {time[-4:]}\n')
print(f'Times em ordem alfabética: {sorted(time)}\n')
print(f'A Chapecoense se encontra na {time.index("Chapecoense-sc") + 1}ª posição')
