def predict_anomalies(model, features, df):
    """
    Predict anomalies using the trained model.
    In Isolation Forest: -1 means anomaly, 1 means normal.
    We convert this to boolean True/False for 'is_anomaly'.
    """
    print("Detecting anomalies...")
    predictions = model.predict(features)
    
    # Map raw predictions (-1 for anomaly) to boolean
    df['is_anomaly'] = predictions == -1
    
    anomalies_count = df['is_anomaly'].sum()
    print(f"Detection complete. Found {anomalies_count} anomalies out of {len(df)} logs.")
    
    return df

def print_results(df):
    """
    Print the results grouped by normal and anomalous logs.
    """
    print("\n--- NORMAL LOGS ---")
    normals = df[df['is_anomaly'] == False]['log']
    for log in normals:
        print(f"[OK] {log}")
        
    print("\n--- ANOMALOUS LOGS ---")
    anomalies = df[df['is_anomaly'] == True]['log']
    for log in anomalies:
        print(f"[!]  {log}")
