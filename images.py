import random
from discord.ext import commands
import discord
import asyncpraw
from settings import REDDIT_APP_ID, REDDIT_APP_SECRET, REDDIT_ENABLED_MEME_SUBREDDITS
import logging

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
for logger_name in ("asyncpraw", "asyncprawcore"):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)


# class MemeBot(commands.AutoShardedBot):
#     def __init__(self):
#         self.reddit = ...

class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reddit = None
        if REDDIT_APP_ID and REDDIT_APP_SECRET:
            self.reddit = asyncpraw.Reddit(client_id = REDDIT_APP_ID, 
            client_secret = REDDIT_APP_SECRET, 
            user_agent = 'MemeBot:%s:1.0' % REDDIT_APP_ID)

    @commands.command()
    async def memes(self, ctx, subreddit: str=""):
        async with ctx.channel.typing():
            if self.reddit:
                subreddit = await self.reddit.subreddit(REDDIT_ENABLED_MEME_SUBREDDITS[0])
                # if subreddit in REDDIT_ENABLED_MEME_SUBREDDITS:
                #     chosen_subreddit = subreddit
                # else:
                #     list_memes = "\n".join(REDDIT_ENABLED_MEME_SUBREDDITS)
                #     await ctx.send("Please choose a subreddit of the following:\n %s" % (list_memes))

                submissions = [submission async for submission in subreddit.hot() if not submission.stickied]
                post_to_pick = random.randint(1,10)
                submission = submissions[post_to_pick]
                await ctx.send(submission.url)

    @commands.command()
    async def meme(self, ctx, subreddit: str=""):
        async with ctx.channel.typing():
            subreddit = await self.reddit.subreddit(subreddit)
            submissions = [submission async for submission in subreddit.hot() if not submission.stickied]
            post_to_pick = random.randint(1, 10)
            submission = submissions[post_to_pick]
            await ctx.send(submission.title)
            await ctx.send(submission.url)

    @commands.command()
    async def lol(self, ctx):
        async with ctx.channel.typing():
            subreddit = await self.reddit.subreddit("leagueofmemes")
            submissions = [submission async for submission in subreddit.hot() if not submission.stickied]
            post_to_pick = random.randint(1, 10)
            submission = submissions[post_to_pick]
            await ctx.send(submission.url)

    @commands.command()
    async def prequelmemes(self, ctx):
        async with ctx.channel.typing():
            subreddit = await self.reddit.subreddit("prequelmemes")
            submissions = [submission async for submission in subreddit.hot() if not submission.stickied]
            post_to_pick = random.randint(1, 10)
            submission = submissions[post_to_pick]
            await ctx.send(submission.url)

    @commands.command()
    async def CoronavirusMemes(self, ctx):
        async with ctx.channel.typing():
            subreddit = await self.reddit.subreddit("CoronavirusMemes")
            submissions = [submission async for submission in subreddit.hot() if not submission.stickied]
            post_to_pick = random.randint(1, 10)
            submission = submissions[post_to_pick]
            await ctx.send(submission.url)

def setup(bot):
    bot.add_cog(Images(bot))