x = int(input("Digite um numero para descobrir se o numero é divisivel por 5 : "))

teste = x % 5

if teste == 0:
    print("Buzz")
else:
    print(x)
