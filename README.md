# Projeto: Privacidade em Jogo - Projeto Extensionista Mackenzie

## Desenvolvido por: João Pedro Queiroz de Andrade

[Importante: Como Tornar o Projeto Executável](#como-tornar-o-projeto-executável)

# Introdução 
O interesse na utilização de Inteligência Artificial em grandes empresas tem aumentado expressivamente nos últimos anos. Portanto, é fato que a utilização desse tipo de tecnologia será amplamente aproveitada de diversas formas. No entanto, a partir de uma breve análise sobre a forma em que as grandes empresas se portam em relação a problemas de integridade e segurança das pessoas, podendo ser utilizado como exemplo a explosão da plataforma Deepwater Horizon em 2010 causada por negligência e pressão por redução de custos, é possível observar que a ideia antiquada de Milton Friedman que apresenta que o único objetivo de uma empresa é gerar lucro para seus acionistas ainda é uma realidade nos dias de hoje.
Tendo isso em mente, esse crescimento na utilização da IA também não escaparia de problemas de integridade e segurança, nesse caso de dados pessoais. Atualmente, diversas empresas utilizam das IAs para a manipulação e análise de dados de usuários de seus produtos para personalização da experiência do usuário, otimização de processos e melhoria no atendimento ao cliente, no entanto, isso levanta questões cruciais quanto a segurança, privacidade e ética.
A partir dessas questões a Lei Geral de Proteção de Dados surgiu, tendo como seu principal objetivo garantir que o tratamento de dados pessoais de pessoa natural ou jurídica esteja de acordo com os direitos fundamentais de liberdade e de privacidade e o livre desenvolvimento da personalidade da pessoa natural (BRASIL,2018). 

# Descrição e Objetivo do Projeto
O projeto Privacidade em Jogo - Projeto Extensionista Mackenzie consiste em um simulador de decisões desenvolvido em python utilizando a biblioteca PyGame-CE, baseando-se no tema IA e a conformidade com a LGPD/GDPR. O jogador é o novo Encarregado de Proteção de Dados da Agência Quântica, uma empresa de marketing digital que utiliza inteligência artificial para analisar o comportamento de consumidores e prever tendências, então o jogador deve tomar diversas decisões em relação as ações irresponsáveis do último Encarregado que estava em sua posição anteriormente.
O principal objetivo do projeto é apresentar situações reais e como as ações tomadas pela empresa em relação a essas situações podem afetar a confiança, segurança e privacidade das pessoas que se relacionam a essa empresa e quão prejudicial isso pode ser até mesmo para a própria empresa.

# Implementação Técnica

O simulador de decisões foi desenvolvido em **Python** utilizando a biblioteca **PyGame** [6], que fornece as ferramentas necessárias para a criação de jogos e aplicações multimídia. A estrutura do código é orientada a estados, gerenciando a transição entre as telas de **Menu**, **História**, **Jogo** (Decisões) e **Final**.

## Estrutura e Componentes Visuais

O jogo opera em uma tela de 500x800 pixels, e a interface é construída a partir do carregamento e manipulação de diversas imagens que representam os estados do jogo.

| Componente | Arquivo de Imagem (Exemplo) | Função no Jogo |
| :--- | :--- | :--- |
| **Fundo do Menu** | `Images\menubackground.png` | Tela inicial e de fundo padrão. |
| **Botões** | `Images\start.png`, `Images\opt1.png` | Botão de início e botões de opção para as decisões. |
| **Personagem** | `Images\player.png`, `Images\player2.png` | Representação visual do Encarregado de Proteção de Dados, com animação simples. |
| **História** | `Images\story1.png`, `Images\story2.png` | Telas estáticas que apresentam o contexto e a narrativa inicial. |
| **Decisões** | `Images\game1.png` a `Images\game10.png` | Telas que apresentam os 10 cenários de decisão relacionados à LGPD/GDPR. |
| **Finais** | `Images\guardiao.png` a `Images\vazador.png` | Telas que exibem o resultado final do jogador com base na pontuação. |

Todas as imagens são carregadas e redimensionadas programaticamente para se ajustarem à tela e manterem a proporção visual, como visto nas linhas 5 a 103 do código.

## Lógica de Jogo e Pontuação

O jogo é dividido em três estados principais, controlados pelas variáveis booleanas `menu`, `story`, `play` e `finalScreen`.

1.  **Menu:** Exibe o botão "Start". Ao clicar, o estado transiciona para a História.
2.  **História:** Exibe as telas de `stories` (`story1`, `story2`). O jogador avança na história clicando no botão "Continuar" (`continueRect`).
3.  **Jogo (Decisões):** O estado principal do simulador. O jogo itera sobre a lista de `decisions` (10 cenários). Para cada cenário, o jogador tem três opções de resposta, representadas pelos retângulos de colisão `optaRectangle`, `optbRectangle` e `optcRectangle`.

A **pontuação** (`score`) do jogador é atualizada com base na opção escolhida, simulando o impacto de cada decisão na conformidade e segurança de dados da empresa:

| Opção | Pontuação Adicionada | Implicação |
| :--- | :--- | :--- |
| **Opção A** (`optaRectangle`) | +10 pontos | Decisão mais favorável à conformidade e privacidade. |
| **Opção B** (`optbRectangle`) | +5 pontos | Decisão intermediária ou de risco moderado. |
| **Opção C** (`optcRectangle`) | -10 pontos | Decisão desfavorável ou de alto risco à conformidade e privacidade. |

## Resultados e Finais

Após passar pelos 10 cenários de decisão (`gameIndex` > 9), o jogo transiciona para a tela final, onde o resultado é determinado pela pontuação total acumulada. Existem cinco finais possíveis, cada um associado a uma imagem e um título que reflete o perfil do Encarregado de Proteção de Dados (DPO) que o jogador se tornou:

| Pontuação (`score`) | Final | Imagem | Perfil do DPO |
| :--- | :--- | :--- | :--- |
| **≥ 90** | `final1` | `Images\guardiao.png` | **Guardião** (Excelência em conformidade) |
| **≥ 70** | `final2` | `Images\gestor.png` | **Gestor** (Bom gerenciamento de riscos) |
| **≥ 50** | `final3` | `Images\descuidado.png` | **Descuidado** (Risco moderado) |
| **≥ 30** | `final4` | `Images\risco.png` | **Risco** (Alto risco de não conformidade) |
| **< 30** | `final5` | `Images\vazador.png` | **Vazador** (Não conformidade grave) |

Essa mecânica de pontuação e finais permite que o projeto atinja seu objetivo de forma lúdica, ilustrando as consequências diretas das decisões do DPO no contexto da LGPD/GDPR.

## Como Tornar o Projeto Executável

O projeto utiliza a ferramenta **cx_Freeze** para criar um executável autônomo (standalone), que pode ser distribuído e executado em sistemas operacionais sem a necessidade de ter o Python ou o PyGame instalados.

### Pré-requisitos

Para gerar o executável, você precisará ter o Python instalado em seu sistema e o pacote `cx_Freeze`.

1.  **Instalar `cx_Freeze`:**
    ```bash
    pip install cx_Freeze
    ```

### Geração do Executável

Com o `setup.py` e o script principal (`lgpd.py`) no mesmo diretório, execute o seguinte comando no terminal:

```bash
python setup.py build
```

Este comando irá:
1.  Compilar o script principal (`lgpd.py`).
2.  Incluir a biblioteca `pygame` e todos os arquivos da pasta `Images` no pacote.
3.  Criar uma pasta chamada `build` no diretório do projeto.

### Execução do Jogo

Após a conclusão do processo de `build`, o executável estará disponível dentro da pasta `build`.

-   **No Windows:** O executável estará em `build\exe.win-amd64-3.x\lgpd.exe` (o nome exato da pasta pode variar dependendo da sua versão do Python e arquitetura).
-   **No Linux/macOS:** O executável estará em um caminho similar, como `build/exe.linux-x86_64-3.x/lgpd`.

Basta navegar até o diretório apropriado e executar o arquivo gerado.

## Estrutura do Projeto

O projeto depende da seguinte estrutura de arquivos:

-   `lgpd.py`: O script principal do jogo (baseado no código Python fornecido anteriormente).
-   `setup.py`: Arquivo de configuração para a criação do executável com `cx_Freeze`.
-   `Images/`: Pasta contendo todas as imagens e assets do jogo (fundo, botões, personagens, telas de história e decisão).
-   `README.md`: Este arquivo.

# Bibliografia
BRASIL. Lei n° 13.709, de 14 de agosto de 2018. Dispõe sobre a proteção de dados pessoais e altera a Lei n° 12.965, de 23 de abril de 2014 (Marco Civil da Internet). Diário Oficial da União: seção 1, Brasília, DF, ano 155, n. 157, p. 59-64, 15 ago. 2018. Disponível em: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm. Acesso em: 11 out. 2025.

LUCROS devem deixar de ser principal objetivo das empresas. Dinheiro Vivo, 14 abr. 2024. Disponível em: https://dinheirovivo.dn.pt/lucros-devem-deixar-de-ser-principal-objetivo-das-empresas. Acesso em: 11 out. 2025.

O GLOBO. Funcionário da BP diz que houve negligência da petroleira porque plataforma apresentou defeito. O Globo, Rio de Janeiro, 21 jun. 2010. Atualizado em: 4 nov. 2011. Disponível em: https://oglobo.globo.com/saude/ciencia/funcionario-da-bp-diz-que-houve-negligencia-da-petroleira-porque-plataforma-apresentou-defeito-2990823. Acesso em: 11 out. 2025.

RAMOS, Marien. Uso de inteligência artificial aumenta e alcança 72% das empresas, diz pesquisa. CNN Brasil, 8 jun. 2024. Disponível em: https://www.cnnbrasil.com.br/economia/negocios/uso-de-inteligencia-artificial-aumenta-e-alcanca-72-das-empresas-diz-pesquisa/#goog_rewarded. Acesso em: 11 out. 2025.

ECKSCHMIDT, Thomas. O único propósito de uma empresa é gerar lucro para os acionistas? MIT Sloan Review Brasil, 30 set. 2020. Disponível em: https://mitsloanreview.com.br/o-unico-proposito-de-uma-empresa-e-gerar-lucro-para-os-acionistas/. Acesso em: 10 out. 2025.

PYGAME. **Documentação oficial do Pygame**. Disponível em: https://www.pygame.org/docs/. Acesso em: 10 out. 2025.
