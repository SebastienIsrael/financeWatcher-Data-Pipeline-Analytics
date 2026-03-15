import requests
#link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
link = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=brl,usd"
headers = {"User-Agent":"brave 1.87.192" }

def pegar_cotação():
    try:
        requisição = requests.get(link, headers=headers)
        if requisição.status_code == 200:
            resposta = requisição.json()
            cotação = resposta["bitcoin"]["brl"]
            return cotação
    except:
        captura_erro = requisição.status_code
        print("Erro de conexão física.Verifique sua internet.")
        return None


    

    


