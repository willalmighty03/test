import time
import datetime
import google_auth_oauthlib.flow
import googleapiclient.errors
import googleapiclient.discovery
import googleapiclient.http

# Set up authentication flow and build the client object
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    'client_secrets.json', scopes=['https://www.googleapis.com/auth/youtube.force-ssl'])
creds = flow.run_local_server(port=0)
youtube = googleapiclient.discovery.build('youtube', 'v3', credentials=creds)

# Define the schedule for video uploads
upload_times = [
    datetime.time(hour=9, minute=0),  # 9:00 AM
    datetime.time(hour=12, minute=0),  # 12:00 PM
    datetime.time(hour=15, minute=0),  # 3:00 PM
    datetime.time(hour=18, minute=0),  # 6:00 PM
    datetime.time(hour=21, minute=0),  # 9:00 PM
]

while True:
    # Get the current time
    now = datetime.datetime.now().time()

    # Check if it's time to upload a video
    if now in upload_times:

        # Generate the video and get relevant information
        video = generate_video()
        title = video['title']
        description = video['description']
        tags = video['tags']
        video_path = video['video_path']

        # Upload the video to YouTube
        request_body = {
            'snippet': {
                'title': title,
                'description': description,
                'tags': tags,
                'categoryId': '22'  # CategoryId for short videos
            },
            'status': {
                'privacyStatus': 'public'
            }
        }
        media = googleapiclient.http.MediaFileUpload(video_path)
        response = youtube.videos().insert(
            part='snippet,status',
            body=request_body,
            media_body=media
        ).execute()

        # Print the video ID and upload time for verification
        print(f
