Cesar Augusto S Fifolato
RA:2840482421022

Projeto de P.O.O. com Python.  

## Integrantes

 Cesar Augusto



## Jogo implementado

- Jogo da Velha — partida para dois jogadores, via terminal.

---

## Como executar

```bash
cd src
python main.py
```

Para rodar os testes:

```bash
python testes/teste_jgdavelha.py
```

## Arquitetura

O projeto é dividido em duas camadas: o `core` e os `jogos`.

O `core` contém as classes genéricas que funcionam para qualquer jogo de tabuleiro. Os `jogos` contém as implementações concretas de cada jogo, usando a base do `core`.

A classe central é `JogoTabuleiro`, uma classe abstrata que define o contrato que todo jogo deve seguir. Ela obriga qualquer jogo concreto a implementar cinco métodos: `inicializar`, `validar_jogada`, `aplicar_jogada`, `verificar_fim` e `exibir`. Além dela, o core tem `Tabuleiro`, que representa a grade de casas, `Jogador`, que guarda nome e símbolo de um jogador, e `Jogada`, que representa a intenção de jogar em uma posição.

`JogoDaVelha` herda de `JogoTabuleiro` e implementa as regras específicas: tabuleiro 3x3, vitória por linha, coluna ou diagonal, e detecção de empate.

## Conceitos de POO aplicados

**Abstração:** `JogoTabuleiro` usa `ABC` e `@abstractmethod`. Nenhum objeto pode ser criado diretamente a partir dela.

**Herança:** `JogoDaVelha` herda de `JogoTabuleiro` e é obrigada a implementar todos os métodos abstratos.

**Polimorfismo:* o loop do jogo chama `validar_jogada`, `aplicar_jogada` e `verificar_fim` sem saber qual jogo está rodando — cada subclasse responde do seu jeito.

**Encapsulamento:** todos os atributos usam o prefixo `_` e são acessados via `@property`.

**Relações entre objetos:** `JogoDaVelha` possui um `Tabuleiro` por composição. `JogoTabuleiro` referencia uma lista de `Jogador` por agregação. `Jogada` referencia o `Jogador` que a fez por associação.

## Extensibilidade

Para adicionar um novo jogo, basta criar um arquivo em `src/jogos/` com uma classe que herda de `JogoTabuleiro` e implementa os 5 métodos obrigatórios. Nenhum arquivo do `core` precisa ser modificado.

## Decisões de projeto

A classe `Peca` descrita no enunciado foi omitida intencionalmente. No Jogo da Velha, a peça se reduz a um símbolo, então É representada diretamente como atributo nome do jogador, simplificando a arquitetura.

O `Tabuleiro` não conhece regras, ele apenas guarda e fornece o estado das casas. Isso permite que o mesmo `Tabuleiro` seja reutilizado por qualquer jogo, independente das suas regras.

## Limitações e melhorias futuras

A arquitetura atual foi pensada para jogos de colocação de peças. Jogos com peças que se movem, como Damas ou Xadrez, exigiriam uma classe `Peca` com atributos de posição e tipo. A interação é feita inteiramente via terminal, sem interface gráfica. Novos jogos precisariam de seus próprios arquivos de teste.
