# src/core/ jogada.py

class Jogada: # cria a classe jogada
    def __init__(self, linha, coluna, jogador): # def define a funscao
        self._linha = linha
        self._coluna = coluna
        self._jogador = jogador
 # o underline eh dda convencao de atributo protegido 
 
    @property    # property deixa acessar como atributo, mas eh metodo
    def linha(self): 
        return self._linha



    @property
    def coluna(self): 
        return self._coluna 

    @property
    def jogador(self):
        return self._jogador
    
#encapsulamento em _linha e acesso controlado @prop