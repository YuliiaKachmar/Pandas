import statistics
import pandas as pd


# Get data from 'titanic_train.csv' into Pandas.DataFrame
data = pd.read_csv('titanic_train.csv', index_col='PassengerId')
print(data.head(10))
print(data.describe())

# Get passengers with Embarked= C and price for ticket higher than 200
data[(data['Embarked'] == 'C') & (data.Fare > 200)].head()
print(data)

# Sort by ticket price
print(data[(data['Embarked'] == 'S') &
           (data['Fare'] > 200)].sort_values(by='Fare',
                                             ascending=False).head())


# Add new column
def age_category(age):
    if age < 30:
        return 1
    elif age < 55:
        return 2
    else:
        return 3


age_categories = [age_category(age) for age in data.Age]
data['Age_category'] = age_categories
print(data.head(10))

# Sex statistics
print(data.groupby("Sex")["Sex"].count())

# Quantity of men, women in each class
print(pd.crosstab(data['Pclass'], data['Sex']))

# Mediana and deviation based on 'Fare'
mediana = round(data['Fare'].median(), 2)
deviation = round(statistics.stdev(data['Fare']), 2)
print("Mediana - {0}, deviation - {1}".format(mediana, deviation))


# Statistics of survival people by age category
def age_category(age):
    if age < 25:
        return "Younger than 25"
    elif age > 25 and age < 35:
        return "Older than 25 and younger than 35"
    elif age > 35 and age < 50:
        return "Older than 35 and younger than 50"
    elif age > 50:
        return "Older than 50"


age_categories = [age_category(age) for age in data.Age]
data['Age_category'] = age_categories
print(pd.crosstab(data['Age_category'], data['Survived'], normalize='index'))

# Statistics of survival people by sex
print(pd.crosstab(data['Sex'], data['Survived'], margins=True, normalize='index'))

# The most popular name
data2 = data[data.Sex == 'male']['Name']
C = []
for i in data2:
    if '(' in i:
        if ')' in i.split('(')[1].split(' ')[0]:
            C.append(i.split('(')[1].split(' ')[0].split(')')[0])
        else:
            C.append(i.split('(')[1].split(' ')[0])

    else:
        C.append(i.split('. ')[1].split(' ')[0])

print(pd.DataFrame.from_dict(C)[0].value_counts().nlargest(1))
