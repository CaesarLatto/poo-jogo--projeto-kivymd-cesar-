Cesar Augusto S Fifolato
RA:2840482421022

PARTE 2:
Projeto de P.O.O. com Python e KivyMD.  

## Integrantes

 Cesar Augusto


## WORK IN PROGRESS
## Jogo implementado

- Jogo da Velha — partida para dois jogadores, via ~~terminal~~ KivyMD!!


---

## COMO RODAR:

```bash
cd c:\Users\Cesar\Downloads\TrabPOOCESAR
.\venv\Scripts\python.exe src\appkivy.py

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

