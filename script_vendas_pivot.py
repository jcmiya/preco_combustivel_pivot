import pandas as pd

#verifica arquivo
from urllib.request import urlopen
url = "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos/de/vdpb/vendas-combustiveis-m3-1.xls"
df = pd.read_excel(url)

#identifica índice de referência das tabelas
for i in range(df.shape[0]):
  if df.iloc[i]['Unnamed: 1'] == df.iloc[i]['Unnamed: 1'] and 'derivados combustíveis de petróleo por Unidade da Federação e produto' in df.iloc[i]['Unnamed: 1']:
    indice_derivados = i
  if df.iloc[i]['Unnamed: 1'] == df.iloc[i]['Unnamed: 1'] and 'óleo diesel por tipo e Unidade da Federação' in df.iloc[i]['Unnamed: 1']:
    indice_diesel = i

#cria tabelas vazias
df_derivados = pd.DataFrame({'volume':[],'ano':[],'mes':[]})
df_diesel = pd.DataFrame({'volume':[],'ano':[],'mes':[]})

df.columns = [i for i in range(df.columns.shape[0])]

df_table = df.iloc[indice_derivados+10:indice_derivados+22][[j for j in range(1,24)]]

df.iloc[indice_derivados+9][[j for j in range(1,24)]]

df_table.columns = df.iloc[indice_derivados+9][[j for j in range(1,24)]]
df.iloc[indice_derivados+9][[j for j in range(1,24)]].values

for j in range(10, 22):
    df_derivados = df_derivados.append(
        pd.DataFrame({'volume': df.iloc[indice_derivados + j][2:24], 'ano': df.iloc[indice_derivados + 9][2:24],
                      'mes': df.iloc[indice_derivados + j][1]}))

for j in range(10, 22):
    df_diesel = df_diesel.append(
        pd.DataFrame({'volume': df.iloc[indice_diesel + j][2:24], 'ano': df.iloc[indice_diesel + 9][2:24],
                      'mes': df.iloc[indice_diesel + j][1]}))

df_derivados = pd.DataFrame({'volume':[],'ano':[],'mes':[]})
df_diesel = pd.DataFrame({'volume':[],'ano':[],'mes':[]})

for j in range(10, 22):
    for i in range(len(df.iloc[indice_derivados + 9][2:24])):
        df_derivados = df_derivados.append(
            {'volume': df.iloc[indice_derivados + j][2 + i], 'ano': df.iloc[indice_derivados + 9][2 + i],
             'mes': df.iloc[indice_derivados + j][1]}, ignore_index=True)

for j in range(10, 22):
    for i in range(len(df.iloc[indice_diesel + 9][2:11])):
        df_diesel = df_diesel.append(
            {'volume': df.iloc[indice_diesel + j][2 + i], 'ano': df.iloc[indice_diesel + 9][2 + i],
             'mes': df.iloc[indice_diesel + j][1]}, ignore_index=True)

df_diesel['unidade'] = df.iloc[indice_diesel+4][1][-3:-1]
df_derivados['unidade'] = df.iloc[indice_derivados+4][1][-3:-1]

import datetime
df_diesel['created_date'] = datetime.datetime.now()
df_derivados['created_date'] = datetime.datetime.now()

dic_mes = {'Jan':1,'Fev':2,'Mar':3,'Abr':4,'Mai':5,'Jun':6,'Jul':7,'Ago':8,'Set':9,'Out':10,'Nov':11,'Dez':12}

def aplicar_dic(x):
    return dic_mes[x]

df_diesel['mes'].apply(aplicar_dic)