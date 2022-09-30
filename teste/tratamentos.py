import os
import pandas as pd

# criar lista cons os arquivos da pasta arquivos_csv
lista_arquivos = os.listdir('arquivos_csv')


# criar funcao para verificar a quantidade de linhas e colunas de cada arquivo
def verificar_linhas_colunas(item):
    try:
        df = pd.read_csv('arquivos_csv/' + item, sep=';', encoding='latin-1')
        print('O arquivo {} possui {} linhas e {} colunas'.format(item, df.shape[0], df.shape[1]))
    except UnicodeDecodeError as U:
        print('O arquivo {} possui erro de codificação'.format(item))
        print('Erro: {}'.format(U))


#ler e concatenar os arquivos usando o pd.concat
def concatenar_arquivos(lista):
    lista_df = []
    for item in lista:
        try:
            df = pd.read_csv('arquivos_csv/' + item, sep=';', encoding='latin-1')
            lista_df.append(df)
        except UnicodeDecodeError as U:
            print('O arquivo {} possui erro de codificação'.format(item))
            print('Erro: {}'.format(U))
    df_concatenado = pd.concat(lista_df, axis=0)
    #ignorar o index
    df_concatenado.to_csv('arquivos_csv/concatenado.csv', index=False, sep=';')
    return df_concatenado




