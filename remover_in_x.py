import os
import re

# Função para remover o texto "In [x]:" de um arquivo HTML
def remover_in_x(arquivo_html):
    with open(arquivo_html, 'r', encoding='utf-8') as file:
        conteudo = file.read()

    # Regex ajustada para remover "In [x]:" incluindo possíveis quebras de linha e espaços
    conteudo_modificado = re.sub(r'\s*In\s*\[\d+\]:\s*', '', conteudo, flags=re.MULTILINE)

    # Sobrescrever o arquivo com o conteúdo modificado
    with open(arquivo_html, 'w', encoding='utf-8') as file:
        file.write(conteudo_modificado)

# Caminho do diretório onde estão os arquivos HTML
caminho_diretorio = './'  # Você pode alterar para o diretório específico

# Percorrer todos os arquivos no diretório
for nome_arquivo in os.listdir(caminho_diretorio):
    if nome_arquivo.endswith('.html'):  # Processar apenas arquivos .html
        caminho_completo = os.path.join(caminho_diretorio, nome_arquivo)
        remover_in_x(caminho_completo)
        print(f'Processado: {caminho_completo}')

print('Remoção de "In [x]:" concluída.')
