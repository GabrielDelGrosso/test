try:
    salario = float(input('Digite seu salário: '))
    s20 = float(salario + (salario * 20 / 100))
    s15 = float(salario + (salario * 15 / 100))
    s5 = float(salario + (salario * 5 / 100))

    if salario <= 280:
        print(f'Seu salario atual é {salario}. Você obteve um reajuste de 20% e seu novo salario será {s20}')
    elif salario >= 280 and salario <= 700:
        print(f'Seu salario atual é {salario}. Você obteve um reajuste de 15% e seu novo salario será {s15}')
    elif salario > 1500:
        print(f'Seu salario atual é {salario}. Você obteve um reajuste de 5% e seu novo salario será {s5}')
except ValueError:
    print('Apenas números.')

