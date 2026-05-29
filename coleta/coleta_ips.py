import pandas as pd


from config.caminhos import arquivo_bruto_ips_2026




def coletando_dados_ips() -> pd.DataFrame:
    return pd.read_csv(arquivo_bruto_ips_2026)