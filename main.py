#dependencies
import discord
from discord.ext import commands, tasks
import random
import time

from config import token

#set intents
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='?', intents=intents)

#generate list
path = "./morbielist.txt"
morbies = [] 
with open(path) as txtfile:
    for line in txtfile:
        morbies.append(line)

#quotes
quotes = ["Highly experimental. Ethically questionable. Very, very, very expensive. And not exactly legal. Oh, and it has to be done in international waters.","🦇 I feel a kinship with these creatures. They would tear anyone else apart, but they welcome me. Like a brother. 🦇","If you quote The Notebook, I'm going to turn and hobble very slowly in the other direction.","I've made a terrible mistake, Milo. You've never made one like this before.","Deadly to bats, lethal to humans.","It’s impressive, don’t you think? Vampire bats weigh almost nothing, but they can down a creature nearly ten times their size.","Like the original Spartans, we are the few against the many.","We have to push the boundaries, take the risks. Without that, there is no science. No medicine. No breakthroughs at all.","You know, the whole near death thing is very, very chic. I read it in Cosmo. Do they still make Cosmo? I don’t know."," As a result of my procedure, I have an overpowering urge to consume blood. Human blood.\nIn certain respects, I have succeeded far beyond anything I could have imagined. For the first time in my entire life, I feel good.\nYesterday, I could barely walk. Today, I don’t know what I’m capable of.","I’m sorry. I’m starting to get hungry. And you don’t want to see me when I’m hungry.","I've developed a form of echolocation. Bat radar, for the uninitiated.","“Crazy” isn’t a term that I would use, detective. Unorthodox, maybe. But I’d do just about anything to save a life.","Hello, Milo"]


#start up event
@bot.event
async def on_ready():
    channel = bot.get_channel(975271554424377384)
    await channel.send("It's Morbin Time!")
    loop_quotes.start()

#command to select a movie    
@bot.command(brief='Randomly chooses a morbie from the list', description='Randomly chooses a morbie from the list')
async def morbie(ctx):
    await ctx.send('Stand back! I am beginning to Morb!')
    choice = random.choice(morbies)
    await ctx.send(f'Milo, your morbie is {choice}')

#command to show the list
@bot.command(brief='Shows the morbie list in full', description='Shows the morbie list in full')
async def morbielist(ctx):
    
    await ctx.send("".join(morbies))

#command to add to the list
@bot.command(brief='Adds a morbie to the list', description='Adds a morbie to the list')
async def add(ctx, *, content):
    morbies.append(content+" - "+str(ctx.author)+'\n')
    with open(path,'w') as txtfile:
         txtfile.write(''.join(morbies))
    await ctx.send(f"I've added {content} to the list Milo")

#command to delete from the list
@bot.command(brief='Deletes a morbie from the list', description='Deletes a morbie from the list')
async def delete(ctx, *, content):
    try:
        strmovie = content+'\n'
        morbies.remove(strmovie)
        with open(path,'w') as txtfile:
            txtfile.write(''.join(morbies))
        await ctx.send(f'{content} removed from the list Milo')
    except:
        await ctx.send(f"{content} isn't on the list Milo...")

@tasks.loop(hours=4)
async def loop_quotes():
    choice = random.choice(quotes)
    channel = bot.get_channel(975271554424377384)
    await channel.send(choice)


bot.run(token)