valor = float(input('Digite o valor médio que deseja pagar por aluguel: R$ '))

if valor < 400:
    a1 = 'Jardim São Paulo'
    a2 = 'Jordão'
    a3 = 'Casa Amarela'
    print(a1)
    print(a2)
    print(a3)
    bairro1 = input('Escolha entre os bairros acima:').strip().title()
    if bairro1 == a1:
        print('Uma casa em {} vale R$250,00 / mês '.format(a1))
    elif bairro1 == a2:
        print('Uma casa em {} vale R$150,00 / mês '.format(a2))
    elif bairro1 == a3:
        print('Uma casa em {} vale R$350,00 / mês '.format(a3))
elif 1000 > valor > 400 :
    b1 = 'Campo Grande'
    b2 = 'Rosarinho'
    b3 = 'Várzea'
    print(b1)
    print(b2)
    print(b3)
    bairro2 = input('Escolha entre os bairros acima: ').strip().title()
    if bairro2 == b1:
        print('Uma casa em {} vale R$450,00 / mês '.format(b1))
    elif bairro2 == b2:
        print('Uma casa em {} vale R$650,00 / mês '.format(b2))
    elif bairro2 == b3:
        print('Uma casa em {} vale R$950,00 / mês '.format(b3))
else:
    print('Não foram encontrados imóveis nos valore sespecíficados')
