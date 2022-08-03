## Fazer uma calculadora de 4 operações (soma, multiplicação, divisão inteira, potência). Peça a operação desejada e depois os
# dois números ao usuário.

print('1 - Soma\n2 - Multiplicação\n3 - Divisão\n4 - Potência\n')
op = int(input('Escolha uma operação: '))
num1 = float(input('Primeiro número: ')) # Usando o 'Casting' é a conversão dos dados do usuário (Strings) para (float.)
num2 = float(input('Segundo número:' )) # Usando o 'Casting' é a conversão dos dados do usuário (Strings) para (float.)

if op == 1:
    soma = num1 + num2
    print('Soma: {0}'.format(soma))
else:
    if op == 2:
        multiplicacao = num1 * num2
        print('Multiplicacao: {0}'.format(multiplicacao))
    else:
        if op == 3:
            divisao = num1 // num2 # Divisão inteira
            print('Divisão: {0}'.format(divisao))
        else:
            if op == 4:
                potencia = num1 ** num2
                print('Pontência: {0}'.format(potencia))
            else:
                print('Digite um opção válida')