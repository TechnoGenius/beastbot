# Made by ScriptingVoid

import discord
import random
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import youtube_dl

bannedwords = []
players = {}


client = commands.Bot(command_prefix="!")
@client.event
async def on_ready():
    print("Getting ready...")
    print("I am running on " + client.user.name)
    print("With the ID: " + client.user.id)
    await client.change_presence(game=discord.Game(name='Superhero City'))
    #channel43=client.get_channel('519344401110138881')
    #await client.send_message(channel43, "@everyone")
    #em = discord.Embed(
        #title = "**Update Log V0.0.2.4**",
        #description = """
        #New updates:
        #||:|| Removed the announce command.
        #||:|| Removed the setrule command.
        #||:|| Added version to name.
        #||:|| Fixed checking perms.

        #Future updates:
        #||:|| Music command.
        #||:|| Ban command.
        #||:|| Chat filter.
        #""",
        #colour = discord.Colour.gold()
    #)
    #em.set_author(name="Beast Administration Announcement", icon_url="https://cdn.discordapp.com/attachments/514887805386883076/519991776602226698/beastgamesbeast1.png")
    #await client.send_message(channel43, embed=em)

@client.command(pass_context=True)
async def dm(ctx, member: discord.Member,*,msg:str):
    if "518842438081839142" in [roles.id for roles in ctx.message.author.roles] or "518844297366208524" in [roles.id for roles in ctx.message.author.roles]:
        await client.send_message(member, msg)
        em = discord.Embed(
            title = "Message has been sent to the user!",
            colour = discord.Colour.green()
        )
        await client.send_message(ctx.message.channel, embed=em)
    else:
        await client.send_typing(ctx.message.channel)
        await asyncio.sleep(1)
        em = discord.Embed(
            title = "Sorry, but you don't have perms to use cmd!",
            colour = discord.Colour.red()
        )
        await client.send_message(ctx.message.channel, embed=em)

@client.command(pass_context = True)
async def cmds(ctx):
    if "518842438081839142" in [roles.id for roles in ctx.message.author.roles] or "518844297366208524" in [roles.id for roles in ctx.message.author.roles]:
        em = discord.Embed(
                title = """
                Commands:""",
                description = """
                !clear [int] - Clears the int number of messages.
                !dm [member] [message] - Sends message to the member.
                !kick [member] - Works for everyone except the admins. Kicks the selected member.
                !askbeast [message] - The client will answer the message with a yes, maybe, or no.
                !help - Displays a the list of commands you are able to use.
                """,
                colour = discord.Colour.gold()
        )
        em.set_author(name="Private message from Beast client Administration!", icon_url="https://cdn.discordapp.com/attachments/514887805386883076/519991776602226698/beastgamesbeast1.png")
        await client.send_message(ctx.message.author, embed=em)
    else:
        em = discord.Embed(
                title = """
                Commands:""",
                description = """
                !askbeast [message] - The client will answer the message with a yes, maybe, or no.
                !help - Displays a the list of commands you are able to use.
                """,
                colour = discord.Colour.gold()
        )
        em.set_author(name="Private message from Beast client Administration!", icon_url="https://cdn.discordapp.com/attachments/514887805386883076/519991776602226698/beastgamesbeast1.png")
        await client.send_message(ctx.message.author, embed=em)

@client.command(pass_context = True)
async def clear(ctx, number):
    if "518842438081839142" in [roles.id for roles in ctx.message.author.roles] or "518844297366208524" in [roles.id for roles in ctx.message.author.roles]:
        number = int(number)
        if number > 250:
            await client.send_typing(ctx.message.channel)
            await asyncio.sleep(1)
            em = discord.Embed(
                title = "Sorry, but the max ammount you can clear is 250.",
                colour = discord.Colour.red()
            )
            await client.send_message(ctx.message.channel, embed=em)
            return
        actualnum = number + 1
        counter = 0
        async for x in client.logs_from(ctx.message.channel, limit = actualnum):
            if counter < actualnum:
                await client.delete_message(x)
                counter += 1
                await asyncio.sleep(.0000000000000000000000000000000000001)
            if counter + 1 == actualnum:
                await client.send_typing(ctx.message.channel)
                await asyncio.sleep(1)
                em = discord.Embed(
                    title = "Messages cleared: " + str(counter),
                    colour = discord.Colour.green()
                )
                await client.send_message(ctx.message.channel, embed=em)
    else:
        await client.send_typing(ctx.message.channel)
        await asyncio.sleep(1)
        em = discord.Embed(
            title = "Sorry, but you don't have perms to use cmd!",
            colour = discord.Colour.red()
        )
        await client.send_message(ctx.message.channel, embed=em)

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()


