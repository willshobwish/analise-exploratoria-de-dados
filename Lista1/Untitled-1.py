# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %%
numero_email=48
df = pd.read_csv(r'dad600.acad3.csv')
df_sample = df.sample(n=100,random_state=numero_email)

# %%
ecivil = df_sample["E.Civil"].value_counts()

# %%
df_sample["E.Civil"].value_counts()/100

# %%
plt.title("Distribuição do estado civil")
plt.ylabel("Frequencia")
plt.xlabel("Estado civil")
plt.bar(x=ecivil.index, height=ecivil)

# %%
ptreino = df_sample["P.Treino"].value_counts()
plt.title("Distribuição do periodo de treino")
plt.xlabel("Estado civil")
plt.pie(ptreino,labels=ptreino.index,autopct='%1.1f%%')

# %%
fsemanal = df_sample["Freq.Sem"].value_counts().reset_index()
fsemanal.columns = ["Freq.Sem", "count"]  # Rename columns
fsemanal["percent"] = fsemanal["count"] / fsemanal["count"].sum() * 100
display(fsemanal)

# %%
plt.bar(x=fsemanal["Freq.Sem"], height=fsemanal['count'])
plt.title("Frequencia semanal")
plt.ylabel("Frequencia")
plt.xlabel("Dias por semana")

# %%
inst = df_sample["Aval.Instal"].value_counts().reset_index()
inst.columns = ["Aval.Instal", "count"]  # Rename columns
inst["percent"] = inst["count"] / inst["count"].sum() * 100
display(inst)

# %%
plt.bar(x=inst["Aval.Instal"], height=inst['count'])
plt.title("Avaliação das instalações")
plt.ylabel("Frequencia")
plt.xlabel("Nota")

# %%
cross_treino_civil = pd.crosstab(df_sample["P.Treino"],df_sample["E.Civil"])
display(cross_treino_civil)

# %%
pd.crosstab(df_sample["P.Treino"], df_sample["E.Civil"],normalize='all')

# %%
# Este bloco cruza duas variáveis do conjunto de dados — por exemplo, "Freq.Sem" e "Aval.Aparelhos".
# Primeiro, usamos `pd.crosstab()` para contar quantas vezes cada combinação de valores ocorre entre essas duas variáveis.
# Isso gera uma tabela de frequência absoluta, onde cada célula mostra o número de pessoas com uma determinada frequência de treino e avaliação dos aparelhos.
# Em seguida, usamos `melt()` para transformar essa tabela para o formato "longo", no qual cada linha representa uma combinação entre as variáveis e sua contagem.
col2 = "P.Treino"
col1 = "E.Civil"
cross_troca_prof = pd.crosstab(df_sample[col1],df_sample[col2])
tabela_long = cross_troca_prof.reset_index().melt(id_vars=col1, var_name=col2, value_name="Count")
sns.barplot(x=col1, y="Count", hue=col2, data=tabela_long)

# %%
col2 = "P.Treino"
col1 = "Freq.Sem"
cross_troca_prof = pd.crosstab(df_sample[col1],df_sample[col2])
tabela_long = cross_troca_prof.reset_index().melt(id_vars=col1, var_name=col2, value_name="Count")
sns.barplot(x=col1, y="Count", hue=col2, data=tabela_long)

# %%
col2 = "P.Troca.Acad"
col1 = "Aval.Prof"
cross_troca_prof = pd.crosstab(df_sample[col1],df_sample[col2])
tabela_long = cross_troca_prof.reset_index().melt(id_vars=col1, var_name=col2, value_name="Count")
sns.barplot(x=col1, y="Count", hue=col2, data=tabela_long)

# %%
col2 = "P.Troca.Acad"
col1 = "E.Civil"
cross_troca_prof = pd.crosstab(df_sample[col1],df_sample[col2])
tabela_long = cross_troca_prof.reset_index().melt(id_vars=col1, var_name=col2, value_name="Count")
sns.barplot(x=col1, y="Count", hue=col2, data=tabela_long)

# %%
col2 = "Aval.Instal"
col1 = "P.Treino"
cross_troca_prof = pd.crosstab(df_sample[col1],df_sample[col2])
tabela_long = cross_troca_prof.reset_index().melt(id_vars=col1, var_name=col2, value_name="Count")
sns.barplot(x=col1, y="Count", hue=col2, data=tabela_long)

# %%
col2 = "Aval.Aparelhos"
col1 = "Freq.Sem"
cross_troca_prof = pd.crosstab(df_sample[col1],df_sample[col2])
tabela_long = cross_troca_prof.reset_index().melt(id_vars=col1, var_name=col2, value_name="Count")
sns.barplot(x=col1, y="Count", hue=col2, data=tabela_long)


