import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#create the dataframes using the csv file.
df = pd.read_csv(r'./rain.csv')

plt.figure(figsize=(17,5))
plt.plot( df['Month'], df['Temperature'], label='Temperature')
plt.show()

plt.figure(figsize=(17,5))
plt.plot( df['Month'], df['Rainfall'], label='Rainfall')
plt.show()

plt.figure(figsize=(17,5))
plt.plot( df['Month'], df['Rainfall'], label='Rainfall')
plt.plot( df['Month'], df['Temperature'], label='Tempertaure')
plt.legend()
plt.show()