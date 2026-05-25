import pandas as pd
import numpy as np




def coletando_ocorrencias_de_desastres(caminho) -> pd.DataFrame:
    return pd.read_csv(
        caminho, 
        sep=';', 
        thousands='.', 
        decimal=','
    )





