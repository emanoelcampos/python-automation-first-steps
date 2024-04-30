import pandas as pd

breaking_bad_data = pd.read_html("https://en.wikipedia.org/wiki/List_of_Breaking_Bad_episodes", index_col=0)

df_breaking_bad_data = pd.DataFrame(breaking_bad_data[3])

print(df_breaking_bad_data)
