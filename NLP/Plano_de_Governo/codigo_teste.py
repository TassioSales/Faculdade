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
nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('portuguese')
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
            print('7 - Sair')

    
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
                return False
                os.system('exit')
                
        except ValueError:
            print('Opção inválida')
        except Exception as e:
            print('Erro: {}'.format(e))


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

if __name__ == '__main__':
    menu()

    