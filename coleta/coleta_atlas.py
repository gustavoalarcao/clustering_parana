import pandas as pd




def coletando_dados_atlas(arquivo) -> pd.DataFrame:
    return pd.read_csv(
        arquivo,
        parse_dates=['Data_Registro']
    )
