# Detecção de Tumores Cerebrais com Aprendizado de Máquina

Projeto Prático de Inteligência Artificial — IFMG Campus Ouro Branco (2026)
Bacharelado em Sistemas de Informação

## Descrição
Classificação de imagens de ressonância magnética em 4 categorias (glioma, meningioma,
notumor, pituitary) comparando MLP e SVM (scikit-learn) em 8 experimentos, sem uso de
redes convolucionais ou GPU.

## Dataset
[Brain Tumor MRI Dataset](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset)
— 7.200 imagens (5.600 treino / 1.600 teste, 1.800 por classe).

## Como rodar
\`\`\`bash
pip install -r requirements.txt
\`\`\`
Baixe o dataset do Kaggle e extraia em `data/Training` e `data/Testing`.
Depois abra `notebook/experimento_final.ipynb` e rode as células em ordem.

## Estrutura do projeto
\`\`\`
data/                          — dataset (nao versionado, ver .gitignore)
notebook/
  experimentos_final.ipynb     — notebook final, com os 8 experimentos
  historico-desenvolvimento/   — notebooks de debug/exploracao (processo de desenvolvimento)
results/
  resultados_experimentos.csv
  figuras/
relatorio/
  Relatorio_Projeto_IA.docx
\`\`\`

## Resultados
Melhor experimento: Exp7 (SVM, kernel RBF, C=100) — Acurácia 88,19%, F1-Score 87,98%.
Detalhes completos em `relatorio/Relatorio_Projeto_IA.docx`.

## Autor
Victor Caetano — Sistemas de Informação — IA