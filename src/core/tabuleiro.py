#      src/core/tabuleiro.py


class Tabuleiro: #define class tabuleiro, campo

    def __init__(self, linhas, colunas):
        self._linhas = linhas 
        self._colunas = colunas
        # grade começa toda vazia (None = vazio)
        self._grade = [[None] * colunas for _ in range(linhas)] 
# self._grade armazena estado do tabuleiro. for pra criar lista
#range pra setar o range.  none eh porque comeca vazio


    def get_casa(self, linha, coluna):
        return self._grade[linha][coluna]



    def set_casa(self, linha, coluna, valor):  #valor X ou O
        self._grade[linha][coluna] = valor


    def casa_vazia(self, linha, coluna):
        return self._grade[linha][coluna] is None

    def dentro_dos_limites(self, linha, coluna):
        return 0 <= linha < self._linhas and 0 <= coluna < self._colunas
 # se a linha e coluna estao dentro dos limites, true


    @property
    def linhas(self):
        return self._linhas

    @property

    def colunas(self):
        return self._colunas
    

