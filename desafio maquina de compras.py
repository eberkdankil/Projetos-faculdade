c5 = 4
c2 = 3
c1 = 5
c75 = 20
c50 = 10
c25 = 10
c10 = 10
c05 = 10
c01 = 10

cc5 = 0
cc2 = 0
cc1 = 0
cc75 = 0
cc50 = 0
cc25 = 0
cc10 = 0
cc05 = 0
cc01 = 0

banco = (c5 * 5) + (c2 * 2) + (c1 * 1) + (c75 * 0.75) + (c50 * 0.50) + (c25 * 0.25) + (c10 * 0.10) + (c05 * 0.05) + (c01 * 0.01)
#print(banco)

valor = float(input('digite o preço do produto:'))
pagamento = float(input('digite o pagamento:'))

troco = pagamento - valor

if pagamento < valor :
    print('Saldo insuficiente')

if troco == 0 :
    print('transação concluida')

if troco > banco :
    print ('cara, troco insuficiente')
else :
    print('O troco foi de: ' + str(troco))

    while troco >= 5 and c5 > 0 :
        troco = troco - 5
        c5 = c5 - 1
        cc5 = cc5 + 1
    while troco >= 2 and c2 > 0 :
        troco = troco - 2
        c2 = c2 - 1
        cc2 = cc2 + 1
    while troco >= 1 and c1 > 0 :
        troco = troco - 1
        c1 = c1 - 1
        cc1 = cc1 + 1
    while troco >= 0.75  and c75 > 0:
        troco = troco - 0.75
        c75 = c75 - 1
        cc75 = cc75 + 1
    while troco >= 0.50 and c50 > 0 :
        troco = troco - 0.50
        c50 = c50 - 1
        cc50 = cc50 + 1
    while troco >= 0.25 and c25 > 0 :
        troco = troco - 0.25
        c25 = c25 - 1
        cc25 = cc25 + 1
    while troco >= 0.10 and c10 > 0 :
        troco = troco - 0.10
        c10 = c10 - 1
        cc10 = cc10 + 1
    while troco >= 0.05 and c05 > 0 :
        troco = troco - 0.05
        c05 = c05 - 1
        cc05 = cc05 + 1
    while troco >= 0.01 and c01 > 0 :
        troco = troco - 0.01
        c01 = c01 - 1
        cc01 = cc01 + 1
    
    if c5 >= 0 and cc5 > 0 :
        print("Imprimindo" + " " + str(cc5) + " " + "cedulas de 5$")
    if c2 >= 0 and cc2 > 0:
        print("Imprimindo" +  " " + str(cc2) + " " + "cedulas de 2$")
    if c1 >= 0 and cc1 > 0:
        print("Imprimindo" +  " " + str(cc1) + " " + "cedulas de 1$")
    if c75 >= 0 and cc75 > 0:
        print("Contando" +  " " + str(cc75) + " " + "moedas de 0.75$")
    if c50 >= 0 and cc50 > 0:
       print("Contando" +  " " + str(cc50) + " " + "moedas de 0.50$")
    if c25 >= 0 and cc25 > 0:
        print("Contando" +  " " + str(cc25) + " " + "moedas de 0.25$")
    if c10 >= 0 and cc10 > 0:
        print("Contando" +  " " + str(cc10) + " " + "moedas de 0.10$")
    if c05 >= 0 and cc05 > 0:
        print("Contando" +  " " + str(cc05) + " " + "moedas de 0.05$")
    if c01 >= 0 and cc01 > 0:
        print("Contando" +  " " + str(cc01) + " " + "moedas de 0.01$")
    

    
    #desafio: sem ter troco infinito (concluido)
