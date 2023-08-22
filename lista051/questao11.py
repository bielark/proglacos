''' Elaborar um programa que apresente o valor de uma potência de uma base qualquer (Variável b) elevada a um
expoente qualquer (Variável e), ou seja, de be
. (Sem usar Math.pow();)'''

b = float(input("informe um numero: "))
e = float(input("informe o expoente da potencia"))

cont = 1
acu = 1
while(cont <=e):
    acu = acu * b
    cont = cont+1
print(f"{b:.0f} elevado a {e:.0f} = {acu}")

