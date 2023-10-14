import discord

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def r(ctx):
    await ctx.send(f'         Сроки разложения отходов естественного происхождения (растительного или животного)!')
    await ctx.send(f'Опавшие листья, мелкие веточки, кожура от банана разлагаются 1-3 месяца!')
    await ctx.send(f'помет животных - 10-30 дней!')
    await ctx.send(f'остатки костей - 5-8 лет!')
    await ctx.send(f'одежда из натуральных тканей  (хлопка, вискозы, льна) разлагается за 2-3 года!')
    await ctx.send(f'обувь из натуральной кожи - 4 года!')
    await ctx.send(f'вощеная бумага - 5 лет!')
    await ctx.send(f'оструганные доски - 4 года!')
    await ctx.send(f'доски, покрытые лаком или окрашенные масляной краской - более 13 лет!')
    await ctx.send(f'автобусный билет исчезает за месяц!')
    await ctx.send(f'         Сроки разложения разных видов мусора!')
    await ctx.send(f'Железная банка - 10 лет!')
    await ctx.send(f'синтетическая одежда - 30-40 лет!')
    await ctx.send(f'фольга, резина, пластик - 100 лет!')
    await ctx.send(f'полиэтилен - 100-200 лет!')
    await ctx.send(f'стекло - более 1000 лет!')




bot.run("import discord

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def r(ctx):
    await ctx.send(f'         Сроки разложения отходов естественного происхождения (растительного или животного)!')
    await ctx.send(f'Опавшие листья, мелкие веточки, кожура от банана разлагаются 1-3 месяца!')
    await ctx.send(f'помет животных - 10-30 дней!')
    await ctx.send(f'остатки костей - 5-8 лет!')
    await ctx.send(f'одежда из натуральных тканей  (хлопка, вискозы, льна) разлагается за 2-3 года!')
    await ctx.send(f'обувь из натуральной кожи - 4 года!')
    await ctx.send(f'вощеная бумага - 5 лет!')
    await ctx.send(f'оструганные доски - 4 года!')
    await ctx.send(f'доски, покрытые лаком или окрашенные масляной краской - более 13 лет!')
    await ctx.send(f'автобусный билет исчезает за месяц!')
    await ctx.send(f'         Сроки разложения разных видов мусора!')
    await ctx.send(f'Железная банка - 10 лет!')
    await ctx.send(f'синтетическая одежда - 30-40 лет!')
    await ctx.send(f'фольга, резина, пластик - 100 лет!')
    await ctx.send(f'полиэтилен - 100-200 лет!')
    await ctx.send(f'стекло - более 1000 лет!')




bot.run("token")")
