import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset and skip the header row
columns = ['Sex', 'Length', 'Diameter', 'Height', 'Whole weight', 
           'Shucked weight', 'Viscera weight', 'Shell weight', 'Rings']
df = pd.read_csv('abalone.csv', skiprows=1, names=columns)

# Convert Sex to numeric using one-hot encoding
df = pd.get_dummies(df, columns=['Sex'])

# Ensure all numeric columns are float type
numeric_columns = ['Length', 'Diameter', 'Height', 'Whole weight', 
                  'Shucked weight', 'Viscera weight', 'Shell weight', 'Rings']
df[numeric_columns] = df[numeric_columns].astype(float)

# Split features and target
X = df.drop('Rings', axis=1)
y = df['Rings']

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on test set
y_pred = model.predict(X_test)

# Print model performance metrics
print("\nModel Performance Metrics:")
print(f"R-squared Score: {r2_score(y_test, y_pred):.4f}")
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred):.4f}")
print(f"Root Mean Squared Error: {np.sqrt(mean_squared_error(y_test, y_pred)):.4f}")

# Print training dataset summary
print("\nTraining Dataset Summary:")
print(X_train.describe())
