# -*- coding: utf-8 -*-
"""FluxoDeTrabalho.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19NS6grsbQ2WOlNOInHtyREyG0MR5wmyX

# Fluxo de Trabalho
Esqueleto sugerido para o processo de análise de dados.

Observação:   
Esse modelo é uma base, e algumas etapas podem não ser aplicáveis a sua análise em específico. Considerando isso avalie bem quais processos são necessários e compatíveis com o seu caso.

Como usar:   
Você pode criar uma cópia deste arquivo e usar essa cópia para seguir o passo a passo de desenvolvimento no seu projeto, ou simplesmente usá-lo como um direcionamento mental para se guiar no seu projeto pessoal.

# Autor
Jonathas Carneiro

# ETL
Extração, transformação, carregamento e possível automação do processo de etl dos dados.

## Install e Libs
Instalações e importações das bibliotecas necessárias para o processo de ETL.
"""



"""## Extraction
A primeira etapa da ETL é a extração dos dados de sua fonte original. Dependendo do tipo de dados e da fonte, você pode precisar de diferentes ferramentas e técnicas para extrair os dados.
"""



"""## Transformation
Aqui os dados extraídos precisam ser transformados em um formato adequado para análise, e para isso deve seguir alguns passos, que podem precisar serem repetidos ao longo do processo de análise.

### Limpeza de Dados
Remover dados duplicados, corrigir erros de digitação, tratar dados inconsistentes etc.
"""



"""### Normalização de Dados
Colocar os dados em um formato padronizado para facilitar a análise.
"""



"""### Criação de Variáveis
Criar novas variáveis com base nos dados originais para permitir uma análise mais detalhada e avançada.
"""



"""## Load
Depois que os dados são extraídos e transformados adequadamente, eles estarão prontos para as análise, mas antes disso eles precisam ser carregados em um local de armazenamento adequado. Podendo ser um banco de dados SQL ou NoSQL, um sistema de armazenamento em nuvem, e para o caso de disponibilizar o projeto publicamente é ideal que ele seja colocar em uma pasta de datasets, diferenciando o arquivo bruto e o tratado.
"""



"""## Automação ETL
Caso seja necessário atualização dos dados, é importante também automatizar o processo de ETL para que ele possa ser repetido facilmente. Para isso você pode utilizar ferramentas de automação de fluxo de trabalho como o Apache Airflow ou mesmo scripts no shell que execute o ETL em intervalos definidos.
"""



"""# EDA
Análise exploratória de dados. É importante saber com clareza o conjunto de dados que será utilizado e ter definido qual objetivos e perguntas a serem respondidas com a análise.
No processo de cada etapa da análise exploratório é importante fazer:
- Descrição de dados: identificação dos tipos de variáveis, dimensões dos dados, valores extremos e estatísticas descritivas.
- Visualização dos dados: criação de gráficos, tabelas e outros tipos de visualização para entender a distribuição e a relação entre as variáveis.
- Identificação de padrões: identificação de padrões, tendências, correlações e outras relações entre as variáveis.
- Testes estatísticos: aplicação de testes estatísticos para confirmar ou refutar hipóteses sobre os dados.

## Install e Libs
Instalações e bibliotecas necessárias para a análise de dados que não haviam sido importadas anteriormente.
"""



"""## Preparação do Dados
Novo processo de transformação de dados caso seja necessário fazer algo a mais para as análises a serem feitas.
"""



"""## Análise Descritiva
- Estatísticas descritivas do conjunto de dados;
- Distribuição das variáveis numéricas e categóricas;
- Identificação de outliers e tratamento, se necessário
"""



"""## Análise de Correlação
- Identificação de correlação entre as variáveis;
- Verificação de multicolinearidade;
- Visualização de gráficos de correlação, como heatmap e pairplot
"""



"""## Análise de Grupos
- Identificação de grupos no conjunto de dados;
- Visualização de gráficos de dispersão e boxplot para cada grupo
"""



"""## Análise Temporal
- Verificação de tendências temporais;
- Visualização de gráficos de linha, barras e scatterplot para cada período de tempo

"""



"""## Análise Geoespacial (se aplicável)
- Verificação de padrões geoespaciais;
- Visualização de mapas e gráficos de pontos para cada localização
"""



"""## Conclusão da EDA
Resumo das principais conclusões e insights obtidos a partir da análise exploratória, sugestões para próximos passos da análise ou possíveis ações a serem tomadas.

# Modelagem e Predição de Dados
É preciso ter em mente qual objetivo e qual problema será abordado na modelagem e predição, é importante explicar o modelo escolhido para abordar o problema e a métrica escolhida para avaliar o desempenho do modelo.

## Install e Libs
Instalações e bibliotecas necessárias para a análise de dados que não haviam sido importadas anteriormente.
"""



"""## Preparação do Dados
Novo processo de transformação de dados caso seja necessário fazer algo a mais para a modelagem e predições a serem feitas, além de dividir os dados em conjuntos de treino e conjunto de testes.
"""



"""## Modelagem
- Escolher o modelo a ser utilizado;
- Treiná-lo com o conjunto de treino;
- Validá-lo com o conjunto de testes;
- Caso preciso otimizar os hiperparâmetros do modelo
"""



"""## Avaliação do Modelo
- Avaliação do desempenho do modelo com a métrica escolhida;
- Análise de viés e variância do modelo;
- Análise da importância das variáveis no modelo
"""



"""## Predição
Utilização do modelo treinado para fazer predição de novos dados.
- Análise e interpretação dos resultados da predição.
"""



"""## Conclusão da Modelagem e Predição de Dados
Resumo das principais conclusões e insights obtidos. Assim como sugestões para próximos passos, como ajustes no modelo, coleta de mais dados ou ações a serem tomadas com base nas predições realizadas.
"""