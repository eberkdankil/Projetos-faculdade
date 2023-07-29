hora = int(input("quantas horas por dia você trabalha: "))
qhora = int(input("Quantas horas nesse mês você trabalhou: "))

inss = 0.10
fgts = 0.11
descontoir = 0
desconto_inss = 0
desconto_fgts = 0
desconto_total = 0
ir = 0
salario_bruto = hora * qhora
salario_liquido = 0

if salario_bruto > 900 and salario_bruto <= 1500:
    descontoir = 0.05

if salario_bruto > 1500 and salario_bruto <= 2500:
    descontoir = 0.10

if salario_bruto > 2500:
    descontoir = 0.20

desconto_inss = salario_bruto * inss
desconto_fgts = salario_bruto * fgts
ir = salario_bruto * descontoir

imposto = descontoir * 100

desconto_total = desconto_inss + ir
salario_liquido = salario_bruto - desconto_total

print("Salario Bruto:            R$:",salario_bruto)
print(f"IF ({int(imposto)}%)                   R$:", ir)
print("INSS (10%)                R$:", desconto_inss)
print("FGTS (11%)                R$:", desconto_fgts)
print("Desconto total            R$:",desconto_total)
print("Salario Liquido:          R$",salario_liquido)

    