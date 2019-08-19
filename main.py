import pandas as pd

dfs = pd.read_html('https://es.wikipedia.org/wiki/Chile', header = 1, attrs={'class': 'wikitable col1izq col2der col3der col4der col5der col6izq'})
df = dfs[0]
print(df.columns)
