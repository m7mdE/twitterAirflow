import pandas as pd
import nltk
import string
import re
import preprocessor as p
stopwords = nltk.corpus.stopwords.words('english')


def run_twitter_etl():
    # reading from the file
    df = pd.read_csv('s3://airflow-moe/tweets.csv')

    # dropping unnecessary columns
    df = df.drop(columns=['country', 'date_time', 'id',
                          'language', 'latitude', 'longitude'], axis=1)

    # renaming columns
    df.columns = ['author', 'text', 'likes', 'shares']

    # Initialize preprocessor options
    p.set_options(p.OPT.URL, p.OPT.MENTION, p.OPT.HASHTAG)
    # cleaning text method - preprocess

    def clean_text(text):
        # Remove URLs, hashtags, and mentions using preprocessor
        cleaned_text = p.clean(text)
        # Remove punctuation and convert to lowercase
        text = ''.join([word.lower()
                        for word in cleaned_text if word not in string.punctuation])
        # Tokenize the text
        tokens = re.split('\W+', text)
        # Removing empty characters
        empty_char = [word for word in tokens if word not in '']
        # Remove stopwords
        text = [word for word in empty_char if word not in stopwords]
        return text

    # calling clean_text method and apply it to a new column called clean_text
    df['clean_text'] = df['text'].apply(lambda x: clean_text(x))

    # drop rows that contains empty arrays in order for the ML model to work
    df.drop(df[df['clean_text'].apply(len) == 0].index, inplace=True)

    # creating a file
    df.to_csv('s3://airflow-moe/clean_data.csv')
