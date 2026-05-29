import config.caminhos as caminhos

from processamento.processamento_atlas import processando_arquivo_atlas
from processamento.processamento_serie_historica import processando_serie_historica_2016




def pipeline() -> None:
    processando_arquivo_atlas(
        caminhos.arquivo_bruto_atlas, 
        caminhos.arquivo_alterado_atlas
    )
    processando_serie_historica_2016(
        caminhos.arquivo_bruto_serie_historica_2016, 
        caminhos.arquivo_alterado_serie_historica_2016
    )



if __name__ == '__main__':
    pipeline()