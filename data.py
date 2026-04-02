import pandas as pd
import matplotlib.pyplot as plt
#read from csv file into df
df=pd.read_csv('premier-league-matches.csv')


#decode FTR into readable format
#df['new_column']=value
df['result'] = df['FTR'].map({'H': 'Home Win', 'A': 'Away Win', 'D': 'Draw'})
#count each rows has how much value
print(df['result'].value_counts())
#normal convert to proportion
print(df['result'].value_counts(normalize=True).round(3))
#desribe()print all column related to numeric
print(df.describe())


#encode text of result column
#label encoder le_temp.fit()-used to find unique value and sort
#le_temp.transform()actually replaces the text with those numbers
from sklearn.preprocessing import LabelEncoder
le_temp = LabelEncoder()
#le_temp.fit_transform()-does both at same time
df['result_encoded'] = le_temp.fit_transform(df['result'])

# quick correlation check
print(df.corr(numeric_only=True)['result_encoded'].sort_values())


df['HomeGoals'].hist(bins=10)
plt.title('Distribution of Home Goals')
plt.show()


