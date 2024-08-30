import s3fs
import pandas as pd
import json
from datetime import datetime

def process_data():
        df = pd.read_csv('s3://suhaas-airflow-project-bucket/raw_youtube_comments.csv')
        # with open('processed_test.json', 'r') as f:
        #         df = json.load(f)
        # df = pd.DataFrame(df)
        df['commentCount'] = df['commentCount'].astype(int)
        df['viewCount'] = df['viewCount'].astype(int)
        df['likeCount'] = df['likeCount'].astype(int)
        df['publishedDate'] = df['publishedAt'].apply(lambda rec: datetime.strptime(rec[:10], "%Y-%m-%d").date())
        df['videoLikeability'] = round((df['likeCount'] / df['viewCount']) * 100, 2)
        df.drop('publishedAt', axis=1, inplace=True)

        df.to_csv('s3://suhaas-airflow-project-bucket/processed_youtube_comments.csv', index=False)

        print(f'Finished processing all the comments and published to S3.')

process_data()
