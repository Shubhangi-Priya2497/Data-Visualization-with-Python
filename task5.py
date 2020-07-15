import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#create the dataframes using the csv file.
df = pd.read_csv(r'./rain.csv')
print(df)

sns.jointplot("Rainfall", "Temperature",data=df,kind="hex")
plt.show()