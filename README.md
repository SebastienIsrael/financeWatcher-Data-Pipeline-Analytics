# financeWatcher-Data-Pipeline-Analytics
A resilient Python data pipeline for real-time Bitcoin monitoring, featuring automated API extraction, CSV persistence, and dark-mode financial analytics.

O **financeWatcher** é um pipeline de dados modular desenvolvido em Python, projetado para monitorar cotações de criptomoedas (Bitcoin) de forma resiliente e automatizada. O projeto demonstra o fluxo completo de Engenharia de Dados: Extração (API), Armazenamento (Persistência) e Análise (Visualização).

## 🛠️ Arquitetura do Sistema
O projeto foi estruturado seguindo o princípio de responsabilidade única:

- **`extrator.py`**: Camada de ingestão de dados. Utiliza a API CoinGecko com tratamento de erros (try/except) e validação de status HTTP.
- **`storage.py`**: Camada de persistência. Garante a integridade dos dados salvos em CSV com timestamp no padrão ISO 8601.
- **`main.py`**: Orquestrador do pipeline. Gerencia o loop de execução e a resiliência do sistema.
- **`analytics.py`**: Camada de inteligência de negócio. Gera visualizações financeiras em "Dark Mode" estilo terminal.

## 🚀 Tecnologias
- **Linguagem:** Python 3.10+
- **Bibliotecas:** - `Pandas` para manipulação de séries temporais.
  - `Matplotlib` para visualização customizada.
  - `Requests` para consumo de API REST.

## 📊 Como Utilizar
1. Clone o repositório.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
