import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib


# Load your dataset
df = pd.read_csv('commands_and_actions.csv')

# Split the data into training and testing sets
X = df['Command']
y = df['Action']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4)

# Create a text vectorizer (CountVectorizer)
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Train a Support Vector Machine (SVM) classifier
svm_classifier = SVC(kernel='linear', C=1, random_state=42)
svm_classifier.fit(X_train_vectorized, y_train)

# Predict on the test set
y_pred = svm_classifier.predict(X_test_vectorized)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print("Accuracy:", accuracy)
# print("Classification Report:\n", report)

# Save the trained SVM model to a file
joblib.dump(svm_classifier, 'svm_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

