import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
import pylab as plt

#Vamos agora carregar nossos dados já sem os nulos
df_train = pd.read_csv("train_no_nulls.csv")

#vamos agora exercitar a remoção de outliers. Vale ressaltar que os dados originais foram modificados
# para incluir ocorrências incomuns em alguns atributos.
#O primeiro passo para identificar outliers é ver uma breve descrição dos dados numéricos.

print(df_train.describe())

#As colunas que nos interessam são 'Age', 'SibSP', 'Parch' e 'Fare', poisas demais são categoricas po apenas o ID do passageiro.
# Observando as 4 colunas, podemos ver algumas coisas incomuns:
#* A menor tarifa é negativa (o que é provavelmente um erro) e a maior é um numero 10x maior que o Terceiro Quartil (75% percentil)
# Há alguém com idade 133 anos. Hoje já parece improvável. Deve tratar-se também de um outlier (ou erro).
# A discussão sobre outliers é subjectiva. Sem o conhecimento de domínio do problema (como fizemos com a idade), é muito dificil dizer o que é um outlier.
# Mas para fins didáticos, vamos tratar aqui as anomalias como erros nos dados e vamos removê-los trocando pelo valor médio.
# #Primeiro, vamos mostrar os 5 maiores e os 5 menores idades.

print(df_train.sort_values("Age", ascending=False).head(5)["Age"])
print(df_train.sort_values("Age", ascending=True).head(5)["Age"])

#No caso da coluna idadae, podemos notar que o valor 133 parece fora da normalidade.
#Vamos trocá-lo pelo valor médio das idades, que já calculamos na limpesaNulos.py.

media_idade = df_train["Age"].mean()
df_train.loc[df_train["Age"]==133, "Age"] = media_idade ## Aqui substituimos os valores de idade iguais a 133 pela média

#Agora vamos fazer o mesmo para o campo tarifa
print(df_train.sort_values("Fare", ascending=False).head(5)["Fare"])
print(df_train.sort_values("Fare", ascending=True).head(5)["Fare"])

#Aqui confirmamos o valor negativo e um valor 10x do bilhete mais caro para o segundo mais caro.
# Vamos tratá-los como erros e atualizá-los com o valor da mediana da tarifa.
# Usaremos a mediana em vez de médi, pois ela é menos sensível aos outliers.

mediana_tarifa = df_train["Fare"].median()
df_train.loc[df_train["Fare"]>5000, "Fare"] = mediana_tarifa
df_train.loc[df_train["Fare"]<0, "Fare"] = mediana_tarifa

#vamos conferir a remoção de outliers

print(df_train.sort_values("Fare", ascending=False).head(5)["Fare"])
print(df_train.sort_values("Fare", ascending=True).head(5)["Fare"])

#vamos agora guerdar os nossos dados

df_train.to_csv("train_no_nulls_no_outliers.csv", index=False)