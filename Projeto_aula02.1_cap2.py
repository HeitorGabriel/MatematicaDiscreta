class Conjunto():
    def __init__(self):
        self.conjunto = []

    def adicionar(self, valor):
        if valor not in self.conjunto:
            self.conjunto.append(valor)

    def remover(self, valor):
        if valor in self.conjunto:
            self.conjunto.remove(valor)
        else:
            raise "Valor não está no conjunto"

    def pertinencia(self, valor):
        return valor in self.conjunto

    def contido(self, conjunto):
        for e in self.conjunto:
            if not conjunto.pertinencia(e):
                return False
        return True
            
    def contitoPropriamente(self, subconjunto):
        return self.contido(subconjunto)

    def uniao(self, subconjunto):
        for e in subconjunto.conjunto:
            self.adicionar(e)

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
                

    def imprimir(self):
        for e in self.conjunto:
            print(e)
        
    


A = Conjunto()
A.adicionar(4)
A.adicionar(5)

B = Conjunto()
B.adicionar(4)
B.adicionar(5)
B.adicionar(6)
B.adicionar(7)
B.adicionar(8)

##A.imprimir()
            
##C = A.interseccao(B)
##C.imprimir()

##D = B.diferenca(A)
##D.imprimir()

E = A.produtoCartesiano(B)
E.imprimir()


