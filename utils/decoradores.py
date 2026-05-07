import time


def marcar_tempo_de_execucao():
    def envelope_funcao(funcao):
        def envelope_argumentos(*args, **kwargs):
            inicio = time.perf_counter()
            funcao(*args, **kwargs)
            fim = time.perf_counter()
            tempo_de_execucao = fim - inicio
            print(f'Tempo de execução: {tempo_de_execucao:.6g} segundos')
        return envelope_argumentos
    return envelope_funcao