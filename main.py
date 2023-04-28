import discord
from discord import file
from discord.ext import commands
import json
import os
import keep_alive
import asyncio

with open('setting.json', "r", encoding="utf8") as file:
    data = json.load(file)

intent = discord.Intents.all()
intent.members = True
intent.messages = True

bot = commands.Bot(command_prefix='%', intents=intent)


#添加事件
@bot.event
async def on_ready():
    print("I am running on " + bot.user.name)
    print(f"With the ID: {bot.user.id}")
    print('Bot is ready to be used')
    print("   ")
    #takenGuild = bot.get_guild(1081912383770988614)
    #print(takenGuild)
    print(bot.user.name + "有管理權的伺服器")
    for guild in bot.guilds:
        print(f"伺服器名稱: {guild}")
        print(f"伺服器ID: {guild.id}")


@bot.command()
async def reload(ctx, extension):
    await bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Reloaing {extension} done!!')


# listdir可列出./cmds底下的文件有哪些 ./是相對路徑
#for file_name in os.listdir('./cmds'):
#    if file_name.endswith('.py'):
#        bot.load_extension(f'cmds.{file_name[:-3]}')


async def load():
    for filename in os.listdir('./cmds'):
        if filename.endswith('.py'):
            await bot.load_extension(f"cmds.{filename[:-3]}")


async def main():
    print("   ")
    await load()


if __name__ == "__main__":
    asyncio.run(main())
    keep_alive.keep_alive()
    bot.run(data['TOKEN'])
