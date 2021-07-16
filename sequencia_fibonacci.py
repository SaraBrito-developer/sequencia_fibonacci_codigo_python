sequencia = int(input("Quantos numeros Fibonacci você deseja?  ""\n"))
sequencia = int(input("voce precisa digitar um numero maior que 0\n \nQuantos numeros Fibonacci você deseja? "))
contagem = 0
num1, num2 = 0, 1

while sequencia <= 0:
    sequencia = int(input("voce precisa digitar um numero maior que 0\n \nQuantos numeros Fibonacci você deseja? "))
    
if sequencia == 1:
    print("sequencia numerica fibonacci",sequencia,":")
    print(num1)

else:
    print("\nA sequencia Fibonacci requisitada foi:")

    while contagem < sequencia:
        print(num1)
        soma = num1 + num2
        num1 = num2
        num2 = soma
        contagem += 1