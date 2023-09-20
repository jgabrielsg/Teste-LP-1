from calculus import dias_entre_datas

if __name__ == "__main__":
    while True:
        try:
            diff_datas = dias_entre_datas()
            print(f"A diferença em dias entre as datas é {diff_datas}!\n")
        except Exception as e:
            print("Não foi possível calcular a diferença\n")
    
