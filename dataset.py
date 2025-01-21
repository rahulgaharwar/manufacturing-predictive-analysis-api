import pandas as pd
import numpy as np

# Generate synthetic data
np.random.seed(0)
data = {
    'Machine_ID': np.arange(1, 101),
    'Temperature': np.random.normal(75, 10, 100),
    'Run_Time': np.random.normal(200, 50, 100),
    'Downtime_Flag': np.random.choice([0, 1], size=100)
}

df = pd.DataFrame(data)
df.to_csv('C:\\Users\\rahul\\OneDrive\\Desktop\\pedictive_analysis\\static\\sample_data.csv', index=False)