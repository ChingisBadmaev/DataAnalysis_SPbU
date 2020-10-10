import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

data_SALE_LIST = pd.read_csv('SALE_LIST.csv', sep=';')
data_SALE_LIST['date'] = data_SALE_LIST['date'].apply(lambda x: x[6:])
data_PRODUCT_LIST = pd.read_csv('PRODUCT_LIST.CSV', encoding='cp1251')



print()
