# Automação de Testes com Alumnium

Este projeto utiliza a biblioteca [Alumnium](https://alumnium.ai/) para automação de testes de interface do usuário (UI) com inteligência artificial.

## O que é Alumnium?

Alumnium é uma biblioteca experimental que permite escrever testes automatizados em linguagem natural, simplificando a criação e manutenção de testes de UI.

## Pré-requisitos

- Python 3.13+
- Selenium
- Chave de API do Google Gemini (ou outra suportada pla Alumnium)
- Biblioteca Alumnium instalada

## Instalação

1. Clone este repositório:

   ```bash
   git clone [https://github.com/jeffbarreto1/selenium_ai]
   cd [selenium_ai]
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # No Linux/Mac
   .venv\Scripts\activate  # No Windows
   ```

3. Instale as dependências com Poetry:

   ```bash
   poetry install
   ```

## Configuração

1. Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

   ```
   ALUMNIUM_MODEL=google
   GOOGLE_API_KEY=SUA_CHAVE_GEMINI   
   ```

   Substitua `SUA_CHAVE_GEMINI` pela sua chave de API do Google Gemini.

2. (Opcional) Se quiser usar outra IA, defina a variável de acordo com a documentação da Alumnium.

## Executando os testes

Execute os testes usando `unittest`:

```bash
poetry run python -m unittest test.py
```

## Estrutura do projeto

```
.
├── .venv/                # Ambiente virtual
├── .env                  # Variáveis de ambiente
├── test.py               # Arquivo de teste
├── pyproject.toml        # Configuração do Poetry
├── README.md             # Este arquivo
└── ...
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

[MIT](LICENSE)
