import os

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN", False)

# Reddit Configurtion
REDDIT_APP_ID = os.getenv("REDDIT_APP_ID", False)
REDDIT_APP_SECRET = os.getenv("REDDIT_APP_SECRET", False)

REDDIT_ENABLED_MEME_SUBREDDITS = [
    'memes',
    'funny',
    'prequelmemes',
    'leagueofmemes',
    'CoronavirusMemes'
]