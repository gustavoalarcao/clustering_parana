import pandas as pd


from config.caminhos import arquivo_alterado_atlas




def coletando_dados_atlas() -> pd.DataFrame:
    return pd.read_csv(
        arquivo_alterado_atlas,
        parse_dates=['Data_Registro']
    )
