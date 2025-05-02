from googleapiclient.discovery import build
import json

def get_youtube_data():
    creds = json.load(open('config/credentials.json'))['youtube']
    youtube = build('youtube', 'v3', developerKey=creds['145905912120-7go176t3q7silraree3pidi6gmqmdqo2.apps.googleusercontent.com'])
    request = youtube.videos().list(part="snippet,statistics", chart="mostPopular", regionCode="BR", maxResults=10)
    response = request.execute()
    return response
