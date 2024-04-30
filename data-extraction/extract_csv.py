import pandas as pd

laliga_data = pd.read_csv("https://www.football-data.co.uk/mmz4281/2324/SP1.csv")

df_laliga = pd.DataFrame(laliga_data)

print(df_laliga)
