print("Digite uma sequencia de valores terminada por zero ")

tamanho  = int(input("Digite o tamanho da sequencia de numeros "))

soma = 0 #para iniciar a soma


i = 0  #para não dar ero ao entrar no while

while i<tamanho: ##condição
        valor = int(input ("Digite um valor a ser somado: ")) #msg dentro do while
        i = i+1
        soma = soma + valor

        
print("A soma dos Valores digitados e : " , soma)

