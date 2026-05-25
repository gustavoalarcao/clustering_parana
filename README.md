# Configuração Inicial

Este projeto usa a versão Python 3.12.3 .

Clone o repositório:
```bash
git clone https://github.com/gustavoalarcao/clustering_parana
```

Faça a pasta com o repositório ser o diretório ativo:
```bash
cd clustering_parana
```

Na pasta com o repositório, crie e ative um ambiente virtual:
```bash
# Ubuntu / Debian / MacOS
python3 -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate
```

Instale as dependências do projeto:
```bash
# Ubuntu / Debian / MacOS
pip3 install -r requirements.txt

# Windows
pip install -r requirements.txt
```


# Acompanhamento do projeto

Mude para a pasta do projeto:
```bash
cd clustering_parana
```

Ative o ambiente virtual:
```bash
# Ubuntu / Debian / MacOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

Para visualizar as análises ativas, execute:
```bash
streamlit run main.py
```


