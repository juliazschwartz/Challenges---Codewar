
# para CÉDULAS APENAS:
valor = int(input('valor: '))

valor;

notas = [200,100,50,20,10,2,1];

while True:
    for i in notas:
        if valor >= i:
            print('{} nota de {}'.format(valor//i, i))
            valor = valor%i
            
        if valor == 0:
            break




#para MOEDAS  E CÉDULAS:

valor = float(input('valor: '))
valor
notas = [200,100,50,20,10,2,1]
moedas = [0.50, 0.25, 0.10, 0.05, 0.01]

while True:
    for i in notas:
        if valor >= i:
            print('{} nota de {}'.format(int(valor//i), i))
            valor = valor%i
        if valor == 0:     
            break

    for B in moedas:
            if (valor / B) >= 2 :
            
                    print('{} MOEDA de {}'.format(round(valor//B), B))
                    valor = valor%B
           
    
            if valor == 0:     
                    break