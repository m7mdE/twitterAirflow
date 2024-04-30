import pandas as pd
import string
import re
import s3fs


def run_twitter_etl():

    # Initialize the S3 client
    s3 = s3fs.S3FileSystem()

    # reading from the file
    # df = pd.read_csv('tweets.csv')

    try:
        # Specify the bucket name and file key
        bucket_name = 'twitter-airflow-test-bucket'
        file_key = 'tweets.csv'

        with s3.open(f'{bucket_name}/{file_key}', 'rb') as file:
            df = pd.read_csv(file)

        # dropping unnecessary columns
        df = df.drop(columns=['country', 'date_time', 'id',
                              'language', 'latitude', 'longitude'], axis=1)

        # renaming columns
        df.columns = ['author', 'text', 'likes', 'shares']

        # Define regular expressions for URLs, mentions, and hashtags
        url_pattern = r'https?://\S+|www\.\S+'
        mention_pattern = r'@\w+'
        hashtag_pattern = r'#\w+'

        def clean_text(text):
            # Remove URLs, hashtags, and mentions using regular expressions
            cleaned_sentence = re.sub(url_pattern, '', text)
            cleaned_sentence = re.sub(mention_pattern, '', cleaned_sentence)
            cleaned_sentence = re.sub(hashtag_pattern, '', cleaned_sentence)
            # Remove punctuation and convert to lowercase
            text = ''.join([word.lower()
                            for word in cleaned_sentence if word not in string.punctuation])
            # Tokenize the text
            tokens = re.split('\W+', text)
            # Removing empty characters
            empty_char = [word for word in tokens if word not in '']
            # Remove stopwords
            # text = [word for word in empty_char if word not in stopwords]
            return text

        # calling clean_text method and apply it to a new column called clean_text
        df['clean_text'] = df['text'].apply(lambda x: clean_text(x))

        # drop rows that contains empty arrays in order for the ML model to work
        df.drop(df[df['clean_text'].apply(len) == 0].index, inplace=True)

        # creating a clean data file
        df.to_csv('s3://twitter-airflow-test-bucket/clean_data.csv')

    except Exception as e:
        print(f"Error reading file from S3: {e}")
