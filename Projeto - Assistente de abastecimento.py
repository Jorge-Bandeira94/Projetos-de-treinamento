from time import sleep
print(40*'-=-')
print('Bem vindo ao assistente automático para abastecimento')
sleep(2)
print('Cobramos 0,15 R$ para cada litro utilizado em vazão menor que 50 L/s e 0.30 R$ para vazão acima de 50 L/s')
print(40*'-=-')
sleep(2)


l1 = float(input('Digite a vazão (l/s) desejada para o bombeamento de água: '))
l2 = float(input('Digite a capacidade máxima em litros de sua piscina: '))
l3 = float(input('Digite a quantidade de água média que a piscina já comporta, caso não haja, use o valor zero: '))

a1 = l1
a2 = l2
a3 = l3
while a3 < a2:
    sleep(1)
    a3 = a3 + a1
    if a3 > a2:
        a3 = a3 - a1
        break
    print('Já foram depositados {} litros na psicina'.format(a3))
print('\nA piscina está com sua capacidade total de água: {} Litros'.format(a2))
print(40*'-=-','\n')
sleep(1)

if l1 < 50:
    a4 = a3 - l3
    b1 = a4 * 0.15
    print('O total a pagar por este serviço, para vazão {} L/s, é de R$ {:.2f}'.format(l1, b1))
else:
    a4 = a3 - l3
    b2 = a4 * 0.30
    print('O total a pagar por este serviço, para vazão {} L/s, é de R$ {:.2f}'.format(l1, b2))