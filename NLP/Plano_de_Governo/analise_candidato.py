import pdfplumber
from PIL import Image
import re
from collections import Counter
import networkx as nx
import numpy as np
import nltk
from wordcloud import WordCloud, STOPWORDS
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('portuguese')
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os


def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('0 - Sair')
    print('1 - CIRO FERREIRA GOMES')
    print('2 - JOSE MARIA EYMAEL')
    print('3 - LUIZ FELIPE CHAVES D''AVILA')
    print('4 - JAIR MESSIAS BOLSONARO')
    print('5 - LEONARDO PÉRICLES VIEIRA ROQUE')
    print('6 - LUIZ INÁCIO LULA DA SILVA')
    print('7 - PABLO HENRIQUE COSTA MARÇAL')
    print('8 - ROBERTO JEFFERSON MONTEIRO FRANCISCO')
    print('9 - SIMONE NASSAR TEBET')
    print('10 - SOFIA PADUA MANZANO')
    print('11 - SORAYA VIEIRA THRONICKE')
    print('12 - VERA LUCIA PEREIRA DA SILVA SALGADO')
    try:
        opt = int(input('Escolha o Candidato: '))
        if opt == 0:
            pass
        elif opt == 1:
            ArquivoPdf = 'planos_de_governo/ciro.pdf'
            imagem = 'imagens/ciro.png'
            candidato = 'Ciro Gomes'
            menu_secudario(ArquivoPdf, candidato, imagem)
        elif opt == 2:
            ArquivoPdf = 'planos_de_governo/eymael.pdf'
            imagem = 'imagens/eymael.png'
            candidato = 'Jose Maria Eymael'
            menu_secudario(ArquivoPdf, candidato, imagem)
        elif opt == 3:
            ArquivoPdf = 'planos_de_governo/davila.pdf'
            imagem = 'imagens/davila.png'
            candidato = 'Felipe Davila'
            menu_secudario(ArquivoPdf, candidato, imagem)
        elif opt == 4:
            ArquivoPdf = 'planos_de_governo/bolsonaro.pdf'
            imagem = 'imagens/bolsonaro.png'
            candidato = 'Jair Bolsonaro'
            menu_secudario(ArquivoPdf, candidato, imagem)
        elif opt == 5:
            ArquivoPdf = 'planos_de_governo/roque.pdf'
            imagem = 'imagens/roque.png'
            candidato = 'Leonardo Roque'
            menu_secudario(ArquivoPdf, candidato, imagem)
        elif opt == 6:
            ArquivoPdf = 'planos_de_governo/lula.pdf'
            imagem = 'imagens/lula.png'
            candidato = 'Lula'
            menu_secudario(ArquivoPdf, candidato, imagem)
        elif opt == 7:
            ArquivoPdf = 'planos_de_governo/marcal.pdf'
            imagem = 'imagens/marcal.png'
            candidato = 'Pablo Marcal'
            menu_secudario(ArquivoPdf, candidato, imagem)
        elif opt == 8:
            ArquivoPdf = 'planos_de_governo/jefferson.pdf'
            imagem = 'imagens/jefferson.png'
            candidato = 'Jefferson'
            menu_secudario(ArquivoPdf, candidato, imagem)
        elif opt == 9:
            ArquivoPdf = 'planos_de_governo/simone.pdf'
            imagem = 'imagens/simone.png'
            candidato = 'Simone'
            menu_secudario(ArquivoPdf, candidato, imagem)
        elif opt == 10:
            ArquivoPdf = 'planos_de_governo/sofia.pdf'
            imagem = 'imagens/sofia.png'
            candidato = 'Sofia'
            menu_secudario(ArquivoPdf, candidato, imagem)
        elif opt == 11:
            ArquivoPdf = 'planos_de_governo/soraya.pdf'
            imagem = 'imagens/soraya.png'
            candidato = 'Soraya'
            menu_secudario(ArquivoPdf, candidato, imagem)
        elif opt == 12:
            ArquivoPdf = 'planos_de_governo/vera.pdf'
            imagem = 'imagens/vera.png'
            candidato = 'Vera'
            menu_secudario(ArquivoPdf, candidato, imagem)
        else:
            print('Opção Invalida')
            menu()
    except ValueError:
        print('Opção invalida')
        menu()
    except Exception as e:
        print(e)
        menu()
         
