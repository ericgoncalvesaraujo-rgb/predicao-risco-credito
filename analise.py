# loan_amnt = valor do empréstimo
# 
# term = prazo do empréstimo 
# 
# int_rate = taxa de juros
# 
# nstallment	= valor da parcela
# 
# grade	= classificação de risco
# 
# sub_grade	= sub-classificação de risco
# 
# emp_title	= cargo / profissão
# 
# emp_length	= tempo de emprego
# 
# home_ownership	= tipo de moradia
# 
# annual_inc	= renda anual
# 
# verification_status	= status de verificação da renda
# 
# issue_d	= data de emissão do empréstimo
# 
# loan_status	= status do empréstimo
# 
# purpose	= finalidade do empréstimo
# 
# title	= título / descrição do empréstimo
# 
# dti	= relação dívida-renda
# 
# earliest_cr_line	= primeira linha de crédito
# 
# open_acc	= contas de crédito abertas
# 
# pub_rec	= registros públicos negativos
# 
# revol_bal	= saldo de crédito rotativo
# 
# revol_util	= utilização do crédito rotativo
# 
# total_acc	= total de contas de crédito
# 
# initial_list_status	= status inicial de listagem
# 
# application_type	= tipo de aplicação
# 
# mort_acc	= contas de hipoteca
# 
# pub_rec_bankruptcies	= registros de falência
# 
# address	= endereço

# %% [markdown]
# loan_amnt = valor do empréstimo
# 
# term = prazo do empréstimo 
# 
# int_rate = taxa de juros
# 
# nstallment	= valor da parcela
# 
# grade	= classificação de risco
# 
# sub_grade	= sub-classificação de risco
# 
# emp_title	= cargo / profissão
# 
# emp_length	= tempo de emprego
# 
# home_ownership	= tipo de moradia
# 
# annual_inc	= renda anual
# 
# verification_status	= status de verificação da renda
# 
# issue_d	= data de emissão do empréstimo
# 
# loan_status	= status do empréstimo
# 
# purpose	= finalidade do empréstimo
# 
# title	= título / descrição do empréstimo
# 
# dti	= relação dívida-renda
# 
# earliest_cr_line	= primeira linha de crédito
# 
# open_acc	= contas de crédito abertas
# 
# pub_rec	= registros públicos negativos
# 
# revol_bal	= saldo de crédito rotativo
# 
# revol_util	= utilização do crédito rotativo
# 
# total_acc	= total de contas de crédito
# 
# initial_list_status	= status inicial de listagem
# 
# application_type	= tipo de aplicação
# 
# mort_acc	= contas de hipoteca
# 
# pub_rec_bankruptcies	= registros de falência
# 
# address	= endereço
# ## Modelo de predição Score de crédito
# 

# %%
import pandas as pd 
import numpy as np
import plotly.express as px
import seaborn as sns
from sklearn.model_selection import train_test_split


# %%
df = pd.read_csv("lending_club_loan_two.csv")

# %%
df.head()

# %%
df.tail()

# %%
df.info()

# %%
df.isnull().sum()

# %%
df["mort_acc"].info()

# %%
df["pub_rec_bankruptcies"].info()

# %%
df["revol_util"].info()

# %%
df["revol_util"] = df["revol_util"].fillna(df["revol_util"].median())
df["mort_acc"] = df["mort_acc"].fillna(df["mort_acc"].median())
df["pub_rec_bankruptcies"] = df["pub_rec_bankruptcies"].fillna(df["pub_rec_bankruptcies"].median())


# %%
df.isna().sum()

# %%
