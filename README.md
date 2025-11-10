# Star Wars: Aliança Rebelde – Floresta de Dados

<div align="center">
    Figura 1: Aliança Rebelde – Floresta de Dados
    <br>
    <img src="https://raw.githubusercontent.com/EDAII/Algoritmos_Busca_Alianca_Rebelde/refs/heads/main/Imagens/alianca_simbolo.png" width="500">
    <br>
    <br>
</div>

**Número da Lista:** 3  
**Conteúdo da Disciplina:** Árvores Balanceadas  
<br>

## Alunas
| Matrícula | Aluna |
| -- | -- |
| 21/1039573 | Larissa Stéfane Barboza Santos |
| 21/1029497 | Mylena Angélica Silva Farias |
<br>


### Equilibrar para resistir!

**"Aliança Rebelde – Floresta de Dados"** é um jogo de puzzle e simulação, em que o jogador assume o papel de **Analista de Estruturas da Rebelião**.  
A Aliança está armazenando dados secretos e precisa mantê-los **organizados, balanceados e de acesso rápido**, mesmo sob ataque Imperial.  
Para isso, você irá operar **árvores balanceadas**, garantindo que as informações permaneçam seguras e rapidamente acessíveis.

Cada desafio do jogo é uma simulação interativa que mostra como **árvores Rubro-Negras e AVL** mantêm o equilíbrio da Rebelião.  
A narrativa segue o universo de Star Wars, com uma abordagem didática e lúdica para o aprendizado de Estruturas de Dados.

Para compreender melhor sobre o jogo, suas missões e a relação com as estruturas de dados, acesse a [Descrição](Descricao.md).


## Inspiração

Este projeto é a continuidade do universo criado pelas estudantes em módulos anteriores da saga **Aliança Rebelde**, que exploram os algoritmos de forma narrativa e visual.  
Após lidar com buscas e ordenações, a Rebelião agora precisa de **eficiência e estabilidade** em suas bases de dados.  
As **árvores balanceadas** são a chave para manter o sistema rebelde funcionando, mesmo sob pressão.

Os repositórios anteriores podem ser acessados nos links abaixo:

**Projeto de algoritmos**

