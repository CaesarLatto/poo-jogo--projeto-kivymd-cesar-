Cesar Augusto S Fifolato
RA:2840482421022

# Projeto de P.O.O. com Python e KivyMD - Jogo da Velha

## Integrantes

- Cesar Augusto


## 📱 Jogo Implementado

- **Jogo da Velha** — partida para dois jogadores, com interface gráfica KivyMD


---

## ⚙️ Requisitos do Sistema

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)


---

## 🚀 Como Instalar e Rodar

### Opção 1: Instalação com `pip` (Recomendado)

```bash
# Navegar até a pasta do projeto
cd c:\Users\Cesar\Downloads\TrabPOOCESAR

# Instalar dependências
pip install -r requirements.txt

# Executar a aplicação
python src/appkivy.py
```

### Opção 2: Usando virtual environment (Recomendado para desenvolvimento)

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# No Windows:
.\venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Executar a aplicação
python src/appkivy.py
```

### Opção 3: Versão terminal (sem KivyMD)

```bash
python src/main.py
```


---

## 📋 Arquitetura do Projeto

O projeto é dividido em **duas camadas principais**: o `core` e os `jogos`, com separação completa entre lógica e interface gráfica.

### Estrutura de Pastas

```
src/
├── core/                    # Camada de lógica do jogo
│   ├── __init__.py
│   ├── jogo.py             # Classe abstrata JogoTabuleiro
│   ├── tabuleiro.py        # Classe Tabuleiro (grade 3x3)
│   ├── jogador.py          # Classe Jogador (nome + símbolo)
│   └── jogada.py           # Classe Jogada (linha + coluna + jogador)
├── jogos/                   # Implementações específicas de jogos
│   ├── __init__.py
│   └── jogo_da_velha.py    # JogoDaVelha herda de JogoTabuleiro
├── views/                   # Views (estrutura para múltiplas telas)
│   ├── menuscreen.py
│   ├── boardscreen.py
│   ├── configscreen.py
│   └── resultscreen.py
├── app.kv                   # Definição de UI em KivyMD (linguagem declarativa)
├── appkivy.py              # Aplicação KivyMD (interface gráfica)
├── main.py                 # Aplicação terminal (sem interface gráfica)
└── controller/              # Controladores (MVC pattern)
    └── game_controller.py
```

### Fluxo de Lógica

```
JogoTabuleiro (classe abstrata)
    ↑
    └── JogoDaVelha (implementação concreta)
            - Tabuleiro (composição)
            - Lista de Jogador (agregação)
            - Jogada (associação)
