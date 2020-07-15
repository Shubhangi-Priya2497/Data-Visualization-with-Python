import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#create the dataframes using the csv file.
df = pd.read_csv(r'./rain.csv')

sns.set(rc={'figure.figsize':(12,6)})
sns.regplot(x='Rainfall', y='Temperature', data = df)
plt.show()