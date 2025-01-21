import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score

class PredictiveModel:
    def __init__(self):
        self.model = None

    def train_model(self, data_path):
        df = pd.read_csv(data_path)
        X = df[['Temperature', 'Run_Time']]
        y = df['Downtime_Flag']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
        
        # You can use LogisticRegression or DecisionTreeClassifier
        self.model = LogisticRegression()
        self.model.fit(X_train, y_train)
        
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        
        return {'accuracy': accuracy, 'f1_score': f1}

    def predict(self, input_data):
        if self.model is None:
            raise Exception("Model is not trained yet. Please train the model first.")
        
        prediction = self.model.predict([input_data])
        confidence = self.model.predict_proba([input_data])[0][prediction][0]
        
        return {'Downtime': 'Yes' if prediction[0] == 1 else 'No', 'Confidence': confidence}