#C:\\Users\\rahul\\OneDrive\\Desktop\\pedictive_analysis\\static
from flask import Flask, request, jsonify, render_template
from model import PredictiveModel
import os
import json
from datetime import datetime

app = Flask(__name__)
predictive_model = PredictiveModel()
UPLOAD_FOLDER = 'C:\\Users\\rahul\\OneDrive\\Desktop\\pedictive_analysis\\static'
PREDICTIONS_FOLDER = 'C:\\Users\\rahul\\OneDrive\\Desktop\\pedictive_analysis\\predictions'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PREDICTIONS_FOLDER'] = PREDICTIONS_FOLDER

# Ensure the predictions folder exists
os.makedirs(PREDICTIONS_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        return "File uploaded successfully", 200

@app.route('/train', methods=['POST'])
def train_model():
    data_path = os.path.join(UPLOAD_FOLDER, 'sample_data.csv')
    metrics = predictive_model.train_model(data_path)
    return jsonify(metrics)

@app.route('/predict', methods=['POST'])
def predict():
    content = request.json
    if not content or 'Temperature' not in content or 'Run_Time' not in content:
        return "Invalid input", 400
    input_data = [content['Temperature'], content['Run_Time']]
    result = predictive_model.predict(input_data)
    
    # Save the prediction result to a JSON file
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'prediction_{timestamp}.json'
    file_path = os.path.join(app.config['PREDICTIONS_FOLDER'], filename)
    with open(file_path, 'w') as f:
        json.dump(result, f)
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)