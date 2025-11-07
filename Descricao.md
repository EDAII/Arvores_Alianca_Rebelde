# Star Wars: Aliança Rebelde – Floresta de Dados

### Em tempos de guerra, informação é poder. A Rebelião enfrenta um novo desafio: armazenar e acessar dados estratégicos sem deixar rastros para o Império.  
Você, como **Engenheiro(a) de Estruturas da Rebelião**, deve garantir que as bases de dados se mantenham organizadas, balanceadas e seguras — mesmo sob ataques cibernéticos imperiais.

### Cada missão do jogo é uma simulação prática de como as **árvores de busca balanceadas** mantêm o acesso rápido e estável a dados críticos, com uma narrativa imersiva inspirada no universo Star Wars.  
Equilibrar é sobreviver.

## EQUILIBRAR PARA RESISTIR!

## Descrição do Jogo

**"Aliança Rebelde – Floresta de Dados"** é um jogo de puzzle e simulação em que o jogador atua como um(a) **Analista de Estruturas da Rebelião**.  
A missão é projetar, balancear e proteger bancos de dados secretos utilizando **estruturas de árvores balanceadas** — Rubro-Negra e AVL — aplicadas em contextos de guerra informacional.

Cada fase demonstra, de forma visual e interativa, como os algoritmos de balanceamento garantem **eficiência e estabilidade**, mesmo com inserções e remoções constantes.  
O jogo combina **narrativa sci-fi**, **conceitos teóricos de Estruturas de Dados 2** e **simulação educacional**, tornando o aprendizado mais intuitivo e envolvente.

---

## Público-Alvo

- Estudantes da disciplina de **Estrutura de Dados 2**  
- Curiosos e entusiastas da **lógica computacional**  
- Fãs do universo **Star Wars** interessados em aprender de forma lúdica

---

## Objetivos do Jogo

- **Para o Jogador:** Garantir o equilíbrio das estruturas de dados, aplicando corretamente as rotações e recolorações para manter o desempenho ideal da Rebelião.  
- **Educacional:** Compreender o funcionamento prático das árvores balanceadas — suas propriedades, inserções, rotações e fatores de equilíbrio — e como elas otimizam buscas, inserções e exclusões.

---

## Estrutura do Projeto

O jogo é composto por duas missões principais, cada uma abordando uma estrutura de árvore balanceada:

- [JogoArvores](https://github.com/EDAII/Algoritmos_Arvores_Alianca_Rebelde/tree/main/JogoArvores)  
  Contém os minigames e interfaces gráficas que representam as missões interativas.

- [Arvores](https://github.com/EDAII/Algoritmos_Arvores_Alianca_Rebelde/tree/main/Arvores)  
  Contém as implementações dos algoritmos e operações das árvores Rubro-Negra e AVL.

---

## Missões do Jogo (Desafios de Árvores) em JogoArvores

### MISSÃO 1: Sentinelas de Scarif  
#### Estrutura: Árvore Rubro-Negra

- **Contexto:**  
  A base de Scarif está em alerta. Códigos de agentes rebeldes são interceptados e precisam ser inseridos rapidamente em uma estrutura segura.  
  Uma falha na ordem dos registros pode revelar a identidade dos espiões da Rebelião.  
  Para garantir que os acessos sejam rápidos e estáveis, você deve utilizar uma **Árvore Rubro-Negra**, capaz de manter o equilíbrio a cada inserção.

- **Descrição:**  
  A missão consiste em inserir registros na árvore, observando as etapas de recoloração e rotação:  
  - Inserir nós como vermelhos  
  - Detectar violações das propriedades da árvore  
  - Recolorir e aplicar rotações simples ou duplas conforme necessário  

- **Conceitos Aprendidos:**  
  - Regras de coloração (nó vermelho/preto)  
  - Estrutura e propriedades da árvore Rubro-Negra  
  - Como a árvore mantém a altura balanceada (O(log n))  
  - A importância da rotação e recoloração para eficiência e estabilidade  

- **Analogias no Jogo:**  
  Cada **recoloração** representa um ajuste tático na comunicação rebelde,  
  e cada **rotação** simboliza uma manobra estratégica para manter o equilíbrio entre segurança e velocidade de resposta.

---

### MISSÃO 2: Santuário de Endor  
#### Estrutura: Árvore AVL

- **Contexto:**  
  Na lua florestal de Endor, a Rebelião construiu uma base secreta.  
  Nela, um grande banco de dados de recursos — combustível, armamentos e esquadrões — precisa estar sempre balanceado.  
  Inserções desordenadas tornam o acesso lento e vulnerável, comprometendo as defesas da base.  
  Sua tarefa é aplicar o algoritmo da **Árvore AVL** para garantir o equilíbrio constante.

- **Descrição:**  
  A missão consiste em inserir e remover elementos, observando o **fator de balanceamento** e aplicando as rotações apropriadas:
  - Calcular o fator de balanceamento (altura esquerda – altura direita)  
  - Identificar quando ocorre um desbalanceamento (±2)  
  - Aplicar rotações simples (direita ou esquerda) e duplas (direita-esquerda ou esquerda-direita)  

- **Conceitos Aprendidos:**  
  - Cálculo do fator de balanceamento  
  - Detecção de desbalanceamento  
  - Aplicação das rotações e manutenção da altura logarítmica  
  - Diferença entre a AVL (equilíbrio rigoroso) e a Rubro-Negra (equilíbrio por cor)

- **Analogias no Jogo:**  
  Cada **rotação** simboliza uma reorganização da frota rebelde, e o **fator de balanceamento** representa a estabilidade do comando.  
  Quando a árvore se equilibra, a base atinge o estado ideal — pronta para resistir a qualquer ofensiva imperial.

---

## Dados Utilizados

Para a simulação das missões, foram utilizados subconjuntos da base **The Star Wars Dataverse** (Kaggle), incluindo:
- Personagens (nomes, espécies, ano de nascimento)  
- Naves (modelo, fabricante e comprimento)  
- Planetas (população e clima)  

Esses dados foram transformados em **chaves de inserção** (inteiros ou strings) usadas para demonstrar, visualmente, o balanceamento das árvores.

---

## Importante!

O jogo possui **duas pastas executáveis**, cada uma com seu próprio arquivo `main.py`:

- **JogoArvores:** interface visual e narrativa do jogo.  
- **Arvores:** algoritmos e operações das estruturas (inserção, busca, rotação, recoloração, etc).

Ambas as partes se conectam para representar, de forma visual, como as árvores se mantêm balanceadas e eficientes.

---

## Conclusão

Em “**Star Wars: Aliança Rebelde – Floresta de Dados**”, equilibrar não é apenas um requisito técnico — é uma questão de sobrevivência.  
O domínio das **árvores Rubro-Negra e AVL** representa o controle e a resistência da Rebelião diante do caos do Império.

Assim como as forças rebeldes, as estruturas de dados devem se adaptar, reorganizar e permanecer firmes —  
pois na galáxia dos algoritmos, **a ordem é a chave da vitória**.

---

