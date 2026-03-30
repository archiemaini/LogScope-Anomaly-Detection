import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from data_loading import load_data
from preprocessing import preprocess_logs
from model_training import train_model
from anomaly_detection import predict_anomalies, print_results

def visualize_results(df):
    """
    Create a simple visualization showing the count of normal vs anomalous logs.
    """
    counts = df['is_anomaly'].value_counts()
    
    plt.figure(figsize=(6, 4))
    counts.plot(kind='bar', color=['skyblue', 'salmon'])
    
    plt.title('Log Anomaly Detection Results')
    plt.xlabel('Classification')
    
    # Safely map the boolean indices to string labels
    label_map = {False: 'Normal', True: 'Anomaly'}
    plt.xticks(range(len(counts)), [label_map.get(idx, 'Unknown') for idx in counts.index], rotation=0)
    
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig('anomaly_distribution.png')
    print("\nVisualization saved to 'anomaly_distribution.png'")

def main():
    print("Starting Log Anomaly Detection System...\n")
    
    # 1. Load Data
    file_path = 'sample_logs.csv'
    df = load_data(file_path)
    
    if df is None:
        return
        
    # 2. Preprocess Data
    df, features, vectorizer = preprocess_logs(df)
    
    # 3. Train Model
    # Here contamination is set to 0.2 because 2 out of 10 logs are anomalies
    model = train_model(features, contamination=0.2)
    
    # 4. Predict Anomalies
    df = predict_anomalies(model, features, df)
    
    # 5. Output Results
    print_results(df)
    
    # Optional: Visualization
    visualize_results(df)

if __name__ == "__main__":
    main()
