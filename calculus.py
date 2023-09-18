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
    Solicita ao usuário que escolha entre duas opções:
    (1) Digitar duas datas no formato 'dia de mês de ano' separadas por ' - '
    (2) Passar o nome de um arquivo .txt que contém as datas

    Returns
    -------
    datas : str
        As datas em string.

    """
    
    try:
        while True:
            print("Escolha uma opção:")
            print("(1) Digitar datas")
            print("(2) Passar um arquivo .txt")

            escolha = input("Digite o número da opção desejada: ")
            
            if escolha == "1":
                datas = input("Digite duas datas no formato 'dia de mês de ano' separadas por ' - ': ")
                return datas
            
            elif escolha == "2":
                arquivo = input("Digite o nome do arquivo .txt que contém as datas: ")
                if arquivo.endswith(".txt"):
                    datas = ler_arquivo(arquivo)
                    return datas
                else:
                    print("O arquivo deve ter extensão .txt.")
                    
            else:
                print("Opção inválida. Escolha uma opção válida (1 ou 2).")
    
    except Exception as e:
        print("Erro!", (e))
        return None

def transform_data(datas):
    """
    Converte as datas no formato exigido para objetos em datetime.

    Parameters
    ----------
    datas : str
       Datas ou arquivo com datas a ser entregue para calcular a diferença.

    Returns
    -------
    data_completa1 : datetime
        Primeira data entregue convertida para datetime.
    data_completa2 : datetime
        Segunda data entregue convertida para datetime.
    """
    
    datas = datas.split(" - ")
    
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

def ler_arquivo(nome_arquivo):
    """
    Lê arquivo .txt para calcular a diferença entre as datas contidas nele.

    Parameters
    ----------
    nome_arquivo : str
       Nome do arquivo a ser chamado.

    Returns
    -------
    conteudo : str
        O conteúdo do arquivo passado.
    """
    
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            return conteudo
        
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
        
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

def dias_entre_datas():
    """
    Calcula a diferença de dias entre as datas dadas.

    Returns
    -------
    diferenca_dias : int
        Número de dias entre uma data e outra.
    """
    
    datas = input_data()

    if datas:
        data1, data2 = transform_data(datas)
        diferenca_dias = abs((data2 - data1).days)
    
    return diferenca_dias