''' Desenvolver um programa que peça ao usuário para digitar diversos números reais, e ao final, exibir o maior e o
menor número que foram digitados, além da média entre TODOS os números digitados pelo usuário. A inserção
de números deve parar quando o usuário digitar o número -1, e este número -1 não deve ser considerado nem
como maior, nem como menor, e nem na contagem da média'''


num = float(input("digite um numero (-1 encerra o programa): "))
maior =num

while(num != -1):
    if(maior < num):
        maior=num
    num = float(input("digite outro numero (-1 encerra o programa): "))

print("fim do programa")