def menu_secudario(ArquivoPdf, candidato, imagem):
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'Analisa Plano de Governo do Candidato {candidato}')
            print('1 - Analise do PDF')
            print('2 - Tabela de palavras mais usadas')
            print('3 - WordCloud')
            print('4 - Grafico de barras')
            print('5 - Plotar Grafo')
            print('6 - Menu Principal')
            print('7 - Salva em CSV')
            print('8 - WordCloud Geral CSV')
            print('9 - WordCloud Geral PDF')
            print('10 - Grafico de barras Geral CSV')
            print('11 - Grafico somatorio de palavras')
            print('12 - Sair')
    
            opcao = int(input('Escolha uma opção: '))
            if opcao == 1:
                analise(ArquivoPdf, candidato)
                os.system('pause')
            elif opcao == 2:
                print(vendotabela(ArquivoPdf))
                os.system('pause')
            elif opcao == 3:
                plota_wordcloud(ArquivoPdf, imagem)
                os.system('pause')
            elif opcao == 4:
                plotar_grafico(ArquivoPdf)
                os.system('pause')
            elif opcao == 5:
                plotar_grafo(ArquivoPdf)
                os.system('pause')    
            elif opcao == 6:
                menu()
            elif opcao == 7:
                salva_tabela(ArquivoPdf)
                os.system('pause')
            elif opcao == 8:
                wordcloud_geral_csv()
                os.system('pause')
            elif opcao == 9:
                wordcloud_geral_pdf()
                os.system('pause')
            elif opcao == 10:
                grafico_barras_geral()
                os.system('pause')
            elif opcao == 11:
                grafico_somatorio()
                os.system('pause')
            elif opcao == 12:
                return False
        except ValueError:
            print('Opção inválida')
            os.system('pause' if os.name == 'nt' else 'read -p "Pressione Enter para continuar..."')
        except Exception as e:
            print('Erro: {}'.format(e))
            os.system('pause' if os.name == 'nt' else 'read -p "Pressione Enter para continuar..."')

def analise(ArquivoPdf, candidato):
    pdf = pdfplumber.open(ArquivoPdf)
    contapage = len(pdf.pages)
    print(f'O arquivo PDF do Candidato {candidato} tem {contapage} páginas')
    print()
    print('Aqui vai pequeno Trecho da proposta de Governo do candidato:')
    print()
    print(pdf.pages[5].extract_text())

def tratamento_texto(ArquivoPdf):
    texto_limpo = []
    pdf = pdfplumber.open(ArquivoPdf)
    contapage = len(pdf.pages)
    texto = ''
    for i in range(contapage):
        texto += pdf.pages[i].extract_text()
    texto = texto.lower()
    texto = re.sub(r'[^a-zA-Z\s]', '', texto, re.I | re.A)
    texto = re.findall(r'\w+', texto)
    for palavra in texto:
        if (palavra not in stopwords) & (len(palavra) > 3):
            texto_limpo.append(palavra)
    testo_limpo = texto_limpo.sort()
    texto_limpo = ' '.join(texto_limpo)
    texto_limpo = texto_limpo.strip()
    return texto_limpo
    
def vendotabela(ArquivoPdf):
    texto = tratamento_texto(ArquivoPdf)
    palavras = texto.split()
    contagem = Counter(palavras)
    df = pd.DataFrame(contagem.most_common(20), columns=['Palavras', 'Contagem'])
    return df

def plota_wordcloud(ArquivoPdf, imagem):
    mask = np.array(Image.open(imagem))
    # criar wordcloud sem palavras duplicadas
    texto = tratamento_texto(ArquivoPdf)
    wordcloud = WordCloud(width=800, height=500,mask=mask,max_font_size=110, collocations=False).generate(texto)
    plt.figure(figsize=(10, 7))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis('off')
    plt.show()

def plotar_grafico(ArquivoPdf):
    df = vendotabela(ArquivoPdf)
    df.plot.bar(x='Palavras', y='Contagem', figsize=(10, 7))
    plt.show()

def plotar_grafo(ArquivoPdf):
    texto = tratamento_texto(ArquivoPdf)
    palavras = texto.split()
    contagem = Counter(palavras)
    df = pd.DataFrame(contagem.most_common(20), columns=['Palavras', 'Contagem'])
    G = nx.from_pandas_edgelist(df, source='Palavras', target='Contagem')
    G.add_nodes_from(nodes_for_adding=df['Palavras'].tolist())
    G = nx.Graph()
    for palavra in df['Palavras']:
        G.add_node(palavra)
    for palavra in df['Palavras']:
        for palavra2 in df['Palavras']:
            if palavra != palavra2:
                G.add_edge(palavra, palavra2)
    nx.draw(G, with_labels=True, node_size=1000, node_color='yellow', font_size=7, font_color='black')
    plt.show()

def salva_tabela(ArquivoPdf):
    #salva tabela em csv com o mesmo nome do arquivo pdf removendo a extensão
    df = vendotabela(ArquivoPdf)
    nome_arquivo = ArquivoPdf.split('.')[0]
    df.to_csv('{}.csv'.format(nome_arquivo), index=False)
    print('Arquivo salvo com sucesso')

