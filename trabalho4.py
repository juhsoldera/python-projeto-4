from random import choice
from pyknow import *

lstRetornos = []

class TorreEmOperacao(Fact):
    pass

class TorreNaoEstaEmOperacao(Fact):
    pass

class CorrosaoSobControle(Fact):
    pass

class RiscoDeCorrosao(Fact):
    pass

class AjustarVazaoAguaLavagem(Fact):
    pass

class AumentarInjecaoNeutralizante(Fact):
    pass


class VerificarCorrosaoTorre(KnowledgeEngine):

    @Rule(Fact(vazaoProduto=P(lambda vazaoProduto: vazaoProduto > 0)))
    def verificaVazaoProduto(self):
        lstRetornos.append("1 - Vazao Produto Verificada!")
        self.declare(TorreEmOperacao())

    @Rule(Fact(vazaoProduto=P(lambda vazaoProduto: vazaoProduto <= 0)))
    def verificaVazaoProduto2(self):
        lstRetornos.append("1 - Vazao Produto Verificada!")
        self.declare(TorreNaoEstaEmOperacao())

    @Rule(TorreNaoEstaEmOperacao())
    def torreNaoEstaEmOperacao(self):
        lstRetornos.append("2 - Torre não está em operacao!")

    @Rule(TorreEmOperacao())
    def torreEmOperacao(self):
        lstRetornos.append("2 - Torre está em operacao!")

    @Rule(TorreEmOperacao(), Fact(phTopoTorre=5.9), Fact(vazaoAguaLavagem=P(lambda vazaoAguaLavagem: vazaoAguaLavagem < 143 and vazaoAguaLavagem > 117)))
    def verificaCorrosaoTorreEstaOk(self):
        lstRetornos.append("3 - Corrosao na torre verificada!")
        self.declare(CorrosaoSobControle())

    @Rule(TorreEmOperacao(), Fact(phTopoTorre=5.0), Fact(vazaoAguaLavagem=P(lambda vazaoAguaLavagem: vazaoAguaLavagem < 143 and vazaoAguaLavagem < 115)))
    def verificaCorrosaoTorreNaoEstaOk2(self):
        lstRetornos.append("3 - Corrosao na torre verificada!")
        self.declare(RiscoDeCorrosao())
        self.declare(AjustarVazaoAguaLavagem())

    @Rule(TorreEmOperacao(), Fact(phTopoTorre=5.0),
          Fact(vazaoAguaLavagem=P(lambda vazaoAguaLavagem: vazaoAguaLavagem < 143 and vazaoAguaLavagem > 117)))
    def verificaCorrosaoTorreNaoEstaOk(self):
        lstRetornos.append("3 - Corrosao na torre verificada!")
        self.declare(RiscoDeCorrosao())
        self.declare(AumentarInjecaoNeutralizante())

    @Rule(CorrosaoSobControle())
    def corrosaoSobControle(self):
        lstRetornos.append("4 - Corrosão sob controle na torre!")

    @Rule(RiscoDeCorrosao())
    def riscodecorrosao(self):
        lstRetornos.append("4 - Risco elevado de corrosão na torre!")

    @Rule(AjustarVazaoAguaLavagem())
    def ajustarVazaoAguaLavagem(self):
        lstRetornos.append("5 - Ajustar Vazao água de lavagem para > 130 * 0,9")

    @Rule(AumentarInjecaoNeutralizante())
    def aumentarInjecaoNeutralizante(self):
        lstRetornos.append("5 - Aumentar a injeção de Neutralizante em 10 %")



engine = VerificarCorrosaoTorre()
engine.reset()
engine.declare(Fact(vazaoProduto=choice([0, 1, 2, 3, 4, 0])))
engine.declare(Fact(phTopoTorre=choice([5.0, 5.9])))
engine.declare(Fact(vazaoAguaLavagem=choice([140, 115, 110, 130, 109, 112])))
engine.run()

lstRetornos.sort()

for retorno in lstRetornos:
    print(retorno)