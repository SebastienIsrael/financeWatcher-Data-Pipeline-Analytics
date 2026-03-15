import pandas as pd
from datetime import datetime
arquivo_csv = "historico.csv"

def salvar_dados(valor):
    cotacao = valor
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")

    # Criar DataFrame com um único registro
    df = pd.DataFrame([{
        'DataHora': timestamp,
        'Cotacao': cotacao
    }])

    # Salvar no CSV (modo 'a' para anexar, incluir cabeçalho apenas na primeira vez)
    df.to_csv(arquivo_csv, mode='a', header=not pd.io.common.file_exists(arquivo_csv), index=False)
    
    print(f"{timestamp}: Cotacao {cotacao} salva.")
    
    
    
