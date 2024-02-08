"""
Для преобразования столбца DataFrame в формат one hot encoding без использования
функции get_dummies, мы можем воспользоваться циклом и условным выражением.

Код создаст новые столбцы для каждого уникального значения в исходном столбце 'whoAmI'
и заполнит их нулями и единицами в зависимости от того, соответствует ли значение в исходном
столбце значению нового столбца.
"""

import pandas as pd

# Создаем DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Получаем уникальные значения
unique_values = data['whoAmI'].unique()

# Создаем столбцы для каждого уникального значения
for value in unique_values:
    data[value] = (data['whoAmI'] == value).astype(int)

# Удаляем исходный столбец 'whoAmI'
data.drop(columns=['whoAmI'], inplace=True)

print(data.head())
