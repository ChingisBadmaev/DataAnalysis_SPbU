import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

data = pd.read_csv('AB_NYC_2019.csv')
df = pd.DataFrame(data)

# histogram number 1
'''
sns.distplot(data['price'], hist=True, kde=False,  norm_hist=False, bins=np.linspace(0, 500), color='blue', hist_kws={'edgecolor':'black'})
plt.show()
'''
# вопрос к преподавателю как создать счетчик по оси у?


# histogram number 2
'''
data.plot(y='minimum_nights', kind='hist', edgecolor='black')
plt.xlim(0, 150)
data.plot(y='price', kind='hist', edgecolor='black')
plt.xlim(0, 2000)
plt.show()
'''
# как сделать разбиение столба, необходимо для точности


# histogram number 3
'''
price = data['price']
neighbourhood_group = data['neighbourhood_group']
plt.bar(neighbourhood_group, price)
plt.title('Price in New York districts')
plt.xlabel('Location')
plt.ylabel('Price')
plt.show()
'''

# histogram number 4
'''
price = data['price']
neighbourhood = data['neighbourhood']
plt.bar(neighbourhood, price) 
plt.xticks(rotation=90)
plt.xlabel('Neighbourhood')
plt.ylabel('Price')
plt.title('Price in New York neighbourhood')
plt.show()
'''

# histogram number 5
'''
price = data['price']
availability = data['availability_365']
plt.bar(availability, price)
plt.xlabel('availability')
plt.ylabel('price')
plt.show()
'''
'''
sns.distplot(data['availability_365'], hist=True, kde=False,  norm_hist=False, bins=np.linspace(1, 365), color='blue', hist_kws={'edgecolor':'black'})
plt.show()
'''