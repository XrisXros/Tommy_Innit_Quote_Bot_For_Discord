from dotenv import load_dotenv
import random
import os
import discord
import json

load_dotenv()
TOKEN = os.getenv('TOKEN')
PREFIX = os.getenv("PREFIX")

with open("Tommy_Innit_Quote_Bot_For_Discord\quotes.json") as json_file:
    quotes = json.load(json_file)

client = discord.Client()

def remove_prefix(text, prefix):
    return text[text.startswith(prefix) and len(prefix):]

@client.event
async def on_ready():
    print('Bot Online : {0.user}'.format(client))

@client.event
async def on_message(message):
    if not message.content.startswith(PREFIX) or message.author.bot:
        return

    args = remove_prefix(message.content, PREFIX).strip().split()
    command = args.pop(0).lower()

    if command == "random":
        randomqgen = random.randint(0,8)
        file = discord.File("{filename}".format(filename = quotes["quotes"][randomqgen]["link"]), filename = quotes["quotes"][randomqgen]["link"])
        embed=discord.Embed(title="Quote:", description=quotes["quotes"][randomqgen]["quote"], color=0x7301af)
        embed.set_footer(text="do ^random for another! 🔥 ")
        await message.channel.send(embed = embed, file = file)

    if command == "help":
        embed=discord.Embed(title="Help", description="(cuz you apparently need it)", color=0x7301af)
        embed.add_field(name="^help :upside_down:", value="help me :(", inline=False)
        embed.add_field(name="^random :game_die:", value="generates a random quote from your's truly", inline=False)
        embed.add_field(name="^quotebook :notebook_with_decorative_cover:", value="generates an entire list of all of the quotes", inline=False)
        embed.add_field(name="^seek :mag:", value="lets you look for a quote (must include the quote number directly after) e.g ^seek 3", inline=False)
        await message.channel.send(embed=embed)

    if command == "quotebook":
        embed=discord.Embed(title="Quote Book", description="-From your's turly", color=0x7301af)
        embed.add_field(name="No. 1 Just killed a woman feeling good.", value=":)", inline=False)
        embed.add_field(name="No. 2 Everyone Is Still Looking For Women.", value="...what are you doing then???", inline=False)
        embed.add_field(name="No. 3 I don't date girls", value="Okay", inline=False)
        embed.add_field(name="No. 4 *The Twitch Prime Song Feat. Tommy Innit*", value="Sorry, couldn't think of a desc. here, im busy vibing", inline=False)
        embed.add_field(name="No. 5 I don't smoke", value="It's bad for you kids", inline=False)
        embed.add_field(name="No. 6 I'd really rather not", value="understandable", inline=False)
        embed.add_field(name="No. 7 27 emeralds for free", value="Profit anyone?", inline=False)
        embed.add_field(name="No. 8 Oh shh...", value="What happened?", inline=False)
        embed.add_field(name="No. 9 Oof", value="Tragic backstory...", inline=False)
        await message.channel.send(embed=embed)

    if command == "seek": 
        file = discord.File("{filename}".format(filename = quotes["quotes"][int(args[0])]["link"]), filename = quotes["quotes"][int(args[0])]["link"])
        embed=discord.Embed(title="Quote:", description=quotes["quotes"][int(args[0])]["quote"], color=0x7301af)
        embed.set_footer(text="do ^seek for another! 🔥 ")
        await message.channel.send(embed = embed, file = file)

client.run(TOKEN)