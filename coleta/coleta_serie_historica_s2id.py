import pandas as pd


from config.caminhos import arquivo_alterado_serie_historica_2016




def coletando_dados_serie_historica_s2id():
    return pd.read_csv(arquivo_alterado_serie_historica_2016)