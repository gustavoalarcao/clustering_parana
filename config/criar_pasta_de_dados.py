from pathlib import Path




if __name__ == '__main__':
    diretorio_raiz = Path(__file__).parent.parent
    
    caminho_brutos = diretorio_raiz / 'dados' / 'brutos'
    caminho_alterados = diretorio_raiz / 'dados' / 'brutos'
    
    caminho_brutos.mkdir(parents=True, exist_ok=True)
    caminho_alterados.mkdir(parents=True, exist_ok=True)
    
    print('Pasta "dados/brutos" criada.')
    print('Adicione os arquivos do drive')
    
    
