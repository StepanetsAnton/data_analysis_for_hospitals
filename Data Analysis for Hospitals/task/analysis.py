import pandas as pd
pd.set_option('display.max_columns', 8)


gen=pd.read_csv('general.csv')
pren=pd.read_csv('prenatal.csv')
sport=pd.read_csv('sports.csv')

pren.columns = gen.columns
sport.columns = gen.columns

merged_df = pd.concat([gen, pren, sport], ignore_index=True)
merged_df = merged_df.drop(columns=['Unnamed: 0'])

pd.set_option('display.max_columns', 8)
print(merged_df.sample(n=20, random_state=30))