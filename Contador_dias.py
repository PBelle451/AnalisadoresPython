import datetime
ano1 = int(input("Favor inserir ano: "))       #formato AAAA
mes1 = int(input("Favro inserir mês: "))         #usar numeros
dia1 = int(input("Favor inserir dia: "))

ano2 = int(input("Favor inserir ano: "))
mes2 = int(input("Favor inserir mês: "))
dia2 = int(input("Favor inserir dia: "))

datapadrao = datetime.date(ano1, mes1, dia1)
datalimite = datetime.date(ano2, mes2, dia2)
hoje = datetime.date.today()

if datapadrao > datalimite:
    delta = datapadrao - datalimite
elif datapadrao <= datalimite:
    delta = datalimite - datapadrao
print(delta.days)