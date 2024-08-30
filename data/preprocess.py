import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(file_path):
    data = pd.read_csv(file_path)
    
    label_encoder = LabelEncoder()
    data['ip_src'] = label_encoder.fit_transform(data['ip_src'])
    data['ip_dst'] = label_encoder.fit_transform(data['ip_dst'])
    
    X = data[['ip_src', 'ip_dst']].values
    y = data['label'].values
    
    return X, y
