'''8) Desenvolver um programa que apresente todos os valores numéricos inteiros ímpares situados na faixa de 0 a
20. Para saber se o número é ímpar, será necessário verificar essa condição com o comando if. Sendo ímpar,
mostre-o; não sendo, passe para o próximo passo.'''

n = 0
while(n <= 20):
    div2 = n % 2
    if(div2 == 1):
        print(f"{n} seu numero e impar")
    n = n + 1
