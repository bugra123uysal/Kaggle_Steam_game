
import pandas as pd
import seaborn as sns
import  numpy as np
import matplotlib.pyplot  as plt

dt=pd.read_csv(r"C:\Users\buğra\Desktop\Steam_2024_bestRevenue_1500.csv")

print(dt.columns)
print(dt.info)
print(dt.isnull().sum())
print(dt.shape)
print(dt.head())





nn=dt.nlargest(10 ,'copiesSold' )

plt.plot(nn['name'], nn['copiesSold'] , label="copiesSold", color='red'  , marker="o"  )
plt.xticks(rotation=90)
plt.title("10 largest copies Sold is dataset ")
plt.legend()
plt.show()

mm=dt.nsmallest(10 , 'copiesSold' )
plt.plot(mm['name'], mm['copiesSold'], label="copiesSold", color='black', marker="o"   )
plt.xticks(rotation=90)
plt.title("10 smallest copies Sold is dataset ")
plt.legend()
plt.show()

csss=dt.nlargest(10 , 'revenue')


plt.plot(csss['name'], csss['revenue'], label='revenue', marker="o", color='black' )
plt.title("10 largest revenue is dataset")
plt.xticks(rotation=90)
plt.legend()
plt.show()

pc=dt.nsmallest(10, 'revenue')
plt.plot(pc['name'], pc['revenue'], label='revenue', marker="o", color='red' )
plt.title("10 smalest revenue is dataset")
plt.xticks(rotation=90)
plt.legend()
plt.show()


plt.pie(dt['price'].value_counts(), labels=dt['price'].unique(), autopct='%1.1f%%', startangle=90)
plt.show()

plt.pie(dt['publisherClass'].value_counts() , labels=dt['publisherClass'].unique(),autopct='%1.1f%%', startangle=90)
plt.show()
nma=dt['name']
pc=dt['publisherClass']
co=dt['copiesSold']
 
sns.pairplot(dt[['price','copiesSold','revenue','reviewScore','steamId'   ]])
plt.show()


k=dt.nsmallest(10,'reviewScore' )

sns.countplot(x='reviewScore',hue='publisherClass',  data=dt)
plt.show()

sns.scatterplot(x='price',y='copiesSold', hue='publisherClass' , data=dt)
plt.xticks(rotation=90)
plt.show()

sns.scatterplot(x='reviewScore', y='avgPlaytime', hue='publisherClass', data=dt)
plt.show()


b=dt.nlargest( 10, 'revenue' )
plt.plot('revenue',  '-' , data=b )
plt.show()
print(b)

