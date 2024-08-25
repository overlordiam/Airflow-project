from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('GOOGLE_API_KEY')
video_id = 'q8q3OFFfY6c'

youtube = build('youtube', 'v3', developerKey=api_key)

def get_comments(youtube, video_id):
    comments = []
    results = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        textFormat="plainText"
    ).execute()

    while results:
        for item in results['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)

        if 'nextPageToken' in results:
            results = youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                textFormat="plainText",
                pageToken=results['nextPageToken']
            ).execute()
        else:
            break

    return comments

video_comments = get_comments(youtube, video_id)
for comment in video_comments:
    print(comment)