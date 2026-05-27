# Sobre o Git

Para clonar o repositório é necessário ter o Git instalado no computador. No site da plataforma
eles tem tutoriais sobre como fazer isso em cada sistema operacional.

Caso seja a primeira vez usando Git no computador, será necessário definir um nome de usuário:
```bash
git config --global user.name "Seu Nome"
```
e um e-mail:
```bash
git config --global user.email "seu.email@exemplo.com"
```

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

Crie a pasta de dados:
```bash
# Ubuntu / Debian / MacOS
python3 -m config.criar_pasta_de_dados

# Windows
python -m config.criar_pasta_de_dados
```
e adicione os arquivos do drive em "dados/brutos".

Para executar as transformações nos arquivos execute:
```bash
# Ubuntu / Debian / MacOS
python3 -m processamento.executar_pipeline

# Windows
python3 -m processamento.executar_pipeline
```


# Acompanhamento do projeto

Mude para a pasta do projeto:
```bash
cd clustering_parana
```

Nunca esqueça de ativar o ambiente virtual, caso contrário na hora de instalar as 
dependências após uma atualização, o download será feito no seu computador. Ative o ambiente virtual:
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

Conforme o projeto avança, você precisará baixar as atualizações mais recentes. 
Para fazer isso, abra o terminal e execute:
```bash
cd clustering_parana
git pull
```

Pode ser que depois de uma atualização novas dependências tenham sido adicionadas, logo
será necessário instalar as novas dependências. É possível monitorar isso pela data de edição do 
arquivo `requirements.txt`. Caso tenha sido editado depois da última atualização, execute:
```bash
# Ubuntu / Debian / MacOS
pip3 install -r requirements.txt

# Windows
pip install -r requirements.txt
```

Além do mais, pode ser necessário adicionar mais arquivos do drive em "dados/brutos".
E, na sequência processar estes arquivos com:
```bash
# Ubuntu / Debian / MacOS
python3 -m processamento.executar_pipeline

# Windows
python3 -m processamento.executar_pipeline
```

