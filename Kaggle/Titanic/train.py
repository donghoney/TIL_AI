import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

'''
Survived: 생존 여부 => 0 = No, 1 = Yes
pclass: 티켓 등급 => 1 = 1st, 2 = 2nd, 3 = 3rd
Sex: 성별
Age: 나이
Sibsp: 함께 탑승한 형제자매, 배우자의 수
Parch: 함께 탑승한 부모, 자식의 수
Ticket: 티켓 번호
Fare: 운임
Cabin: 객실 번호
Embarked: 탑승 항구 => C = Cherbourg, Q = Queenstown, S = Southampton
'''


train_path = 'train.csv'
test_path = 'test.csv'
train_df = pd.read_csv(train_path)
test_df = pd.read_csv(test_path)

print(train_df.head())

f, ax = plt.subplots(1, 2, figsize=(18,8))
train_df['Survived'].value_counts().plot.pie(explode=[0,0.1],autopct = '%1.1f%%',ax=ax[0],shadow=True)
ax[0].set_title('Survived')
ax[0].set_ylabel('')
sns.countplot('Survived',data=train_df,ax=ax[1])
ax[1].set_title('Survived')
plt.show()

f, ax = plt.subplots(1, 2, figsize=(18,8))
train_df['Survived'][train_df['Sex'] == 'male'].value_counts().plot.pie(explode=[0,0.1],
                                                                      autopct = '%1.1f%%',
                                                                      ax=ax[0],
                                                                      shadow=True)

train_df['Survived'][train_df['Sex'] == 'female'].value_counts().plot.pie(explode=[0, 0.1],
                                                                        autopct='%1.1f%%',
                                                                        ax=ax[1],
                                                                        shadow=True)
ax[0].set_title('Survived (male)')
ax[1].set_title('Survived (female)')
plt.show()

cross_tab = pd.crosstab([train_df['Sex'],
                train_df['Survived']],
                train_df['Pclass'],
                margins=True).style.background_gradient(cmap='summer_r')

