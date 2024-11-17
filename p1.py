import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Read the Titanic dataset
df = pd.read_csv('titanic.csv')

# Select relevant features and drop unnecessary columns
df = df[['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']]

# Handle missing values
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Convert categorical variables to numeric using Label Encoding
le = LabelEncoder()
df['Sex'] = le.fit_transform(df['Sex'])
df['Embarked'] = le.fit_transform(df['Embarked'])

# Scale numerical features
df['Fare'] = np.log1p(df['Fare'])  # Log transform fare to handle skewness

# Print info about the preprocessed dataset
print("Dataset Info after preprocessing:")
print(df.info())
print("\nSample of preprocessed data:")
print(df.head())
