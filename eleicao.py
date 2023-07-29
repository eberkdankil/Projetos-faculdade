print("escolha seu candidato:")
print("1 - Eymael")
print("2 - padre Kelmon")
print("3 - Cabo Daciolo")
print("4 - Nulo")
print("5 - Branco")
print("0 - cancelar")

codigo = 0
eymael = 0
kelmon = 0
cabo = 0
nulo = 0
branco = 0
contador = 0
votos = 0



while contador == 0:

    codigo = int(input("Informe o numero do seu candidato: "))

    if codigo == 1:
        eymael += 1
        votos += 1

    elif codigo == 2:
        kelmon += 1
        votos += 1

    elif codigo == 3:
        cabo += 1
        votos += 1

    elif codigo == 4:
        nulo += 1
        votos += 1

    elif codigo == 5:
        branco += 1
        votos += 1

    elif codigo == 0:
        contador += 1

    else:
        print("digite um codigo valido")

Veymael = (eymael / votos)*100
Vkelmon = (kelmon / votos)*100
Vcabo = (cabo / votos)*100
Vnulo = (nulo / votos)*100
Vbranco = (branco / votos)*100

print(f"Eymael teve um total de {eymael} votos com uma porcentagem de {round(Veymael, 2)}% do total de votos ")
print(f"Kelmon teve um total de {kelmon} votos com uma porcentagem de {round(Vkelmon, 2)}% do total de votos")
print(f"Daciolo teve um total de {cabo} votos com uma porcentagem de {round(Vcabo, 2)}% do total de votos")
print(f"Teve um total de {nulo} votos nulos com uma porcentagem de {round(Vnulo, 2)}% do total de votos")
print(f"Teve um total de {branco} votos brancos com uma porcentagem de {round(Vbranco, 2)}% do total de votos")
print(f"O total de votos foi de: {votos} votos ")
