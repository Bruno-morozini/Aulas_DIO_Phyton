x = int(input("Digite um numero para descobrir se o numero é divisivel por 3 e 5 simultaneamente : "))

teste1 = x % 3
teste2 = x % 5

if teste1 == 0 and teste2 == 0:
    print("FizzBuzz")
else:
    print(x)
