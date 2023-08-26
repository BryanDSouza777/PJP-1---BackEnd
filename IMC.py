nome = str(input("Digite seu nome\n:"))
idade = int(input("\nDigite sua idade\n:"))
altura = float(input("\nDigite sua altura\n:"))
peso = float(input("\nDigite seu peso\n:"))

anoatual = 2023
aniversario = str(input("\nVocê ja fez aniversario este ano?\n\ns = sim\nn = não\n:"))

if aniversario == 's' or aniversario == 'S':
    print(f'\nVocê nasceu em {anoatual - idade}')

elif aniversario == 'n' or aniversario == 'N':
    print(f'\nVocê nasceu em {anoatual - idade - 1}')

imc = peso/((altura)**2)

if imc < 18.5:
    print(f'\nSeu IMC é de {imc:.2f}, você está em subpeso.')

elif imc >= 18.5 and imc <= 24.99:
    print (f'\nSeu IMC é de {imc:.2f}, você está com o peso normal.')

elif imc >= 25 and imc <= 29.99:
    print (f'\nSeu IMC é de {imc:.2f}, você está em sobrepeso.')

else:
    print (f'\nSeu IMC é de {imc:.2f}, você está com obesidade.')