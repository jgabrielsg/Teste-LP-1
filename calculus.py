import pandas as pd

# Dicionário de meses
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

def input_data():
    """
    Solicita ao usuário duas datas no formato "dia de mês de ano" separadas por " - ".
    """
    try:
        datas = input("Digite duas datas no formato 'dia de mês de ano' separadas por ' - ': ").split(" - ")
        return datas
    except Exception as e:
        print("Erro!", (e))
        return None

def transform_data(datas):
    """
    Converte as datas no formato "dia de mês de ano" para objetos datetime.

    Args:
        datas (list): Uma lista contendo as duas datas no formato "dia de mês de ano".

    Returns:
        tuple: Uma tupla contendo os objetos datetime correspondentes às datas.
    """
    data1 = datas[0]
    data2 = datas[1]

    data1 = data1.split(" de ")
    data2 = data2.split(" de ")

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

    return data_completa1, data_completa2

if __name__ == "__main__":
    datas = input_data()
    
    if datas:
        data1, data2 = transform_data(datas)
        diferenca_dias = abs((data2 - data1).days)
        print(f"A diferença em dias entre as datas é: {diferenca_dias}")
