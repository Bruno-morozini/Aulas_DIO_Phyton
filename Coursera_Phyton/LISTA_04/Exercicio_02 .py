x = int(input("Digite um numero para descobrir se o numero é divisivel por 3 : "))

teste = x % 3

if teste == 0:
    print("fizz")
else:
    print(x)
