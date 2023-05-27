# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load data
data = pd.read_csv('content_data.csv')

# Split data into training and testing sets
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# Define features and target variable
features = ['keyword', 'duration', 'views', 'likes', 'dislikes', 'comments']
target = 'performance'

# Create linear regression model
model = LinearRegression()

# Fit model to training data
model.fit(train_data[features], train_data[target])

# Use model to predict performance on testing data
test_data['predicted_performance'] = model.predict(test_data[features])

# Calculate mean squared error of predictions
mse = np.mean((test_data[target] - test_data['predicted_performance']) ** 2)

# Print mean squared error
print("Mean squared error:", mse)

# Save model for future use
from sklearn.externals import joblib
joblib.dump(model, 'content_sourcing_model.pkl')

# Use saved model to make real-time content sourcing recommendations
def recommend_content():
    # Load saved model
    model = joblib.load('content_sourcing_model.pkl')
    
    # Get data on current content performance
    current_performance = pd.read_csv('current_performance.csv')
    
    # Make predictions on current performance data
    predicted_performance = model.predict(current_performance[features])
    
    # Sort predicted performance in descending order
    sorted_performance = predicted_performance.argsort()[::-1]
    
    # Get top-performing keywords
    top_keywords = []
    for i in sorted_performance:
        keyword = current_performance.loc[i, 'keyword']
        if keyword not in top_keywords:
            top_keywords.append(keyword)
        
        if len(top_keywords) >= 5:
            break
    
    # Return list of recommended keywords
    return top_keywords
