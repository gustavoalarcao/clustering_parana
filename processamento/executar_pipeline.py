from config.caminhos import arquivo_bruto_atlas, arquivo_alterado_atlas

from .processamento_atlas import processando_arquivo_atlas



def pipeline() -> None:
    processando_arquivo_atlas(arquivo_bruto_atlas, arquivo_alterado_atlas)



if __name__ == '__main__':
    pipeline()