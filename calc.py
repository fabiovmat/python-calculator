''' 
NOme : Matt
Data: 21/11/2022
Projeto: Calculadora simples python


'''

# Funcao adiciona dois numeros
def adiciona(num1, num2):
	return num1 + num2

# Funcao subtrai dos numeros
def subtrtrai(num1, num2):
	return num1 - num2

# Funcao para multiplicar
def multiplica(num1, num2):
	return num1 * num2

# Funcao para dividir
def divide(num1, num2):
	return num1 / num2

print("Por favor, selecione uma operação  -\n" \
		"1. Adiciona\n" \
		"2. Subtrai\n" \
		"3. Multiplica\n" \
		"4. Divide\n")


# Take input from the user
select = int(input("Digite  1, 2, 3, 4 :"))

numero1 = int(input("Entre com o primeiro número: "))
numero2 = int(input("Entre com o segundo número: "))

if select == 1:
	print(numero1, "+", numero2, "=",
					adiciona(numero1, numero2))

elif select == 2:
	print(numero1, "-", numero2, "=",
					subtrtrai(numero1, numero2))

elif select == 3:
	print(numero1, "*", numero2, "=",
					multiplica(numero1, numero2))

elif select == 4:
	print(numero1, "/", numero2, "=",
					divide(numero1, numero2))
else:
	print("Entrada inválida")
