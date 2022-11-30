a = {'hp': 45, 'attack': 49, 'defense': 49, 'special-attack': 65, 'special-defense': 65, 'speed': 45}

for chave, valor in (a.items()):
    print(chave, valor)

print([(chave, valor) for chave, valor in a.items()])
