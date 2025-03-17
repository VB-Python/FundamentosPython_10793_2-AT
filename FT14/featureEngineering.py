import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
import pylab as plt

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




