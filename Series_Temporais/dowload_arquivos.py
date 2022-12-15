import requests
import os
from time import sleep


# crando lista com os nomes dos arquivos
lista_fim_links = ['ca-2004-01.csv', 'ca-2004-02.csv', 'ca-2005-01.csv', 'ca-2005-02.csv', 'ca-2006-01.csv',
                   'ca-2006-02.csv', 'ca-2007-01.csv', 'ca-2007-02.csv', 'ca-2008-01.csv', 'ca-2008-02.csv',
                   'ca-2009-01.csv', 'ca-2009-02.csv', 'ca-2010-01.csv', 'ca-2010-02.csv', 'ca-2011-01.csv',
                   'ca-2011-02.csv', 'ca-2012-01.csv', 'ca-2012-02.csv', 'ca-2013-01.csv', 'ca-2013-02.csv',
                   'ca-2014-01.csv', 'ca-2014-02.csv', 'ca-2015-01.csv', 'ca-2015-02.csv', 'ca-2016-01.csv',
                   'ca-2016-02.csv', 'ca-2017-01.csv', 'ca-2017-02.csv', 'ca-2018-01.csv', 'ca-2018-02.csv',
                   'ca-2019-01.csv', 'ca-2019-02.csv', 'ca-2020-01.csv', 'ca-2020-02.csv', 'ca-2021-01.csv',
                   'ca-2021-02.csv']

#Criando função para baixar os arquivos
def baixar_csv(item):
    link = f'https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/dsas/ca/{item}'
    # baixando o arquivo csv se ele nao existir na pasta
    #salvar os arquivos em arquivos_csv
    #mostrando o tamanho do arquivo e o tempo de download
    if not os.path.exists(f'arquivoscsv/{item}'):
        print(f'baixando o arquivo {item}')
        r = requests.get(link)
        #mostar o tamanho do arquivo em MB
        print(f'Tamanho do arquivo: {len(r.content)/1024/1024:.2f} MB')
        #mostrar o tempo de download
        print(f'tempo de download: {r.elapsed.total_seconds()} segundos')
        sleep(5)
        print('Arquivo salvo com sucesso!')
        with open(f'arquivoscsv/{item}', 'wb') as f:
            f.write(r.content)
    else:
        print(f'arquivo {item} ja existe')
        
        
#criar função para verificar se as colunas de cada arquivo são iguais
def verificar_colunas():
    import pandas as pd
    #verificar colunas de uma dos arquivos csv da pasta arquivos_csv
    df = pd.read_csv('arquivos_csv/ca-2004-01.csv', sep=';', encoding='latin-1')
    #criar lista com as colunas do arquivo
    coluna =[col for col in df.columns]
    #ler o reestante dos arquivos usando a biblioteca glob e verificar se as colunas são iguais
    for arquivo in gb.glob('arquivoscsv/*.csv'):
        df = pd.read_csv(arquivo, sep=';', encoding='latin-1')
        coluna2 = [col for col in df.columns]
        if coluna == coluna2:
            print(f'Colunas do arquivo {arquivo} são iguais')
        else:
            print(f'Colunas do arquivo {arquivo} são diferentes')


