import re
from sklearn.feature_extraction.text import TfidfVectorizer

def clean_log(text):
    """
    Basic text cleaning: lowercase and remove special characters.
    """
    text = str(text).lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text

def preprocess_logs(df):
    """
    Clean the log text and convert it to numerical features using TF-IDF.
    Returns the processed dataframe, extracted features, and the fitted vectorizer.
    """
    print("Preprocessing log data...")
    df['cleaned_log'] = df['log'].apply(clean_log)
    
    # Convert text to numerical features using TF-IDF
    vectorizer = TfidfVectorizer(max_features=100)
    features = vectorizer.fit_transform(df['cleaned_log']).toarray()
    
    return df, features, vectorizer
