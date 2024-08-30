import joblib
from sklearn.ensemble import RandomForestClassifier
from data.preprocess import preprocess_data

def train_and_save_model(data_file, model_file):
    X, y = preprocess_data(data_file)
    
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)
    
    joblib.dump(model, model_file)
    print(f"Model saved to {model_file}")

# Call this function to train and save the model
train_and_save_model('data/training_data.csv', 'ai/example_model.pkl')
