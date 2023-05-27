import requests
import json

def suggest_content_topics():
    # First, gather user feedback and engagement data
    feedback_data = gather_user_feedback()
    engagement_data = gather_engagement_data()

    # Combine the data to determine relevant content topics
    relevant_topics = analyze_data(feedback_data, engagement_data)

    # Return the relevant topics to the user
    return relevant_topics

def gather_user_feedback():
    # Make a request to gather user feedback from a survey or other source
    response = requests.get("http://example.com/user/feedback")
    feedback_data = json.loads(response.text)

    # Process the feedback data and return it as a dictionary
    processed_feedback = {}
    for feedback in feedback_data:
        topic = feedback['topic']
        rating = feedback['rating']
        if topic in processed_feedback:
            processed_feedback[topic].append(rating)
        else:
            processed_feedback[topic] = [rating]

    return processed_feedback

def gather_engagement_data():
    # Make a request to gather engagement data from YouTube's API
    response = requests.get("https://www.googleapis.com/youtube/v3/analytics/reports")
    engagement_data = json.loads(response.text)

    # Process the engagement data and return it as a dictionary
    processed_engagement = {}
    for data in engagement_data:
        topic = data['topic']
        views = data['views']
        likes = data['likes']
        comments = data['comments']
        processed_engagement[topic] = {'views': views, 'likes': likes, 'comments': comments}

    return processed_engagement

def analyze_data(feedback_data, engagement_data):
    # Use a combination of feedback and engagement data to determine relevant topics
    relevant_topics = []
    for topic in feedback_data:
        ratings = feedback_data[topic]
        total_rating = sum(ratings)
        if topic in engagement_data:
            engagement = engagement_data[topic]
            views = engagement['views']
            likes = engagement['likes']
            comments = engagement['comments']
            engagement_score = views + (likes * 2) + (comments * 3)
            relevance_score = total_rating * engagement_score
            relevant_topics.append({'topic': topic, 'score': relevance_score})

    # Sort the relevant topics by relevance score and return the top 3
    sorted_topics = sorted(relevant_topics, key=lambda topic: topic['score'], reverse=True)
