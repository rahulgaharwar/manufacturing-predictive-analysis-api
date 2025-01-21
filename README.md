# Predictive Analysis for Manufacturing Operations

## Setup and Run

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/rahulgaharwar/manufacturing-predictive-analysis-api.git
    cd manufacturing-predictive-analysis-api
    ```

2. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Flask app:**
    ```bash
    python app.py
    ```

4. **Ensure the server is running:**
    You should see output indicating the server is running on `http://127.0.0.1:5000`.

## API Endpoints

### 1. Upload Endpoint
- **URL:** `/upload`
- **Method:** `POST`
- **Description:** Upload a CSV file containing manufacturing data.
- **Request:** Multipart form data with the file.
- **Response:** `"File uploaded successfully"`

#### Using Postman:
1. Open Postman.
2. Create a new `POST` request to `http://127.0.0.1:5000/upload`.
3. In the `Body` tab, select `form-data`.
4. Add a key named `file`, set the type to `File`, and choose a CSV file to upload.
5. Click `Send`.
6. You should receive a response: `"File uploaded successfully"`

### 2. Train Endpoint
- **URL:** `/train`
- **Method:** `POST`
- **Description:** Train the model on the uploaded dataset.
- **Response:** Returns JSON with accuracy and F1-score, e.g., `{"accuracy": 0.85, "f1_score": 0.80}`

#### Using Postman:
1. Create a new `POST` request to `http://127.0.0.1:5000/train`.
2. Click `Send`.
3. You should receive a response with the model's performance metrics.

### 3. Predict Endpoint
- **URL:** `/predict`
- **Method:** `POST`
- **Description:** Predict machine downtime.
- **Request:** JSON with `Temperature` and `Run_Time`.
- **Response:** Returns prediction result and confidence, e.g., `{"Downtime": "Yes", "Confidence": 0.85}`

#### Using Postman:
1. Create a new `POST` request to `http://127.0.0.1:5000/predict`.
2. In the `Body` tab, select `raw`, and choose `JSON` format.
3. Enter the JSON data, for example:
    ```json
    {
      "Temperature": 80,
      "Run_Time": 120
    }
    ```
4. Click `Send`.
5. You should receive a response with the prediction result and confidence.

## Example Requests and Responses

### Upload Endpoint Example
**Request:**
```bash
curl -X POST -F "file=@path/to/your/sample_data.csv" http://127.0.0.1:5000/upload
