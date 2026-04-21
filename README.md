Cesar Augusto S Fifolato
RA:2840482421022

Projeto de P.O.O. com Python.  

## Integrantes

 Cesar Augusto



## Jogo implementado

- Jogo da Velha — partida para dois jogadores, via terminal.

---

## Como executar

### Pré-requisitos

- Python 3.8 ou superior
- Nenhuma biblioteca externa necessária

### Rodando o jogo

```bash
cd src
python main.py
```

### Rodando os testes

```bash
python testes/teste_jgdavelha.py
```

---

## Estrutura do projeto

```
TrabPOOCESAR/
├── README.md
├── docs/
├── src/
│   ├── core/                   ← classes genéricas e reutilizáveis
│   │   ├── __init__.py
│   │   ├── jogo.py             ← classe abstrata JogoTabuleiro
│   │   ├── tabuleiro.py        ← grade genérica de casas
│   │   ├── jogador.py          ← representa um jogador
│   │   └── jogada.py           ← representa uma jogada
│   ├── jogos/                  ← implementações concretas
│   │   ├── __init__.py
│   │   └── jogo_da_velha.py    ← JogoDaVelha herda de JogoTabuleiro
│   └── main.py                 ← ponto de entrada
└── testes/
    └── teste_jgdavelha.py      ← testes automatizados
```

---

## Arquitetura

### Visão geral

A arquitetura separa o que é **genérico** (válido para qualquer jogo de tabuleiro) do que é **específico** (regras de cada jogo). Isso permite adicionar novos jogos sem modificar o código já existente.

```
JogoTabuleiro  (classe abstrata — src/core/jogo.py)
      │
      └── JogoDaVelha  (classe concreta — src/jogos/jogo_da_velha.py)
```

### Classes principais

#### `JogoTabuleiro` — *src/core/jogo.py*

Classe abstrata que define o contrato que todo jogo deve seguir.  
Não implementa regras específicas — apenas os comportamentos comuns a qualquer jogo de tabuleiro.

Métodos abstratos que toda subclasse deve implementar:

| Método | Responsabilidade |
|---|---|
| `inicializar()` | Prepara o tabuleiro para começar |
| `validar_jogada(jogada)` | Verifica se uma jogada é permitida |
| `aplicar_jogada(jogada)` | Efetua a jogada no tabuleiro |
| `verificar_fim()` | Detecta vitória, derrota ou empate |
| `exibir()` | Exibe o estado atual no terminal |

Atributos e métodos herdados por todos os jogos:

- `jogador_atual` — retorna de quem é a vez
- `avancar_turno()` — passa a vez para o próximo jogador

#### `Tabuleiro` — *src/core/tabuleiro.py*

Representa a grade de casas de qualquer jogo. Não conhece regras — apenas guarda e fornece o estado das posições.

Responsabilidades: armazenar valores nas casas, verificar se uma casa está vazia, verificar se uma posição existe dentro dos limites.

#### `Jogador` — *src/core/jogador.py*

Representa um jogador com nome e símbolo (ex: "X", "O"). Atributos encapsulados e acessados via `@property`.

#### `Jogada` — *src/core/jogada.py*

Representa a intenção de jogar em uma posição (linha, coluna) por um determinado jogador. É um objeto de dados simples, sem lógica.

#### `JogoDaVelha` — *src/jogos/jogo_da_velha.py*

Implementação concreta que herda de `JogoTabuleiro`. Implementa todas as regras específicas do Jogo da Velha: tabuleiro 3×3, vitória por linha, coluna ou diagonal, e detecção de empate.

---

## Conceitos de POO aplicados

### Abstração

`JogoTabuleiro` é uma classe abstrata (usa `ABC` do módulo `abc`). Ela define *o que* todo jogo deve fazer, sem definir *como*. Nenhum objeto pode ser criado diretamente a partir dela.

```python
from abc import ABC, abstractmethod

class JogoTabuleiro(ABC):
    @abstractmethod
    def validar_jogada(self, jogada):
        pass
```

### Herança

`JogoDaVelha` herda de `JogoTabuleiro` e é obrigada a implementar todos os métodos abstratos. Isso garante que qualquer jogo novo seguirá o mesmo contrato.

