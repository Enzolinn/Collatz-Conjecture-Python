n = int(input('Digite um número inteiro natural: '))

listaNumeros = []
listaNumeros.append(n)
flag = True


listaNumerosN = []
listaNumerosN.append(n)
contador = 0
while flag == True:



    def isEven():

        print(n,'É par, portanto,', n,'/ 2 = ', n/2)


    def isOdd():

        print(n, 'É impar, portanto,', n, 'x 3 + 1 = ', (n*3)+1)





    if (n%2) == 0:

        resultado = n / 2 
        listaNumeros.append(resultado)
        print(listaNumeros)
        n = resultado


    else: 

        resultado = (n*3) + 1
        listaNumeros.append(resultado)
        print(listaNumeros)
        n = resultado

    if n == 1:
        n = listaNumerosN[contador]
        n += 1
        contador += 1
        listaNumerosN.append(n)
        