import pandas as pd
import numpy as np
pd.set_option('display.max_columns', 8)


gen=pd.read_csv('general.csv')
pren=pd.read_csv('prenatal.csv')
sport=pd.read_csv('sports.csv')

pren.columns = gen.columns
sport.columns = gen.columns

merged_df = pd.concat([gen, pren, sport], ignore_index=True)
merged_df = merged_df.drop(columns=['Unnamed: 0'])

cleaned_df = merged_df.dropna(how='all')
cleaned_df['gender'] = cleaned_df['gender'].replace({'female': 'f', 'male': 'm', 'man': 'm', 'woman': 'f'})
cleaned_df.loc[(cleaned_df['hospital'] == 'prenatal') & (cleaned_df['gender'].isna()), 'gender'] = 'f'
columns_to_fill = ['bmi', 'diagnosis', 'blood_test', 'ecg', 'ultrasound', 'mri', 'xray', 'children', 'months']
cleaned_df[columns_to_fill] = cleaned_df[columns_to_fill].fillna(0)

print(cleaned_df.shape)

pd.set_option('display.max_columns', 8)
print(cleaned_df.sample(n=20, random_state=30))