import pandas as pd
import numpy as np




def coletando_ocorrencias_de_desastres(caminho_do_arquivo) -> pd.DataFrame:
    return pd.read_csv(
        caminho_do_arquivo, 
        sep=';', 
        thousands='.', 
        decimal=','
    )





