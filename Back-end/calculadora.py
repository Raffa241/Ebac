print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

def calculadora():
    print("Escolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

opcao = input("Digite o número da operação desejada: ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao == "1":
    print("Resultado:", num1 + num2)
elif opcao == "2":
    print ("Resultado:" , num1 - num2)
elif opcao == "3":
    print ("Resultado:" , num1 * num2)
elif opcao == "4":
    if num2 == 0:
        print("Erro: não é possível dividir por zero")
    else:
        print("Resultado:", num1 / num2)
else :
    print("Essa opção matematica é inválida, tente novamente")

print("Fazer mais operações? (s/n)")
resposta = input("Digite 's' para sim ou 'n' para não: ")
if resposta.lower() == 's':
    print("Reiniciando a calculadora...")
    calculadora()
else:    print("Obrigado por usar a calculadora!")
