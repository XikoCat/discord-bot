import discord
import os

from discord.ext import commands, tasks
from discord.ext.commands import Context
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv("discord_token")  # Get the API token from the .env file.
PREFIX = os.getenv("command_prefix")  # Get the command prefix from the .env file.
if PREFIX is None:
    PREFIX = "!"
print(f"prefix: {PREFIX}")

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

cogs = ["fun", "nhentai", "debug", "mc_server", "content_follow"]
for cog in cogs:
    bot.load_extension(cog)

# bot = discord.Client(intents=intents)

##########################################################################
##############################  NORMAL  ##################################
##############################   BOT    ##################################
##############################   STUFF  ##################################
##########################################################################


@bot.event
async def on_ready():
    print("Running!\nActive in:")
    for guild in bot.guilds:
        # for channel in guild.text_channels:
        # if str(channel) == "general":
        # await channel.send("Bot Activated..")
        # await channel.send(file=discord.File("giphy.png"))
        print(f" - {guild.name} | Member Count : {guild.member_count}")


@bot.event
async def on_message(message):
    # bot.process_commands(msg) is a couroutine that must be called here since we are overriding the on_message event
    await bot.process_commands(message)

    message_string = str(message.content).lower()
    if message_string.find("tetr.io") != -1 or message_string.find("tetris") != -1:
        await message.channel.send(
            "Alguém falou em **T E T R I S**?\n⚡⚡⚡!!!Thunder!!!⚡⚡⚡"
        )

    if message_string.find("moura") != -1:
        await message.channel.send(
            "Why!? Why would you bring that bloody cursed word upon this land!"
        )

    if message_string in ["swear_word1", "swear_word2"]:
        await message.channel.purge(limit=1)


@bot.event
async def on_member_join(member):
    for channel in member.guild.text_channels:
        if str(channel) == "general":
            await channel.send(f"Welcome to the Server {member.name}!!")


if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)