@client.command(pass_context=True)
async def kick(ctx, userName: discord.User):
    if "518842438081839142" in [roles.id for roles in ctx.message.author.roles] or "518844297366208524" in [roles.id for roles in ctx.message.author.roles]:
        await client.kick(userName)
        await client.send_typing(ctx.message.channel)
        await asyncio.sleep(1)
        em = discord.Embed(
            title = "Successfully kicked the user!",
            colour = discord.Colour.green()
        )
        await client.send_message(ctx.message.channel, embed=em)
    else:
        await client.send_typing(ctx.message.channel)
        await asyncio.sleep(1)
        em = discord.Embed(
            title = "Sorry, but you don't have the perms to use the cmd!",
            colour = discord.Colour.red()
        )
        await client.send_message(ctx.message.channel, embed=em)

@client.command(pass_context=True)
async def askbeast(ctx,*,msg:str):
    em1 = discord.Embed(
        title = "It is certain",
        colour = discord.Colour.dark_green()
    )
    em2 = discord.Embed(
        title = "It is decidedly so",
        colour = discord.Colour.dark_green()
    )
    em3 = discord.Embed(
        title = "Without a doubt",
        colour = discord.Colour.dark_green()
    )
    em4 = discord.Embed(
        title = "Yes, definitely",
        colour = discord.Colour.dark_green()
    )
    em5 = discord.Embed(
        title = "You may rely on it",
        colour = discord.Colour.dark_green()
    )
    em6 = discord.Embed(
        title = "As I see it, yes",
        colour = discord.Colour.dark_green()
    )
    em7 = discord.Embed(
        title = "Most likely",
        colour = discord.Colour.dark_green()
    )
    em8 = discord.Embed(
        title = "Outlook good",
        colour = discord.Colour.dark_green()
    )
    em9 = discord.Embed(
        title = "Yes",
        colour = discord.Colour.dark_green()
    )
    em10 = discord.Embed(
        title = "Signs point to yes",
        colour = discord.Colour.dark_green()
    )
    em11 = discord.Embed(
        title = "Reply hazy try again",
        colour = discord.Colour.dark_blue()
    )
    em12 = discord.Embed(
        title = "Ask again later",
        colour = discord.Colour.dark_blue()
    )
    em13 = discord.Embed(
        title = "Better not tell you now",
        colour  = discord.Colour.dark_blue()
    )
    em14 = discord.Embed(
        title = "Cannot predict now",
        colour = discord.Colour.dark_blue()
    )
    em15 = discord.Embed(
        title = "Concentrate and ask again",
        colour = discord.Colour.dark_blue()
    )
    em16 = discord.Embed(
        title = "Don't count on it",
        colour = discord.Colour.dark_red()
    )
    em17 = discord.Embed(
        title = "My reply is no",
        colour = discord.Colour.dark_red()
    )
    em18 = discord.Embed(
        title = "My sources say no",
        colour = discord.Colour.dark_red()
    )
    em19 = discord.Embed(
        title = "Outlook not so good",
        colour = discord.Colour.dark_red()
    )
    em20 = discord.Embed(
        title = "Very doubtful",
        colour = discord.Colour.dark_red()
    )
    await client.send_typing(ctx.message.channel)
    await asyncio.sleep(1)
    await client.send_message(ctx.message.channel, embed=random.choice([em1,
                                                                    em2,
                                                                    em3,
                                                                    em4,
                                                                    em5,
                                                                    em6,
                                                                    em7,
                                                                    em8,
                                                                    em9,
                                                                    em10,
                                                                    em11,
                                                                    em12,
                                                                    em13,
                                                                    em14,
                                                                    em15,
                                                                    em16,
                                                                    em17,
                                                                    em18,
                                                                    em19,
                                                                    em20]))
    
client.run("NTE4ODkyMTk2MDM3MDAxMjI3.DuXavw.47e6RE97qN20l9x-5A2_JJcwGEs")