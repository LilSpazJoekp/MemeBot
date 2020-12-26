import asyncpraw
import random
from discord.ext import commands
import discord

DISCORD_TOKEN = "NzkxMTU4MTExNzA4MzgxMjA0.X-LFaA.AFXP0fZ_wzc0vJ0RfbovA-CEDA0"
REDDIT_ID = "wNmMRP6W1FhYLw"
REDDIT_SECRET = "dbVtIa7AustTe9QP2Nk2FpEISVXkMA"

bot = commands.Bot(description="test", command_prefix="!")

reddit = asyncpraw.Reddit(client_id=REDDIT_ID,
                     client_secret=REDDIT_SECRET,
                     user_agent='MemeBot')

@bot.command()
async def meme(ctx):
    subreddit = await reddit.subreddit("memes")
    submissions = [submission async for submission in subreddit.hot() if not submission.stickied]
    post_to_pick = random.randint(1, 10)
    submission = submissions[post_to_pick]
    await ctx.send(submission.url)

bot.run(DISCORD_TOKEN) 