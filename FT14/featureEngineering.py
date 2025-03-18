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

##Recarregando os dados pda parte anterior...

df_train = pd.read_csv("train_no_nulls_no_outliers.csv")
df_train.head(2)

# A técnica de One-hot-encoding é utilizada para converter dados que são categóricos em numéricos de forma
# a não infloenciar de forma negativa alguns algotitmos.
# Converter cada valor possível para a coluna em numeros de 1 a N implicaria haver uma relaçãofixa de
# distância geométrica entre os dados, o que normalmente não ocorre.
# A conversão funciona de forma simples: para cada categoria numa determinada coluna, é criada uma nova coluna onde o valor será 1
# quando a linha tiver aquele valor para a categoria ou 0 caso contrário.
# O código abaixo usa o método get_dummies da biblioteca pandas para criar 3 novas colunas para cada
# um dos 3 valores possíveis para a coluna 'Embarked'.

novas_colunas = pd.get_dummies(df_train["Embarked"])
df_train2 = pd.concat([df_train,novas_colunas], axis=1) # axis = 1 concatena colunas, axis = 0 concatena linhas
print(df_train2.head(3))

#Agora podemos remover a colunaoriginal dos dados

df_train2.drop('Embarked', axis=1, inplace=True)

novas_colunas_pclass = pd.get_dummies(df_train["Pclass"])
novas_colunas_sex = pd.get_dummies(df_train["Sex"])

df_train3 = pd.concat([df_train2, novas_colunas_pclass, novas_colunas_sex], axis=1)
df_train3.drop(["Pclass", "Sex"], axis=1, inplace=True)
print(df_train3.head(3))

df_train3.to_csv("train_no_nulls_no_outliers_ohe.csv", index=False)

df_train = pd.read_csv("train_no_nulls_no_outliers.csv")
df_train.head(2)




