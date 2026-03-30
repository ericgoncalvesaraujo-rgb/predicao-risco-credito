# Credit Score Model

## Descrição

Este projeto apresenta o desenvolvimento de um **modelo de score de crédito** utilizando técnicas de **Machine Learning** para prever a probabilidade de inadimplência de clientes a partir de dados históricos de empréstimos.

Modelos de credit score são amplamente utilizados no setor financeiro para **gestão de risco, aprovação de crédito, definição de taxas de juros e controle de inadimplência**.

O objetivo deste projeto é identificar **padrões financeiros e comportamentais** que indiquem maior ou menor risco de crédito, utilizando técnicas modernas de ciência de dados e aprendizado de máquina.

O projeto inclui **análise exploratória de dados, engenharia de variáveis, treinamento de múltiplos modelos, otimização de hiperparâmetros e interpretabilidade do modelo**.

---

## Objetivo

O objetivo principal deste projeto é construir um modelo capaz de **prever a probabilidade de inadimplência de clientes** com base em características financeiras e históricas presentes no dataset.

Além disso, o projeto busca:

* Identificar **variáveis relevantes para risco de crédito**
* Aplicar **técnicas de feature engineering**
* Comparar diferentes **algoritmos de Machine Learning**
* Interpretar o comportamento do modelo utilizando **Explainable AI**

---

## Dataset

O modelo foi desenvolvido utilizando uma base de dados de empréstimos utilizada em problemas de **Credit Risk Modeling**.

Essa base contém informações financeiras e comportamentais dos clientes, permitindo identificar padrões associados ao risco de inadimplência.

Entre as variáveis presentes no dataset estão:

* valor do empréstimo
* taxa de juros
* renda do cliente
* histórico de crédito
* número de contas abertas
* saldo rotativo de crédito
* relações de dívida
* data de emissão do empréstimo
* status de pagamento

Essas informações permitem analisar o comportamento financeiro dos clientes e identificar fatores relacionados ao **risco de crédito**.

---

## Pipeline do Projeto

O desenvolvimento do modelo seguiu uma estrutura comum em projetos de ciência de dados.

### Análise Exploratória de Dados (EDA)

Inicialmente foi realizada uma **análise exploratória de dados** para compreender melhor a estrutura do dataset.

Durante essa etapa foram analisados:

* distribuição das variáveis
* padrões nos dados
* presença de valores ausentes
* relações entre variáveis

Essa análise é fundamental para orientar decisões de pré-processamento e engenharia de variáveis.

---

### Limpeza e Pré-processamento

Após a análise inicial foi realizada a etapa de preparação dos dados.

As principais etapas incluíram:

* tratamento de valores ausentes
* conversão de variáveis de data
* organização e padronização dos dados

Esse processo garante que os dados estejam adequados para o treinamento dos modelos de machine learning.

---

### Feature Engineering

Para melhorar a capacidade preditiva do modelo, foram criadas **novas variáveis derivadas dos dados originais**.

Entre as transformações realizadas estão:

* criação de **razões financeiras entre variáveis**
* agrupamento de **taxas de juros**
* transformações temporais da **data de emissão do empréstimo**
* criação de métricas baseadas em **saldo de crédito e número de contas**

Essas variáveis ajudam o modelo a capturar **relações ocultas entre comportamento financeiro e risco de inadimplência**.

---

### Encoding de Variáveis Categóricas

Para lidar com variáveis categóricas foi utilizada a técnica de:

**Target Encoding**

Essa abordagem substitui categorias pela média da variável alvo associada àquela categoria, sendo especialmente eficiente para variáveis com **muitas categorias**.

---

### Escalonamento de Variáveis

Alguns algoritmos exigem que as variáveis estejam em escala semelhante.

Para isso foi utilizado:

`StandardScaler`

Esse processo garante melhor desempenho para modelos sensíveis à escala dos dados.

---

## Modelos Utilizados

Durante o desenvolvimento foram testados diversos algoritmos de Machine Learning.

Os principais modelos utilizados foram:

* Logistic Regression
* K-Nearest Neighbors (KNN)
* Random Forest
* XGBoost
* LightGBM

A comparação entre diferentes modelos permite identificar aquele com **melhor desempenho e capacidade de generalização**.

---

## Otimização de Hiperparâmetros

Para melhorar o desempenho dos modelos foi utilizada a técnica de:

`HalvingRandomSearchCV`

Esse método permite realizar uma busca eficiente por hiperparâmetros, concentrando recursos nas configurações mais promissoras.

Essa abordagem é especialmente útil em datasets grandes.

---

## Avaliação do Modelo

Os modelos foram avaliados utilizando diversas métricas importantes para problemas de classificação e risco de crédito.

Entre elas:

* ROC-AUC
* Precision
* Recall
* F1 Score
* Average Precision
* Confusion Matrix

Essas métricas permitem avaliar o desempenho do modelo sob diferentes perspectivas, especialmente a capacidade de distinguir **bons pagadores de inadimplentes**.

---

## Interpretabilidade do Modelo

Para entender como o modelo toma decisões foi utilizada a biblioteca:

**SHAP (SHapley Additive Explanations)**

O SHAP permite analisar o impacto de cada variável nas previsões do modelo.

Entre as visualizações utilizadas estão:

* SHAP Summary Plot
* SHAP Force Plot
* SHAP Waterfall Plot

A interpretabilidade é fundamental em modelos financeiros, pois decisões de crédito precisam ser **transparentes e justificáveis**.

---

## Habilidades Demonstradas

Este projeto demonstra diversas habilidades importantes em ciência de dados:

* análise exploratória de dados (EDA)
* engenharia de features
* pré-processamento de dados
* modelagem de machine learning
* otimização de hiperparâmetros
* avaliação de modelos
* interpretabilidade de modelos
* visualização de dados
* construção de pipelines de modelagem

---

## Instalação

Para executar o projeto é necessário instalar as seguintes bibliotecas:

```bash
pip install pandas
pip install numpy
pip install matplotlib
pip install seaborn
pip install shap
pip install scikit-learn
pip install xgboost
pip install lightgbm
pip install plotly
pip install category-encoders
```

---

## Bibliotecas Utilizadas

* pandas
* numpy
* matplotlib
* seaborn
* shap
* scikit-learn
* xgboost
* lightgbm
* plotly
* category-encoders

---

## Autor

Erick Gonçalves
Estudante de Ciência de Dados

