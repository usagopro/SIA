import joblib

# Load the trained SVM model from the saved file
loaded_svm_model = joblib.load('svm_model.pkl')

# Load the vectorizer
loaded_vectorizer = joblib.load('vectorizer.pkl')

# Now you can use loaded_svm_model to make predictions on new data

# Preprocess the new data and store it in a variable
new_data = ["open amazon website"]

# Vectorize the new data using the same vectorizer used for training
new_data_vectorized = loaded_vectorizer.transform(new_data)

# Use the loaded SVM model to make predictions on the new data
predictions = loaded_svm_model.predict(new_data_vectorized)

# Print the predictions
print("Predictions:", predictions)