- [Greed – Aliança Rebelde](https://github.com/projeto-de-algoritmos-2025/Greed_Alianca_Rebelde)  
- [Divide and Conquer – Aliança Rebelde 2](https://github.com/projeto-de-algoritmos-2025/DC_Alianca_Rebelde_2)  
- [Programação Dinâmica – Aliança Rebelde: Confronto Final](https://github.com/projeto-de-algoritmos-2025/PD_Alianca_Rebelde_Confronto_Final)

**Estrutura de dados 2**
- [Algoritmos de Busca – Aliança Rebelde](https://github.com/EDAII/Algoritmos_Busca_Alianca_Rebelde)  
- [Algoritmos de Ordenação – Aliança Rebelde](https://github.com/EDAII/Algoritmos_Ordenacao_Alianca_Rebelde)  
<br>

## Estrutura do Projeto

O jogo é dividido em dois conjuntos de missões, localizados em pastas separadas, mas que compartilham o mesmo tema central de **árvores balanceadas**:

- `JogoArvores/` → contém as interfaces e minigames das missões  
- `Arvores/` → contém as implementações das estruturas Rubro-Negra e AVL  

<br>

## Missões do Jogo (Desafios de Árvores) em JogoArvores

Localização da pasta: [JogoArvores](https://github.com/EDAII/Algoritmos_Arvores_Alianca_Rebelde/tree/main/JogoArvores)

**Estruturas Focadas:**  
Árvore Rubro-Negra e Árvore AVL

Cada missão é um minigame projetado para ensinar as operações e o balanceamento de cada árvore.

---

### Missão 1: Sentinelas de Scarif – Árvore Rubro-Negra

**Objetivo:**  
Inserir registros de agentes rebeldes e manter o sistema estável aplicando as regras da árvore Rubro-Negra:
- Inserção como nó vermelho  
- Verificação das propriedades da árvore  
- Recoloração de pai e tio  
- Rotações simples e duplas quando necessário  

**Contexto:**  
Os registros de inteligência da Rebelião estão sendo adicionados em tempo real.  
Se a estrutura ficar desbalanceada, os acessos se tornam lentos e vulneráveis à detecção pelo Império.  
As árvores rubro-negras mantêm o sistema com **altura controlada**, garantindo **buscas rápidas e seguras**.

<div align="center">
    Figura 2: Introdução Missão 1
    <br>
    <img src="https://github.com/EDAII/Arvores_Alianca_Rebelde/blob/main/screenshots/missao1-intro-arvores.png?raw=true" width="500">
    <br><br>
</div>

---

### Missão 2: Santuário de Endor – Árvore AVL

**Objetivo:**  
Gerenciar dados da base rebelde em Endor, mantendo o equilíbrio a cada inserção e remoção:
- Cálculo do **fator de balanceamento**  
- Aplicação de rotações simples (direita/esquerda)  
- Aplicação de rotações duplas (direita-esquerda e esquerda-direita)  

**Contexto:**  
A base de Endor está expandindo e armazenando dados de recursos como naves, combustível e escudos.  
Para garantir eficiência, utiliza-se uma **árvore AVL**, que reequilibra a estrutura sempre que o fator de balanceamento ultrapassa ±1.  
O jogador acompanha as inserções passo a passo e vê as rotações acontecerem.

<div align="center">
    Figura 3: Introdução Missão 2
    <br>
    <img src="https://raw.githubusercontent.com/EDAII/Arvores_Alianca_Rebelde/refs/heads/main/screenshots/missao2-intro-arvores.png" width="500">
    <br><br>
</div>

---

## Dados Utilizados

Para a simulação, foram utilizados subconjuntos do **Star Wars Dataverse** (Kaggle), com dados de:
- Personagens (nomes, anos de nascimento, espécies)  
- Naves (modelo, comprimento, fabricante)  
- Planetas (população e clima)  

Esses dados são convertidos em **chaves numéricas ou textuais**, usadas nas inserções das árvores.

<br>

## Link do vídeo

[Assista ao vídeo aqui](https://www.youtube.com/watch?v=T8YVo-bmBDw)

<br>

## Screenshots

### Intro

<div align="center">
    Figura 4: Introdução do jogo
    <br>
    <img src="https://github.com/EDAII/Arvores_Alianca_Rebelde/blob/main/screenshots/intro-arvores.png?raw=true" width="500">
    <br><br>
</div>

### Missão 1 – Rubro-Negra

<div align="center">
    Figura 5: Fase 1-Inserção e recoloração na árvore Rubro-Negra
    <br>
    <img src="https://github.com/EDAII/Arvores_Alianca_Rebelde/blob/main/screenshots/missao1-fase1-arvores.png?raw=true" width="500">
    <br><br>
</div>

<div align="center">
    Figura 6: Fase 2- Conflitos de cor
    <br>
    <img src="https://github.com/EDAII/Arvores_Alianca_Rebelde/blob/main/screenshots/missao1-fase2-arvores.png?raw=true" width="500">
    <br><br>
</div>

<div align="center">
    Figura 7: Fase 3-Rotações 
    <br>
    <img src="https://github.com/EDAII/Arvores_Alianca_Rebelde/blob/main/screenshots/missao1-fase3-arvores.png?raw=true" width="500">
    <br><br>
</div>

### Missão 2 – AVL

<div align="center">
    Figura 8: Fase 1
    <br>
    <img src="https://raw.githubusercontent.com/EDAII/Arvores_Alianca_Rebelde/refs/heads/main/screenshots/missao2-fase1-arvores.png" width="500">
    <br><br>
</div>

<div align="center">
    Figura 9: Dicas
    <br>
    <img src="https://raw.githubusercontent.com/EDAII/Arvores_Alianca_Rebelde/refs/heads/main/screenshots/missao2-fase2-arvores.png" width="500">
    <br><br>
</div>


<div align="center">
    Figura 8: Fase 2
    <br>
    <img src="https://raw.githubusercontent.com/EDAII/Arvores_Alianca_Rebelde/refs/heads/main/screenshots/missao2-fase3-arvores.png" width="500">
    <br><br>
</div>

<div align="center">
    Figura 8: Fase 3
    <br>
    <img src="https://raw.githubusercontent.com/EDAII/Arvores_Alianca_Rebelde/refs/heads/main/screenshots/missao2-fase4-arvores.png" width="500">
    <br><br>
</div>


<div align="center">
    Figura 8: Fase 4
    <br>
    <img src="https://raw.githubusercontent.com/EDAII/Arvores_Alianca_Rebelde/refs/heads/main/screenshots/missao2-fase5-arvores.png" width="500">
    <br><br>
</div>



## Instalação

### 1. Pré-requisitos

Antes de começar, certifique-se de que você tem os seguintes softwares instalados:
* **Python 3:** (versão 3.7 ou superior)
* **Git:** para clonar o repositório
* **Tkinter:** para a interface gráfica  
  - **Linux (Debian/Ubuntu):** `sudo apt-get update && sudo apt-get install python3-tk`  
  - **Windows/macOS:** já vem com o Python

---

### 2. Configuração do Jogo

1. **Clone o Repositório:**

```bash
git clone <git@github.com:EDAII/Algoritmos_Arvores_Alianca_Rebelde.git>
cd Algoritmos_Arvores_Alianca_Rebelde/JogoArvores
>>>>>>> da32dbe (Missao 1 -Arvore rubro negra)
