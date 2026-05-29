import pandas as pd


from utils.decoradores import marcar_tempo_de_execucao



marcar_tempo_de_execucao()
def processando_serie_historica_2016(arquivo_inicial, arquivo_final) -> None:
    df = pd.read_excel(arquivo_inicial)

    df_sem_coluna_nula = df.drop(columns=['Unnamed: 0'])
    df_colunas_nomeadas = df_sem_coluna_nula.rename(columns=df_sem_coluna_nula.iloc[4])
    df_sem_titulo_formatado = df_colunas_nomeadas.drop(df_colunas_nomeadas.index[0:5]).reset_index(drop=True)
    df_sem_valores_ausentes = df_sem_titulo_formatado.dropna(how='any')

    df_sem_valores_ausentes.to_csv(arquivo_final, index=False)
