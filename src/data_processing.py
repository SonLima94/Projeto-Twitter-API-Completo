import pandas as pd

def load_tweets(file_path):
    return pd.read_json(file_path)

def process_tweets(df):
    df['created_at'] = pd.to_datetime(df['created_at'])
    df['word_count'] = df['text'].apply(lambda x: len(x.split()))
    return df

if __name__ == "__main__":
    df = load_tweets('tweets.json')
    df_processed = process_tweets(df)
    df_processed.to_csv('processed_tweets.csv', index=False)