```


---

## 🎯 Conceitos de P.O.O. Aplicados

### 1. **Abstração**
- `JogoTabuleiro` usa `ABC` (Abstract Base Class) e `@abstractmethod`
- Nenhum objeto pode ser criado diretamente a partir dela
- Define o contrato que todo jogo deve seguir

### 2. **Herança**
- `JogoDaVelha` herda de `JogoTabuleiro`
- É obrigada a implementar todos os métodos abstratos
- Reutiliza funcionalidade comum da classe pai

### 3. **Polimorfismo**
- O loop do jogo chama `validar_jogada()`, `aplicar_jogada()` e `verificar_fim()`
- Cada subclasse responde de acordo com suas regras específicas
- Permite adicionar novos jogos sem modificar o código existente

### 4. **Encapsulamento**
- Todos os atributos usam o prefixo `_` (convenção de protegido)
- Acesso controlado via `@property` (leitura)
- Sem setters (atributos imutáveis após criação)
- Exemplo: `self._nome` acessado via `jogador.nome`

### 5. **Relações entre Objetos**
- **Composição**: `JogoDaVelha` possui um `Tabuleiro`
- **Agregação**: `JogoTabuleiro` referencia uma lista de `Jogador`
- **Associação**: `Jogada` referencia o `Jogador` que a fez


---

## 🎨 Componentes KivyMD Utilizados

| Componente | Uso |
|-----------|-----|
| `MDRaisedButton` | Botões de ação (começar jogo, reiniciar) |
| `MDFlatButton` | Botões secundários (voltar) |
| `MDTextField` | Entrada de nomes dos jogadores |
| `MDLabel` | Exibição de texto (título, turno, resultado) |
| `MDGridLayout` | Grade 3x3 do tabuleiro |
| `MDBoxLayout` | Layout vertical/horizontal |
| `MDCard` | Container com sombra (menu, turno, resultado) |
| `MDTopAppBar` | Barra de título com botão de voltar |
| `AnchorLayout` | Centralização do tabuleiro |
| `ScreenManager` | Gerenciamento de telas |
| `MDScreen` | Telas da aplicação |


---

## 🎮 Como Jogar

1. **Iniciar**: Execute `python src/appkivy.py`
2. **Menu**: Digite os nomes dos dois jogadores e clique em "Começar Jogo"
3. **Tabuleiro**: 
   - O jogador X (primeiro) começa
   - Clique nas casas vazias para jogar
   - O turno passa automaticamente
4. **Resultado**: Quando alguém vencer ou der empate, a tela mostra o resultado
5. **Jogar Novamente**: Clique em "Jogar Novamente" ou "Menu Principal"


---

## 📊 Regras do Jogo da Velha

- Tabuleiro 3x3
- Dois jogadores (X e O)
- Ganha quem fizer 3 em linha (horizontal, vertical ou diagonal)
- Se preenchidas todas as 9 casas sem vencedor = empate


---

## 🧪 Testes Unitários

O projeto inclui testes unitários para validar a lógica do jogo:

```bash
python -m unittest testes.teste_jgdavelha -v
```

### Testes Implementados:
- ✓ Validação de jogadas
- ✓ Detecção de vitória por linha/coluna/diagonal
- ✓ Detecção de empate
- ✓ Rejeição de posições inválidas


---

## 📐 Diagrama UML Simplificado

```
┌────────────────────────────────────┐
│     <<abstract>> JogoTabuleiro     │
├────────────────────────────────────┤
│ - _jogadores: List[Jogador]        │
│ - _turno_atual: int                │
│ - _encerrado: bool                 │
├────────────────────────────────────┤
│ + inicializar()                    │
│ + validar_jogada(jogada)           │
│ + aplicar_jogada(jogada)           │
│ + verificar_fim(): bool            │
│ + exibir()                         │
└────────────────────────────────────┘
           ↑
           │ extends
           │
┌────────────────────────────────────┐
│      JogoDaVelha                   │
├────────────────────────────────────┤
│ - _tabuleiro: Tabuleiro            │
│ - _vencedor: Optional[Jogador]     │
├────────────────────────────────────┤
│ + [métodos abstratos implementados]│
└────────────────────────────────────┘

┌────────────────────────────────────┐
│          Tabuleiro                 │
├────────────────────────────────────┤
│ - _linhas: int                     │
│ - _colunas: int                    │
│ - _grade: List[List]               │
├────────────────────────────────────┤
│ + get_casa(linha, coluna)          │
│ + set_casa(linha, coluna, valor)   │
│ + casa_vazia(linha, coluna): bool  │
└────────────────────────────────────┘

┌────────────────────────────────────┐
│          Jogador                   │
├────────────────────────────────────┤
│ - _nome: str                       │
│ - _simbolo: str                    │
├────────────────────────────────────┤
│ + nome: str (property)             │
│ + simbolo: str (property)          │
└────────────────────────────────────┘

┌────────────────────────────────────┐
│           Jogada                   │
├────────────────────────────────────┤
│ - _linha: int                      │
│ - _coluna: int                     │
│ - _jogador: Jogador                │
├────────────────────────────────────┤
│ + linha: int (property)            │
│ + coluna: int (property)           │
│ + jogador: Jogador (property)      │
└────────────────────────────────────┘
```


---

## 🎨 Melhorias Implementadas (Versão 2.0)

- ✅ Responsividade com `size_hint` em vez de tamanhos fixos
- ✅ Tema Material Design (Teal + Amber)
- ✅ Cores personalizadas em botões e componentes
- ✅ MDCard para melhor apresentação
- ✅ Tela de resultados dedicada
- ✅ Ícones nos botões
- ✅ Feedback visual (cores dos botões X vs O)
- ✅ Mensagens com emojis para melhor UX
- ✅ requirements.txt para instalação fácil


---

## 📝 Licença

Este é um projeto acadêmico de P.O.O.



