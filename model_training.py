from sklearn.ensemble import IsolationForest

def train_model(features, contamination=0.2):
    """
    Train an Isolation Forest model to detect anomalies.
    'contamination' is the expected proportion of anomalies in the dataset.
    """
    print("Training Isolation Forest model...")
    # Using a fixed random state for reproducibility
    model = IsolationForest(contamination=contamination, random_state=42)
    model.fit(features)
    print("Model training complete.")
    return model