def wordcloud_geral_csv():
    #criar uma lista com todos os arquivos csv
    lista_csv = []
    for file in os.listdir('csv'):
        if file.endswith('.csv'):
            lista_csv.append(file)
    #criar uma lista com todos os textos dos arquivos csv
    lista_textos = []
    for file in lista_csv:
        df = pd.read_csv('csv/' + file, sep=',')
        lista_textos.append(df['Palavras'].to_string())
    #juntar todos os textos em uma única string
    texto = ''
    for i in lista_textos:
        texto += str(i)
    #remover stopwords
    texto = texto.lower()
    texto = re.sub(r'[^\w\s]','',texto)
    texto = re.sub(r'\d+','',texto)
    texto = re.sub(r'\s+',' ',texto)
    texto = texto.split()
    texto = [word for word in texto if word not in stopwords]
    texto = ' '.join(texto)
    #plotar wordcloud
    wordcloud = WordCloud(width=800, height=500, max_font_size=110, collocations=False).generate(texto)
    plt.figure(figsize=(10, 7))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis('off')
    plt.show()
    
def wordcloud_geral_pdf():
    #criar uma lista com todos os arquivos pdf
    lista_pdf = []
    for file in os.listdir('planos_de_governo'):
        if file.endswith('.pdf'):
            lista_pdf.append(file)
    #criar uma lista com todos os textos dos arquivos pdf
    lista_textos = []
    for file in lista_pdf:
        with pdfplumber.open('planos_de_governo/' + file) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                lista_textos.append(text)
    #juntar todos os textos em uma única string
    texto = ''
    for i in lista_textos:
        texto += str(i)
    #remover stopwords
    texto = texto.lower()
    texto = re.sub(r'[^\w\s]','',texto)
    texto = re.sub(r'\d+','',texto)
    texto = re.sub(r'\s+',' ',texto)
    texto = texto.split()
    texto = [word for word in texto if word not in stopwords]
    texto = ' '.join(texto)
    #plotar wordcloud
    wordcloud = WordCloud(width=800, height=500, max_font_size=110, collocations=False).generate(texto)
    plt.figure(figsize=(10, 7))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis('off')
    plt.show()

def grafico_barras_geral():
    candidatos = []
    for file in os.listdir('csv'):
        if file.endswith('.csv'):
            candidatos.append(file)
    candidatos = [i.replace('.csv', '') for i in candidatos]
    fig = make_subplots(rows=6, cols=2, subplot_titles=candidatos)
    for candidato in candidatos:
        df = pd.read_csv(f'csv/{candidato}.csv')
        df = df.head(10)
        fig.add_trace(go.Bar(x=df['Palavras'], y=df['Contagem'], name=candidato), row=candidatos.index(candidato)//2+1, col=candidatos.index(candidato)%2+1)
        fig.update_layout(barmode='stack')
    fig.update_xaxes(tickangle = -90)
    fig.show()

def grafico_somatorio():
    somatorio = []
    candidatos = []
    for file in os.listdir('csv'):
        if file.endswith('.csv'):
            candidatos.append(file)
    candidatos = [i.replace('.csv', '') for i in candidatos]
    for candidato in candidatos:
        df = pd.read_csv(f'csv/{candidato}.csv')
        df = df.head(10)
        somatorio.append({'candidato': candidato, 'somatorio' : df['Contagem'].sum()})
    somatorio = pd.DataFrame(somatorio)
    somatorio = somatorio.sort_values(by='somatorio', ascending=False)
    #grafico de barras usando seaborn
    plt.figure(figsize=(10,5))
    sns.barplot(x='candidato', y='somatorio', data=somatorio, palette='Blues_d', edgecolor='black', linewidth=1)
    plt.title('Palavras mais frequentes')
    plt.xticks(rotation=90)
    plt.show()

def wordcloub_final():
    #criar wordcloud lado a lado com os candidatos
    candidatos = []
    for file in os.listdir('csv'):
        if file.endswith('.csv'):
            candidatos.append(file)
    candidatos = [i.replace('.csv', '') for i in candidatos]
    fig = make_subplots(rows=1, cols=2, subplot_titles=candidatos)
    for candidato in candidatos:
        df = pd.read_csv(f'csv/{candidato}.csv')
        df = df.head(10)
        texto = ''
        for i in df['Palavras']:
            texto += str(i)
        texto = texto.lower()
        texto = re.sub(r'[^\w\s]','',texto)
        texto = re.sub(r'\d+','',texto)
        texto = re.sub(r'\s+',' ',texto)
        texto = texto.split()
        texto = [word for word in texto if word not in stopwords]
        texto = ' '.join(texto)
        wordcloud = WordCloud(width=800, height=500, max_font_size=110, collocations=False).generate(texto)
    fig.add_trace(go.Image(z=wordcloud), row=1, col=1)
    fig.update_layout(height=800, width=1800, title_text="Palavras mais frequentes")
    fig.show()

if __name__ == '__main__':
    menu()