from functools import wraps

from twitchio.ext import commands

from .config import BOTS, STREAMERS, TOKEN, USERNAME
from .divulgation import Divulgation
from .one_per_live import OnePerLive


def run():
    bot = Bot()
    bot.run()


def is_mod(f):
    @wraps(f)
    async def wrapper(self, ctx):
        if ctx.author.is_mod:
            await f(self, ctx)
    return wrapper


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(irc_token=TOKEN, nick=USERNAME, prefix='!', initial_channels=STREAMERS)

        self.divulgation = Divulgation('divulgation.ini')
        self.hello = OnePerLive('hello.tmp')

    # Events

    async def event_ready(self):
        self.channel = self.get_channel(self.nick)

        print(f'Ready | {self.nick}')

    async def event_message(self, message):
        await self.handle_hello(message)
        await self.handle_commands(message)

    async def event_command_error(self, ctx, error):
        print(error)

    # Handles

    async def handle_hello(self, message):
        name = message.author.name
        if message.content and name not in BOTS and self.hello.add(name):
            await message.channel.send(self.divulgation.get_message(name, f'Olá {name}! Boas vindas <3'))

    # Actions

    # Commands

    @commands.command(name='comandos')
    async def cmd_comandos(self, ctx):
        comandos = str(list(self.commands.keys()))[1:-1]
        await ctx.send(
            f'Comandos: {comandos}'
        )

    @commands.command(name='conduta')
    async def cmd_conduta(self, ctx):
        await ctx.send(f'{ctx.author.name} - O mais importante por aqui é o respeito. '
        'Conheça o Código de Conduta da nossa comunidade: https://github.com/feministech/codigo-de-conduta :)')

    @commands.command(name='feministech')
    async def cmd_feministech(self, ctx):
        await ctx.send(f'{ctx.author.name} - Feministech é um  grupo de pessoas que se identificam no feminino e não binárias que compartilham o interesse por lives na Twitch. <3 | Siga e apoie: https://twitter.com/feminis_tech')

    @commands.command(name='streamers')
    async def cmd_streamers(self, ctx):
        await ctx.send(f'{ctx.author.name} - Conheça as streamers incríveis da nossa comunidade, assista e apoie: https://www.twitch.tv/team/livecodergirls <3')

    @commands.command(name='mandavaga')
    async def cmd_mandavaga(self, ctx):
        await ctx.send(f'{ctx.author.name} -Viu uma vaga '
        'legal da área de tecnologia? Mande seu PR aqui'
        ' e compartilhe com outras pessoas: '
        'https://github.com/feministech/mandavaga <3')

    @commands.command(name='linkedin')
    async def cmd_linkedin(self, ctx):
        await ctx.send(f'{ctx.author.name} - Compartilhe '
        'seu LinkedIn e adicione outras pessoas da '
        'comunidade. Lembre-se de respeitar as pessoas.'
        ' Adicione aqui: https://docs.google.com/spreadsheets/d/1o0XolWlW44VJ2eDL6xhc-Gb5iYvQvyoG8N4DSpeBcaE/edit?usp=sharing <3')

    @commands.command(name='sociais')
    async def cmd_sociais(self, ctx):
        await ctx.send(f'{ctx.author.name} - Time da twitch: '
        'https://www.twitch.tv/team/livecodergirls  |  Twitter:'
        ' https://twitter.com/feminis_tech  |  Instagram: '
        'https://www.instagram.com/feminis_cat/')

    @commands.command(name='redes')
    async def cmd_redes(self, ctx):
        await ctx.send(f'{ctx.author.name} - Time da twitch: '
        'https://www.twitch.tv/team/livecodergirls  |  Twitter: '
        'https://twitter.com/feminis_tech  |  Instagram: '
        'https://www.instagram.com/feminis_cat/')

    @commands.command(name='caverna')
    async def cmd_caverna(self, ctx):
        await ctx.send(
            'Uma comunidade voltada para programação em geral com o objetivo de ajudar uns aos outros, '
            'estudar coletivamente, e outros. http://caverna.live/discord PowerUpL '
            'Por favor, não se esqueça de passar no canal #🆁🅴🅶🆁🅰🆂'
            'para liberar o acesso á todas as salas do nosso servidor PowerUpR'
        )

    @commands.command(name='podcast')
    async def cmd_podcast(self, ctx):
        await ctx.send(
            'Conheça o Feministech Podcast, um podcast feito por uma '
            'equipe de mulheres maravilhosas que trabalham ou estudam '
            'tecnologia! | https://anchor.fm/feministech'
        )
