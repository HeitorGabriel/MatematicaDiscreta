from itertools import combinations
class Conjunto():
    def __init__(self, conjunto = [], nome=None):
        self.conjunto = conjunto
        self.nome = nome

    def adicionar(self, valor):
        if valor not in self.conjunto:
            self.conjunto.append(valor)

    def remover(self, valor):
        if valor in self.conjunto:
            self.conjunto.remove(valor)

    def pertinencia(self, valor):
        return valor in self.conjunto

    def __Contido(self, conjunto):
        for e in self.conjunto:
            if not conjunto.pertinencia(e):
                return False
        return True

    def contido(self, conjunto):
        if len(conjunto.conjunto) == len(self.conjunto):
            return self.__Contido(conjunto)
        return False
            
    def contidoPropriamente(self, conjunto):
        if len(conjunto.conjunto) > len(self.conjunto):
            return self.__Contido(conjunto)
        return False

    def uniao(self, subconjunto):
        conjuntoResultante = Conjunto(conjunto=self.conjunto)
        for e in subconjunto.conjunto:
            conjuntoResultante.adicionar(e)
        return conjuntoResultante

    def interseccao(self, subconjunto):
        conjuntoResultante = Conjunto()
        for e in subconjunto.conjunto:
            if self.pertinencia(e):
                conjuntoResultante.adicionar(e)
        return conjuntoResultante

    def diferenca(self, subconjunto):
        conjuntoResultante = Conjunto()
        for e in self.conjunto:
            if not subconjunto.pertinencia(e):
                conjuntoResultante.adicionar(e)
        return conjuntoResultante

    def complementar(self, subconjunto):
        if len(self.conjunto) <= len(subconjunto.conjunto):
            return subconjunto.diferenca(self)

    def produtoCartesiano(self, subconjunto):
        conjuntoResultante = Conjunto()
        for e in self.conjunto:
            for e2 in subconjunto.conjunto:
                conjuntoResultante.adicionar((e,e2))
        return conjuntoResultante

    def conjuntoDasPartes(self):
        conjuntoResultante = Conjunto(conjunto=[Conjunto()])
        for i in range(1,len(self.conjunto)+1):
            for e in list(combinations(self.conjunto,i)):
                c = Conjunto(conjunto=list(e))
                conjuntoResultante.adicionar(c)
        return conjuntoResultante
            
            
        
    def uniaoDisjunta(self, conjunto):
        conjuntoResultante = Conjunto()
        num = len(self.conjunto) if len(self.conjunto) >= len(conjunto.conjunto) else len(conjunto.conjunto)
        for i in range(num):
            try:
                conjuntoResultante.conjunto.append((self.conjunto[i], self.nome))
            except IndexError:
                pass
            try:
                conjuntoResultante.conjunto.append((conjunto.conjunto[i], conjunto.nome))
            except IndexError:
                pass
        return conjuntoResultante
            

    def imprimir(self):
        for e in self.conjunto:
            if isinstance(e, Conjunto):
                print(e.conjunto, end=", ")
            else:
                print(e, end=", ")
            
        
    

A = Conjunto(conjunto=[1,2], nome="A")
B = A.conjuntoDasPartes()


for e in B.conjunto:
    print(e.conjunto)

