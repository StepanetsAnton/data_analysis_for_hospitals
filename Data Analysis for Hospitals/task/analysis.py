import pandas as pd
import numpy as np



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

hospital_counts = cleaned_df['hospital'].value_counts()
hospital_highest_patients = hospital_counts.idxmax()
print(f"The answer to the 1st question is {hospital_highest_patients}")

general_stomach_issues = cleaned_df[(cleaned_df['hospital'] == 'general') & (cleaned_df['diagnosis'] == 'stomach')].shape[0]
general_total_patients = cleaned_df[cleaned_df['hospital'] == 'general'].shape[0]
general_stomach_share = round(general_stomach_issues / general_total_patients, 3)
print(f"The answer to the 2nd question is {general_stomach_share}")

sports_dislocation_issues = cleaned_df[(cleaned_df['hospital'] == 'sports') & (cleaned_df['diagnosis'] == 'dislocation')].shape[0]
sports_total_patients = cleaned_df[cleaned_df['hospital'] == 'sports'].shape[0]
sports_dislocation_share = round(sports_dislocation_issues / sports_total_patients, 3)
print(f"The answer to the 3rd question is {sports_dislocation_share}")

general_median_age = cleaned_df[cleaned_df['hospital'] == 'general']['age'].median()
sports_median_age = cleaned_df[cleaned_df['hospital'] == 'sports']['age'].median()
median_age_difference = abs(general_median_age - sports_median_age)
print(f"The answer to the 4th question is {median_age_difference}")

blood_test_counts = cleaned_df[cleaned_df['blood_test'] == 't']['hospital'].value_counts()
hospital_most_blood_tests = blood_test_counts.idxmax()
most_blood_tests_count = blood_test_counts.max()
print(f"The answer to the 5th question is {hospital_most_blood_tests}, {most_blood_tests_count} blood tests")