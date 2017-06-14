# ! This Code is for creating simple and fast graph for observe the key features of the data. !


import pandas as pd 
import matplotlib.pyplot as plt

path = " Data Path Here" 

Df = pd.read_csv(path + 'Outlier_Cleaned_2.csv',encoding = 'ISO-8859-1') #Encoding for utf-8 files

a = plt.scatter(Df['User_Score'],Df['Global_Sales'])
plt.xlabel('User_Score')
plt.ylabel('Global_Sales')
plt.savefig("Foo.pdf") # Saves figure under the current project folder
plt.show() # Used for avoiding plots to overlap


b = plt.scatter(Df['Critic_Score'],Df['Global_Sales'])
plt.xlabel('Critic_Score')
plt.ylabel('Global_Sales')
plt.savefig("Bar.pdf") 
