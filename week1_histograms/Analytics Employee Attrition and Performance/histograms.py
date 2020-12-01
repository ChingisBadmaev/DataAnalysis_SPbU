import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

data = pd.read_csv('datasets_1067_1925_WA_Fn-UseC_-HR-Employee-Attrition.csv')
df = pd.DataFrame(data)

# histogram number  1

# sns.distplot(data['Age'], hist=True, kde=False,  norm_hist=False, bins=np.linspace(0, 70), color='blue', hist_kws={'edgecolor':'black'})

# sns.distplot(data['Age'], hist=True, kde=False,  norm_hist=False, bins=np.linspace(0, 18), color='blue', hist_kws={'edgecolor':'black'})

# sns.distplot(data['Age'], hist=True, kde=False,  norm_hist=False, bins=np.linspace(50, 70), color='blue', hist_kws={'edgecolor':'black'})

# sns.distplot(data['Age'], hist=True, kde=False,  norm_hist=False, bins=np.linspace(18, 65), color='blue', hist_kws={'edgecolor':'black'})

# histogram number 2
'''
educationField = data['EducationField']
yearsInCurrentRole = data['YearsInCurrentRole']
plt.bar(educationField, yearsInCurrentRole)

plt.xlabel('Education Field')
plt.ylabel('Years In Current Role')
plt.show()
'''
# histogram number 3
'''
data.plot(y='Age', kind='hist', color='blue', edgecolor='black')
plt.show()
'''
'''
dailyRate = data['DailyRate']
education = data['Education']
plt.xlabel('Daily rate')
plt.ylabel('Education')
plt.bar(dailyRate, education)
plt.show()
'''
# histogram number 4
'''
sns.distplot(data['DailyRate'], hist=True, kde=False,  norm_hist=False, bins=np.linspace(100, 1500), color='blue', hist_kws={'edgecolor':'black'})
plt.title('Distribution density')
plt.xlabel('Daily rate')
plt.show()
'''