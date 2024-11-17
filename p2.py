import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Read the Titanic dataset
df = pd.read_csv('titanic.csv')

# Select relevant features
features = ['Pclass', 'Sex', 'Age']
X = df[features]
y = df['Survived']

# Handle missing values
X['Age'].fillna(X['Age'].mean(), inplace=True)

# Convert categorical variables to numeric
le = LabelEncoder()
X['Sex'] = le.fit_transform(X['Sex'])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Print model performance
print("\nModel Performance:")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Example prediction function
def predict_survival(pclass, sex, age):
    # Convert sex to numeric
    sex_numeric = 1 if sex.lower() == 'female' else 0
    
    # Create input array
    input_data = np.array([[pclass, sex_numeric, age]])
    
    # Make prediction
    probability = model.predict_proba(input_data)[0][1]
    return probability

# Example usage
print("\nExample Predictions:")
print("Probability of survival for:")
print(f"Class 1 female age 25: {predict_survival(1, 'female', 25):.2%}")
print(f"Class 3 male age 30: {predict_survival(3, 'male', 30):.2%}")
