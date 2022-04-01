try:
    ano = int(input('Digite o ano que deseja saber se é bissexto: '))
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f'{ano} foi/será bissexto')
    else:
        print(f'{ano} Não foi/será bissexto')
except ValueError:
    print('Apenas números')
