import google.oauth2.credentials
import google.auth.exceptions
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Function to fetch analytics data from YouTube Analytics API
def fetch_analytics_data(api_key, channel_id):
    try:
        # Authenticate using API key
        youtube = build('youtubeAnalytics', 'v2', developerKey=api_key)

        # Fetch data for the past 7 days
        response = youtube.reports().query(
            ids='channel=={}'.format(channel_id),
            metrics='views,likes,comments',
            dimensions='hour',
            startDate='7daysAgo',
            endDate='today'
        ).execute()

        # Return the response
        return response

    except HttpError as error:
        print('An error occurred: %s' % error)
        return None

# Function to analyze data and return optimal upload time
def get_optimal_upload_time(api_key, channel_id):
    # Fetch analytics data
    analytics_data = fetch_analytics_data(api_key, channel_id)

    if analytics_data:
        # Calculate engagement rate for each hour
        engagement_rates = {}
        for row in analytics_data['rows']:
            hour = int(row['hour'])
            views = int(row['views'])
            likes = int(row['likes'])
            comments = int(row['comments'])
            engagement_rates[hour] = (likes + comments) / views

        # Get the hour with the highest engagement rate
        optimal_hour = max(engagement_rates, key=engagement_rates.get)

        # Return the optimal upload time
        return optimal_hour

    else:
        return None
