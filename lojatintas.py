area_pintada = input('Digite a área a ser pintada em m²: ')


if not area_pintada.isnumeric():
    print('Somente números!')
else:
    litro = int(area_pintada)/ 3
    latas = 18
    preco = 80
    quantidade_latas = litro / latas
    total = quantidade_latas * preco
    print(f'Você precisará de {quantidade_latas:.2f} latas.')
    print(f'O preço final é R${total:.2f}')