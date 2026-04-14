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
    Limit output to the first 10 instances of each to prevent console spam.
    """
    print("\n--- NORMAL LOGS ---")
    normals = df[df['is_anomaly'] == False]['log']
    for log in normals[:10]:
        print(f"[OK] {log}")
    if len(normals) > 10:
        print(f"... and {len(normals) - 10} more normal logs.")
        
    print("\n--- ANOMALOUS LOGS ---")
    anomalies = df[df['is_anomaly'] == True]['log']
    for log in anomalies[:10]:
        print(f"[!]  {log}")
    if len(anomalies) > 10:
        print(f"... and {len(anomalies) - 10} more anomalous logs.")
