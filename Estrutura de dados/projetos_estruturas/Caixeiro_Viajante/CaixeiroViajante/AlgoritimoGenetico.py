
# classe AlgoritimoGenetico --------------------------------------------------------------
from CaixeiroViajante.cidade import Cidade
from CaixeiroViajante.populacao import Individuos


class AlgoritimoGenetico():
    def __init__(self, tamanhoPopulacao, quantidade, geracoes):
        self.tamanhoPopulacao = tamanhoPopulacao
        self.quantidade = quantidade
        self.geracoes = geracoes
        self.melhores = []

    def resolver(self):
        tamanhoPopulacao = self.tamanhoPopulacao
        quantidade = self.quantidade
        geracoes = self.geracoes
        city = Cidade(quantidade)
        cidades = city.gerarDistancias()
        individo = Individuos(tamanhoPopulacao, quantidade)
        populacao = individo.geraCromossomo()
        pop = individo.reproducao(populacao, cidades)
        for i in range(geracoes):
            populacao = []
            for j in range(tamanhoPopulacao):
                populacao.append(pop[j][1])
            resultado = individo.reproducao(populacao, cidades)
            melhor = resultado[0][0]
            self.melhores.append(melhor)
            pop = resultado
        return resultado
