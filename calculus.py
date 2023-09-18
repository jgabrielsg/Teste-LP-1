import pandas as pd

datas = input().split(" - ")

data1 = datas[0]
data2 = datas[1]

data1 = data1.split(" de ")
data2 = data2.split(" de ")

meses = {
    "Janeiro": 1,
    "Fevereiro": 2,
    "Março": 3,
    "Abril": 4,
    "Maio": 5,
    "Junho": 6,
    "Julho": 7,
    "Agosto": 8,
    "Setembro": 9,
    "Outubro": 10,
    "Novembro": 11,
    "Dezembro": 12
}

dia1 = data1[0]
mes1 = data1[1]
numero_mes1 = meses.get(mes1)
ano1 = data1[2]

dia2 = data2[0]
mes2 = data2[1]
numero_mes2 = meses.get(mes2)
ano2 = data2[2]


data_completa1 = str(dia1) + "-" + str(numero_mes1) + "-" + str(ano1)
data_completa2 = str(dia2) + "-" + str(numero_mes2) + "-" + str(ano2)

data_completa1 = pd.to_datetime(data_completa1, format='%d-%m-%Y')
data_completa2 = pd.to_datetime(data_completa2, format="%d-%m-%Y")

diferenca_dias = (data_completa2 - data_completa1).days




print(abs(diferenca_dias))