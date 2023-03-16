import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import boto3
from datetime import datetime

def lambda_handler(event, context):
   client_id = os.environ.get('client_id')
   client_secret = os.environ.get('client_secret')
   
   client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
   sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
   playlists = sp.user_playlists('spotify')
   
   playlist_link = 'https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF'
   playlist_URI = playlist_link.split("/")[-1].split("?")[0]
   spotify_data = sp.playlist_tracks(playlist_URI)
   
   filename = 'spotify_raw_' + str(datetime.now()) + '.json'
   client = boto3.client('s3')
   client.put_object(
      Bucket='spotify-etl-project-leo',
      Key='raw_data/to_processed/' + filename,
      Body=json.dumps(spotify_data)
      )
