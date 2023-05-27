import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

# Authenticate with YouTube's API using OAuth 2.0
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    'client_secret.json', ['https://www.googleapis.com/auth/youtube.force-ssl'])
creds = flow.run_local_server(port=0)
youtube = googleapiclient.discovery.build('youtube', 'v3', credentials=creds)

# Search for videos related to specific keywords
search_response = youtube.search().list(
    q='Andrew Tate, Joe Rogan, David Goggins, Mr. Beast, Elon Musk',
    type='video',
    videoDuration='short',
    fields='items(id(videoId),snippet(title,description))'
).execute()

# Extract relevant keywords and topics from video metadata and content
for search_result in search_response.get('items', []):
    video_id = search_result['id']['videoId']
    video_title = search_result['snippet']['title']
    video_description = search_result['snippet']