```python
class JogoDaVelha(JogoTabuleiro):
    def validar_jogada(self, jogada):
        # implementação específica do Jogo da Velha
        ...
```

### Polimorfismo

O `main.py` pode chamar `jogo.validar_jogada()`, `jogo.aplicar_jogada()` e `jogo.verificar_fim()` sem saber se está lidando com Jogo da Velha, Damas ou qualquer outro jogo — cada um responde do seu jeito.

### Encapsulamento

Os atributos internos das classes usam o prefixo `_` (convenção Python para "privado") e são acessados externamente apenas via `@property`, evitando exposição desnecessária do estado interno.

```python
class Jogador:
    def __init__(self, nome, simbolo):
        self._nome = nome       # privado

    @property
    def nome(self):             # acesso controlado
        return self._nome
```

### Relações entre objetos

| Relação | Exemplo |
|---|---|
| **Composição** | `JogoDaVelha` cria e possui um `Tabuleiro` |
| **Associação** | `JogoTabuleiro` referencia uma lista de `Jogador` |
| **Dependência** | `validar_jogada` recebe um objeto `Jogada` como parâmetro |
| **Herança** | `JogoDaVelha` herda de `JogoTabuleiro` |

---

## Extensibilidade

Para adicionar um novo jogo (ex: Lig-4), basta:

1. Criar um arquivo em `src/jogos/lig4.py`
2. Criar uma classe que herda de `JogoTabuleiro`
3. Implementar os 5 métodos abstratos com as regras do novo jogo

Nenhum arquivo do `core/` precisa ser modificado.

```python
# src/jogos/lig4.py
from core.jogo import JogoTabuleiro
from core.tabuleiro import Tabuleiro

class Lig4(JogoTabuleiro):
    def inicializar(self):
        self._tabuleiro = Tabuleiro(6, 7)  # grade 6x7

    def validar_jogada(self, jogada):
        # regras específicas do Lig-4
        ...
```

---

## Testes

Os testes estão em `testes/teste_jgdavelha.py` e cobrem:

| Teste | O que verifica |
|---|---|
| `test_jogada_valida` | Casa livre é aceita |
| `test_jogada_fora_do_tabuleiro` | Posição inexistente é rejeitada |
| `test_jogada_em_casa_ocupada` | Casa já ocupada é rejeitada |
| `test_vitoria_por_linha` | Três em linha detecta vitória |
| `test_vitoria_por_coluna` | Três em coluna detecta vitória |
| `test_vitoria_por_diagonal` | Diagonal detecta vitória |
| `test_empate` | Tabuleiro cheio sem vencedor detecta empate |

Resultado esperado:

```
Ran 7 tests in 0.001s
OK
```

---

## Decisões de projeto

**Por que usar classe abstrata em vez de herança simples?**  
A classe abstrata (`ABC`) garante em tempo de execução que nenhum jogo concreto esqueça de implementar um método obrigatório. Se uma subclasse não implementar `verificar_fim()`, por exemplo, Python lança um erro imediatamente ao tentar criar um objeto dessa classe.

**Por que `Tabuleiro` não conhece regras?**  
Separar o estado (o que está em cada casa) da lógica (o que é válido fazer) mantém o código mais fácil de testar e reutilizar. O `Tabuleiro` de um Jogo da Velha e o de um Lig-4 são idênticos — só o tamanho muda.

**Por que `Jogada` é uma classe e não só dois números?**  
Encapsular linha, coluna e jogador em um objeto torna o código mais legível e facilita passar essa informação entre métodos sem aumentar a quantidade de parâmetros.

---

## Limitações e melhorias futuras

- Não há suporte a jogos com peças que se movem (ex: Damas, Xadrez) — a arquitetura atual foi pensada para jogos de colocação
- Não há interface gráfica — a interação é feita inteiramente via terminal
- Os testes cobrem o Jogo da Velha; novos jogos precisariam de seus próprios arquivos de teste
- Poderia ser adicionada uma classe `Peca` para representar peças com atributos próprios (cor, tipo, posição)
