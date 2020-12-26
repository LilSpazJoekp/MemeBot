import asyncpraw
import asyncio
import discord
from discord.ext import commands

DISCORD_TOKEN = "NzkxMTU4MTExNzA4MzgxMjA0.X-LFaA.AFXP0fZ_wzc0vJ0RfbovA-CEDA0"
REDDIT_ID = "wNmMRP6W1FhYLw"
REDDIT_SECRET = "dbVtIa7AustTe9QP2Nk2FpEISVXkMA"

REDDIT_USERNAME = "DGIon"
REDDIT_PASSWORD = "ltcaf1964"

bot = commands.Bot(description="test", command_prefix="!")
COMMAND_PREFIX ="!"
reddit = asyncpraw.Reddit(client_id=REDDIT_ID,
                     client_secret=REDDIT_SECRET,
                     user_agent="MemeBot")

    # continued from code above

    # subreddit = await reddit.subreddit("memes")
    # async for submission in subreddit.hot(limit=10):
    #     print(submission.url)
    
#loop = asyncio.get_event_loop()
#loop.run_until_complete(main())

@bot.command()
async def meme(ctx):
    subreddit = await reddit.subreddit("memes")
    async for submission in subreddit.hot(limit=12):    
        await ctx.send(submission.url)

bot.run(DISCORD_TOKEN)