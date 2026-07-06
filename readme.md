# Detecção de Tumores Cerebrais com Aprendizado de Máquina

Projeto Prático de Inteligência Artificial — IFMG Campus Ouro Branco
Bacharelado em Sistemas de Informação — 2026

## Descrição

Este projeto tem como objetivo classificar imagens de ressonância magnética cerebral em quatro categorias:

* glioma
* meningioma
* notumor
* pituitary

Foram comparados modelos clássicos de Aprendizado de Máquina, utilizando `scikit-learn`, com foco em MLP e SVM. Ao todo, foram realizados 8 experimentos, variando técnicas de pré-processamento, extração de características e configuração dos modelos.

O projeto não utiliza redes neurais convolucionais, GPU ou bibliotecas de Deep Learning, seguindo a proposta de aplicar modelos tradicionais de Inteligência Artificial para classificação de imagens.

## Dataset

O dataset utilizado foi o [Brain Tumor MRI Dataset](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset), composto por imagens de ressonância magnética cerebral separadas em quatro classes.

No projeto, o dataset foi organizado da seguinte forma:

* `data/Training` — imagens de treinamento
* `data/Testing` — imagens de teste

O conjunto utilizado nos experimentos contém 7.200 imagens, sendo 5.600 para treinamento e 1.600 para teste, com distribuição balanceada entre as classes.

## Tecnologias utilizadas

* Python
* NumPy
* Pandas
* Matplotlib
* Scikit-learn
* Jupyter Notebook

## Como executar o projeto

Primeiro, instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

Depois, baixe o dataset pelo Kaggle e extraia os arquivos dentro da pasta `data`, seguindo esta estrutura:

```bash
data/
  Training/
    glioma/
    meningioma/
    notumor/
    pituitary/
  Testing/
    glioma/
    meningioma/
    notumor/
    pituitary/
```

Em seguida, abra o notebook principal:

```bash
notebook/experimentos_final.ipynb
```

Execute as células em ordem para reproduzir o carregamento das imagens, o pré-processamento, o treinamento dos modelos e a avaliação dos experimentos.

## Estrutura do projeto

```bash
data/                          # Dataset utilizado no projeto (não versionado)
notebook/
  experimentos_final.ipynb     # Notebook principal com os 8 experimentos
  historico-desenvolvimento/   # Notebooks auxiliares de testes, debug e exploração

results/
  resultados_experimentos.csv  # Tabela com os resultados dos experimentos
  figuras/                     # Gráficos e imagens geradas durante a análise

relatorio/
  Relatorio_Projeto_IA.docx    # Relatório final do projeto
```

## Experimentos realizados

Foram realizados 8 experimentos comparando diferentes abordagens de classificação com MLP e SVM. As avaliações consideraram as seguintes métricas:

* Acurácia
* Precisão
* Recall
* F1-Score

Os experimentos permitiram comparar o desempenho dos modelos e identificar qual configuração apresentou o melhor resultado para o problema de classificação das imagens.

## Resultados

O melhor resultado foi obtido no experimento 7:

**Exp7 — SVM com kernel RBF e C=100**

Resultados principais:

* Acurácia: **88,19%**
* F1-Score: **87,98%**

Os resultados completos estão disponíveis no arquivo:

```bash
results/resultados_experimentos.csv
```

A análise detalhada dos experimentos, incluindo metodologia, discussão dos resultados e conclusão, está documentada em:

```bash
relatorio/Relatorio_Projeto_IA.docx
```

## Observações

A pasta `data` não está versionada no GitHub, pois contém o dataset completo. Para executar o projeto corretamente, é necessário baixar o dataset manualmente pelo Kaggle e organizar as pastas conforme indicado neste README.

## Autor

Victor Caetano
Bacharelado em Sistemas de Informação
IFMG Campus Ouro Branco
