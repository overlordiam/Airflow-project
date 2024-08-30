


def youtube_etl():

    api_key = os.getenv('GOOGLE_API_KEY')
    video_id = 'lYRDD_drRuI'

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
                author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
                author = author.replace('@', '')
                published_time = item['snippet']['topLevelComment']['snippet']['publishedAt']

                comments.append({
                    'author': author,
                    'comment': comment,
                    'published_time': published_time
                })

            if 'nextPageToken' in results:
                results = youtube.commentThreads().list(
                    part="snippet",
                    videoId=video_id,
                    textFormat="plainText",
                    pageToken=results['nextPageToken']
                ).execute()
            else:
                break

        print(f'Finished processing all the comments.')

        return comments


    def make_csv(comments):
        df = pd.DataFrame(comments)
        df.to_csv('s3://suhaas-airflow-project-bucket/youtube_comments.csv')

    video_comments = get_comments(youtube, video_id)
    make_csv(video_comments)
