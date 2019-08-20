import pandas as pd

def clean_title(df):
    """
    Clean al titles of the columns and delete 
    unnesessary columans.

    Parameters
        ----------
        df : is the DataFrame that will be modificated and returned
    """
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
    """
    Clean all dataFrame of caracters unnesesary. Then cast the colums to specific
    data type.

    Parameters
        ----------
        df : is the DataFrame that will be modificated and returned
    """

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

def set_percentage_population(df):
    """
    Include a new column named "Porcentaje de Población" that contain the percentage
    of population each region.

    Parameters
        ----------
        df : is the DataFrame that will be modificated and returned
    """
    total = df['Población'].sum()
    df["Porcentaje de Población"] = round(df["Población"]/total * 100,2)
    df["Porcentaje de Población"] = df["Porcentaje de Población"].astype(str)
    df["Porcentaje de Población"] = df["Porcentaje de Población"] + "%"
    return df

# Main of the de program
print("Getting data from wiki Chile...")
dfs = pd.read_html('https://es.wikipedia.org/wiki/Chile', header = 1, attrs={'class': 'wikitable col1izq col2der col3der col4der col5der col6izq'}, encoding='utf-8')
df = dfs[0]

print("Cleaning data")
df = clean_title(df)
df = clean_data(df)

print("Calculating the population percentage...")
df = set_percentage_population(df)

print(df)
df.to_csv(r'organizacion_territoral_de_chile.csv', index=False, encoding='utf-8')
# https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
# pip install -r requirements.txt
# Python >=3.5.3