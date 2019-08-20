import pandas as pd

def clean_title(df):
    del df['Mapa administrativo']
    df.rename(columns={'Región':'Región',
                'Población [8]​':'Población',
                'Superficie (km²)[4]​':'Superficie',
                'Densidad​':'Densidad',
                'Capital':'Capital',
                }, 
                 inplace=True)
    return df

def clean_data(df):
    df = df.iloc[:-1,].copy()
    df.replace(to_replace = r'\u200b', value = '', regex = True, inplace=True)
    df.replace(to_replace = r'\xa0', value = '', regex = True, inplace=True)
    df.replace(to_replace = r'\[[0-9]{1,8}\]', value = '', regex = True, inplace=True)
    df.replace(to_replace = r'\([0-9]{1,8}\)', value = '', regex = True, inplace=True)  

    df['Región'] = df['Región'].str.strip()
    df['Capital'] = df['Capital'].str.strip()
    df['Población'] = df['Población'].str.replace(" ","").astype('int64')
    df['Superficie'] = df['Superficie'].str.replace(",",".").astype('float')

    return df

def get_total_population(df):
    return df['Población'].sum()

def set_percentage_population(df, total):
    df["Porcentaje de Población"] = round(df["Población"]/total * 100,2)
    df["Porcentaje de Población"] = df["Porcentaje de Población"].astype(str)
    df["Porcentaje de Población"] = df["Porcentaje de Población"] + "%"
    return df


print("Init Program...")
print("Getting data from wiki Chile...")
dfs = pd.read_html('https://es.wikipedia.org/wiki/Chile', header = 1, attrs={'class': 'wikitable col1izq col2der col3der col4der col5der col6izq'}, encoding='latin-1')
df = dfs[0]

print("Cleaning data")
df = clean_title(df)
df = clean_data(df)

print("Calculating the population percentage...")
total = get_total_population(df)
df = set_percentage_population(df, total)
print(df)

df.to_csv(r'organizacion_territoral_de_chile.csv', index=False, encoding='latin-1')
# env
# pip install -r requirements.txt