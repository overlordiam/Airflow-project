from googleapiclient.discovery import build
import os
from dotenv import load_dotenv
import s3fs
import pandas as pd
import json


def ingest_data():

    load_dotenv()

    api_key = os.getenv('GOOGLE_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    results = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        chart="mostPopular",
        regionCode="US",  
        maxResults=50  
        ).execute()

    # with open('test.json', 'r') as f:
    #     results = json.load(f)

    # print(len(results['items']))

    comments = []

    # while results:
    for item in results['items']:
        try:
            publishedAt = item['snippet']['publishedAt']
            title = item['snippet']['title']
            channel = item['snippet']['channelTitle']
            language = item['snippet'].get('defaultLanguage', '')
            view_count = item['statistics'].get('viewCount', 0),
            like_count = item['statistics'].get('likeCount', 0),
            comment_count = item['statistics'].get('commentCount', 0)


            comments.append({
                'title': title,
                'publishedAt': publishedAt,
                'channel': channel,
                'language': language,
                'viewCount': view_count[0],
                'likeCount': like_count[0],
                'commentCount': comment_count
            })
        
        except KeyError as e:
            print(e)


    # with open('processed_test.json', 'w') as f:
    #     json.dump(comments, f, indent=4)


        # if 'nextPageToken' in results:
        #     results = youtube.videos().list(
        #     part="snippet,contentDetails,statistics",
        #     chart="mostPopular",
        #     regionCode="US",  # You can change this to get popular videos from different countries
        #     maxResults=50,
        #     nextPageToken=results['nextPageToken']  # You can adjust this, max is 50 per request
        #     ).execute()

        # else:
        #     break


    df = pd.DataFrame(comments)
    df.to_csv('s3://suhaas-airflow-project-bucket/raw_youtube_comments.csv', index=False)
    
    print(f'Finished ingesting all the comments.')

ingest_data()
