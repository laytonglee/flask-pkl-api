# train_model.py
import pickle
import numpy as np
import sys
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Sample dataset (y = 3x + 5 + noise)
X = np.random.rand(100, 1) * 10
y = 3 * X + 5 + np.random.randn(100, 1)

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Save as PKL
with open("linear_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as linear_model.pkl")

print("Python version:", sys.version)
print("NumPy version:", np.__version__)
print("scikit-learn version:", sklearn.__version__)
