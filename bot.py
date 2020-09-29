import discord
from discord.ext.commands import Bot
from datetime import datetime

client = Bot(command_prefix='PREFIX', case_insensitive=True)
client.remove_command('help')

status = {'000000000000000000': {'status': "online"}}

@client.event
async def on_ready():
    print('___'*20)
    print(f'Online --> {client.user.name}')
    print(f'ID: {client.user.id}')
    print(f'Members: {str(len(set(client.get_all_members())))}')
    print(f"https://discordapp.com/api/oauth2/authorize?client_id="+str(client.user.id)+"&permissions=8&scope=bot")
    print('___' * 20)
    print(f"""
    > Initialized!

""")

@client.command()
async def setarimg(ctx, *, link):
    if not ctx.guild.get_role(ID ROLE) in ctx.author.roles:
        return await ctx.send('`You are not allowed to use this command.`')
    global image
    image = link
    embed = discord.Embed(title='Image set successfully.', color=0x00000)
    embed.set_image(url=image)
    await ctx.send(embed=embed)

@client.command()
async def enviar(ctx, *, msg):
    if not ctx.guild.get_role(ID ROLE) in ctx.author.roles:
        return await ctx.send('`You are not allowed to use this command.`')
    embed = discord.Embed(title=f'Server Notification: {ctx.guild.name}',description=f'⠀⠀\n**{msg}**' ,color=0x00000)
    embed.set_thumbnail(url='LINK THUMBNAIL')
    embed.set_image(url="")
    embed.set_image(url=image)
    embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
    x = 0
    for member in ctx.guild.members:
        status[member.id] = {'status': "{}".format(member.status)}
        if not status[member.id]['status'] == "offline":
            try:
                await member.send(embed=embed)
                print(f'Message sent to {member} | Status: {member.status}')
                x+=1
            except:
                pass
    await ctx.send(f'`Message sent for {x} to {len(ctx.guild.members)}`')


if __name__ == '__main__':
    client.run("TOKEN", bot=True)