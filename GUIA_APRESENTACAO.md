# 🎤 GUIA DE APRESENTAÇÃO

Dicas para apresentar o projeto ao professor.

---

## ⏱️ Estrutura da Apresentação (10-15 minutos)

### 1️⃣ Introdução (1 min)
```
"Oi professor! Desenvolvemos o Jogo da Velha com Python e KivyMD,
focando em Programação Orientada a Objetos e boas práticas."
```

### 2️⃣ Demonstração Prática (3-4 min)
1. Rodar a aplicação: `python src/appkivy.py`
2. Mostrar tela de menu (cores, ícones)
3. Iniciar um jogo (jogar algumas rodadas)
4. Ganhar/Empatar (mostrar tela de resultado)
5. Voltar e jogar novamente

**O que falar:**
- "Vê as cores? Teal e Amber (Material Design)"
- "O tabuleiro é responsivo - funciona em qualquer resolução"
- "X é vermelho, O é azul - feedback visual"
- "Tela de resultado dedicada - UX melhorada"

### 3️⃣ Arquitetura (2-3 min)
Mostrar diagrama (em CHECKLIST_FINAL.md ou README.md):
```
JogoTabuleiro (Abstrata)
    ↑
    └── JogoDaVelha (Concreta)
            - Tabuleiro (Composição)
            - Jogador (Agregação)
            - Jogada (Associação)
```

**O que falar:**
- "Separação clara entre lógica (core) e interface (views)"
- "Vamos ver os 7 conceitos de POO em ação..."

### 4️⃣ Conceitos de POO (2-3 min)
```
📌 ABSTRAÇÃO
   - Classe JogoTabuleiro usa ABC e @abstractmethod
   - Código: core/jogo.py (linhas 1-10)

📌 HERANÇA
   - JogoDaVelha herda de JogoTabuleiro
   - Obrigada a implementar 5 métodos

📌 POLIMORFISMO
   - Cada subclasse implementa diferente
   - Loop chama mesmos métodos, mas comportamento varia

📌 ENCAPSULAMENTO
   - Prefixo _ em atributos
   - Acesso via @property (só leitura)

📌 COMPOSIÇÃO/AGREGAÇÃO/ASSOCIAÇÃO
   - Relações entre objetos bem definidas
```

### 5️⃣ KivyMD e Design (1-2 min)
```
Componentes usados:
- MDButton (Começar, Reiniciar, Voltar)
- MDTextField (Entrada de nomes)
- MDLabel (Textos)
- MDGridLayout (Tabuleiro 3x3)
- MDCard (Menu, Turno, Resultado) ← NOVO
- MDTopAppBar (Cabeçalho)
- ScreenManager (Navegação)
- Ícones (play, restart, arrow-left) ← NOVO

Responsividade:
- size_hint em vez de tamanhos fixos
- Layouts adaptáveis
- Funciona em mobile, tablet, desktop
```

### 6️⃣ Fechamento (1 min)
```
"Melhorias v2.0:
✓ +Responsividade
✓ +Tema Material Design
✓ +Componentes KivyMD
✓ +Tela de resultado
✓ +Documentação completa

De 77 para 100 pontos!"
```

---

## ❓ Perguntas Esperadas (+ Respostas)

### POO
**P: "Por que usar classe abstrata?"**
R: Para forçar que cada jogo implemente os métodos obrigatórios. Se alguém tentar criar um JogoTabuleiro diretamente, dá erro.

**P: "Como adicionar um novo jogo?"**
R: Criar uma classe que herda de JogoTabuleiro e implementa os 5 métodos. A UI não precisa mudar - polimorfismo!

**P: "Por que separar core e views?"**
R: Reutilização e manutenção. Temos versão terminal e KivyMD usando mesma lógica. Se mudarmos UI, lógica não muda.

### KivyMD
**P: "Por que usar MDCard?"**
R: Melhor apresentação visual. Sombra e profundidade (Material Design). Deixa mais profissional.

**P: "Como ficaria em mobile?"**
R: size_hint torna responsivo automaticamente. KivyMD suporta mobile nativamente.

**P: "Como mudar cores?"**
R: Atualizar `theme_cls` e `md_bg_color` em appkivy.py.

### Geral
**P: "Qual versão de Python?"**
R: Python 3.8+. Testado em [sua versão].

**P: "Funcionaria sem KivyMD?"**
R: Sim! Temos main.py (versão terminal). Core é independente.

**P: "Como foram os testes?"**
R: Testes unitários em testes/teste_jgdavelha.py. Validam regras do jogo.

---

## 📊 O Que Mostrar na Tela

### Prepare Screenshots de:
1. Menu (cores, ícones)
2. Tabuleiro durante jogo
3. Tela de resultado
4. Diagrama UML
5. Código (jogo.py abstrata)

### Durante Demo, Mostre:
1. Navegar por todas as telas
2. Jogar um jogo inteiro
3. Clicar em botões inválidos (erro em vermelho)
4. Vitória vs Empate
5. Jogar novamente (lógica reutiliza)

---

## 🎯 Pontos-Chave para Enfatizar

1. **POO**: 7 conceitos demonstrados, não apenas teoria
2. **Reutilização**: 2 versões (terminal + gráfica) com mesma lógica
3. **Design**: Material Design profissional com cores coerentes
4. **Responsividade**: Funciona em qualquer tamanho
5. **Documentação**: README, UML, diagrama de fluxo, testes
6. **Melhorias**: De 77 para 100 pontos em 5 alterações

---

## ⚠️ Coisas a Evitar

❌ Não fale sobre erros que já foram corrigidos
❌ Não se desculpe por coisas simples
❌ Não leia slides palavra por palavra
❌ Não foque em detalhes técnicos desnecessários
❌ Não use jargão sem explicar

---

## ✨ Frases Impactantes

```
"Separamos a lógica da interface para reutilização"
"Usamos polimorfismo para adicionar novos jogos sem modificar código"
"Material Design torna a interface profissional e moderna"
"De 77 para 100 pontos com 5 melhorias focadas"
"Tudo pronto, testado e documentado"
```

---

## 🎬 Ensaio Sugerido

1. **Dia antes da apresentação**: Ensaie sozinho
2. **Dias antes**: Ensaie com amigos/família
3. **Dia da apresentação**: Chegue cedo, teste tudo funciona

**Tempo**: Objetivo é 10-15 min total

---

## ✅ Checklist Pré-Apresentação

- [ ] Código testado e funciona
- [ ] KivyMD instalado (`pip install -r requirements.txt`)
- [ ] Aplicação roda sem erros
- [ ] Screenshots preparados
- [ ] Diagrama UML na mão
- [ ] Respostas memorizadas
- [ ] Ensaio feito (pelo menos 1x)
- [ ] Não se esqueceu de nada
- [ ] Backup do código (em pen-drive?)

---

## 🎓 Dica Final

> Fale com **confiança**! Você fez um projeto excelente.
> De 77 para 100 pontos não é coincidência.
> Você trabalhou duro e merece apresentar bem.

**Boa sorte!** 🍀

---

**Lembre-se**: O professor quer ver que você:
1. ✓ Entende POO
2. ✓ Sabe programar bem
3. ✓ Documenta seu trabalho
4. ✓ Faz UI/UX decente
5. ✓ Demonstra criatividade

Você tem tudo isso! Agora é só apresentar. 🚀
