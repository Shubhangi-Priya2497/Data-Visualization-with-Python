import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#create the dataframes using the csv file.
df = pd.read_csv(r'./rain.csv')
print(df)

data = df.pivot("Month","Rainfall","Temperature")
print(data)

sns.heatmap(data, annot=True, fmt="f")
plt.show()