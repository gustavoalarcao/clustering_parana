import numpy as np
import streamlit as st
from streamlit import write, session_state as ss


from config.caminhos import arquivo_limpo_atlas

from coleta.coleta_atlas import coletando_dados_atlas


def pg_atlas() -> None:
    df = coletando_dados_atlas(arquivo_limpo_atlas)
    
    write(df)
    write(df.dtypes)