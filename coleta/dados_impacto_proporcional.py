import pandas as pd
import numpy as np




def coletando_ocorrencias_de_desastres(filepath) -> pd.DataFrame:
    df = pd.read_csv(
        filepath, 
        sep=';', 
        thousands='.', 
        decimal=','
    )
    return df





