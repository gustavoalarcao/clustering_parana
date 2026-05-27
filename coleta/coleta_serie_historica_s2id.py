import pandas as pd




def extraindo_dados_serie_historica_s2id(caminho):
    return pd.read_excel(
        io=caminho,
    )