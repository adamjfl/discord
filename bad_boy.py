import discord
from discord.ext import commands
from discord import app_commands
from discord.ext.commands import hybrid_command

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    await bot.tree.sync()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.lower() == 'hi':
        await message.reply('Hello!')
    await bot.process_commands(message)

@bot.tree.command(name="ping", description="Replies with pong")
async def ping(interaction: discord.Interaction, user: discord.User, member: discord.Member = None):
    if member:
        await interaction.response.send_message(f"Pong! {member.mention}")
    else:
        await interaction.response.send_message(f"Pong! {user.name}")

@bot.command()
async def hii(ctx, user: discord.User):
    em = discord.Embed(
                    title="Hello",
                    description=f"Hello, {user.name}!",
                    color=0x56FF11,
                    timestamp=ctx.message.created_at
                    )
    em.add_field(name="User ID", value=user.id, inline=False)
    em.add_field(name="User ID", value=user.id, inline=False)
    em.add_field(name="User ID", value=user.id, inline=True)
    em.add_field(name="User ID", value=user.id, inline=True)
    em.set_thumbnail(url=user.avatar.url)
    em.set_image(url="https://i.pinimg.com/736x/a0/8d/73/a08d73d745786a626672813650a013f4.jpg")
    em.set_author(name=user.name, icon_url=user.avatar.url, url="https://i.pinimg.com/736x/a0/8d/73/a08d73d745786a626672813650a013f4.jpg")
    em.set_footer(text="Footer", icon_url=user.avatar.url)
    await ctx.reply(embed=em)

@bot.hybrid_command(name="hi", description="Replies with hi")
async def hi(ctx):
    if ctx.interaction:
        await ctx.interaction.response.send_message('Hello!')
    else:
        await ctx.reply('Hello!')

bot.run("your_bot_token")
