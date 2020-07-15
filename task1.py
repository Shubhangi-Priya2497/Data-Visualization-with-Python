import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#create the dataframes using the csv file.
df = pd.read_csv(r'./rain.csv')
print(df)

print("df statistics: \n", df.describe())

df.plot(x='Month', y= 'Temperature')
df.plot(x='Month', y= 'Rainfall')
plt.show()