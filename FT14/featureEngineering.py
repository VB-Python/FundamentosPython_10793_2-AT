import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
import pylab as plt

# Vamos agora exercitar algumas tarefas comuns na atividade de *Feature Engineering*,
# que consiste em remodelar atributos para obter melhor(?) desempenho nos algoritmos.
# Entre as tarefas faremos conversão de categorias usando OHE (*one-hot-encoding*) e *Feature Hashing*,
# e também a produção de novas colunas calculadas com base noutras.
# Não há uma "receita" para essas atividades. É sempre uma questão de experimentar e ver quais os modelos mque são melhores que outros.

##Recarregando os dados pda parte anetrior 
df_train = pd.read_csv("train_no_nulls_no_outliers.csv")
df_train.head(2)

novas_colunas = pd.get_dummies(df_train["Embarked"])
df_train2 = pd.concat([df_train,novas_colunas], axis=1)
print(df_train2.head(3))

novas_colunas_pclass = pd.get_dummies(df_train["Pclass"])
novas_colunas_sex = pd.get_dummies(df_train["Sex"])

df_train3 = pd.concat([df_train2, novas_colunas_pclass, novas_colunas_sex], axis=1)
df_train3.drop(["Pclass", "Sex"], axis=1, inplace=True)
print(df_train3.head(3))

df_train3.to_csv("train_no_nulls_no_outliers_ohe.csv", index=False)

df_train = pd.read_csv("train_no_nulls_no_outliers.csv")
df_train.head(2)




