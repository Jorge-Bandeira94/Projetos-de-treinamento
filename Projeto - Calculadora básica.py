def multiplicação(m1, m2):
    m3 = m1 * m2
    print('{} * {} = {}'.format(m1, m2, m3))
def soma(s1, s2):
    s3 = s1 + s2
    print(' {} + {} = {}'.format(s1, s2, s3))
def subtração(sub1, sub2):
    sub3 = sub1 - sub2
    print('{} - {} = {} '.format(sub1, sub2, sub3))
def divisão(d1, d2):
    d3 = d1 / d2
    print('{} / {} = {}'.format(d1, d2, d3))

print(17*'-=-')
print(5*'-=-', 'Calculadora básica', 5*'-=-')
print(17*'-=-','\n')
print('Escolha a operação digitando o número correspondente')
print('Soma [1], Subtração [2], Divisão [3], Multiplicação [4]')
a = float(input(''))
if a == 1:
    print('SOMA')
    op1 = float(input('Digite o primeiro número: '))
    op2 = float(input('Digite o segundo número: '))
    soma(op1, op2)
elif a == 2:
    print('SUBTRAÇÃO')
    op1 = float(input('Digite o primeiro número: '))
    op2 = float(input('Digite o segundo número: '))
    subtração(op1, op2)
elif a == 3:
    print('DIVISÃO')
    op1 = float(input('Digite o primeiro número: '))
    op2 = float(input('Digite o segundo número: '))
    divisão(op1, op2)
elif a == 4:
    print('MULTIPLICAÇÃO')
    op1 = float(input('Digite o primeiro número: '))
    op2 = float(input('Digite o segundo número: '))
    multiplicação(op1, op2)
else:
    print('Operação não encontrada')

