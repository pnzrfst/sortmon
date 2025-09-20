import tweepy 
import os
from dotenv import load_dotenv
from pokemon_handler import getRandomPokemon
from io import BytesIO
import requests

load_dotenv(); 

authInfos = {
    'api_key' : os.getenv('API_KEY'),
    'api_key_secret' : os.getenv('API_KEY_SECRET'),
    'bearer_token' : os.getenv('BEARER_TOKEN'),
    'access_token' : os.getenv('ACCESS_TOKEN'),
    'access_token_secret' : os.getenv('ACCESS_TOKEN_SECRET')
}

client = tweepy.Client(authInfos['bearer_token'], authInfos['api_key'], authInfos['api_key_secret'], authInfos['access_token'], authInfos['access_token_secret']);

print(f"{authInfos}")

auth = tweepy.OAuth1UserHandler(
    authInfos['api_key'], 
    authInfos['api_key_secret'], 
    authInfos['access_token'], 
    authInfos['access_token_secret']
);

api = tweepy.API(auth)

tweet_data = getRandomPokemon();


tweet_content = tweet_data[0]["content"];

tweet_string = "\n".join([f"{key}: {value}" for key, value in tweet_content.items()])

tweet_image = tweet_data[0]["sprite_url"];
response = requests.get(tweet_image);
tweet_image_bytes = BytesIO(response.content);


media = api.media_upload(filename="pokemon.png", file = tweet_image_bytes);


client.create_tweet(text=tweet_string, media_ids=[media.media_id]);