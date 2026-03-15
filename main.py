import extrator
import time
import storage
while True:
    valor = extrator.pegar_cotação()
    if valor is not None:
        print(valor, flush=True)
        storage.salvar_dados(valor)
    else:
        print("Pulando captura devido a erro na API. tentando novamente em 30 segundos. ")
    time.sleep(300)
    
