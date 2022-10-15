from functools import wraps
from botlive.random_list import RandomList

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
        self.recomeda = RandomList('recomenda.txt')

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
            await message.channel.send(self.divulgation.get_message(name, f'{name} Boas vindas <3'))

    # Actions

    # Commands

    @commands.command(name='comandos')
    async def cmd_comandos(self, ctx):
        comandos = list(self.commands.keys())
        await ctx.send(
            f'Comandos: {" | ".join(comandos)}'
        )

    @commands.command(name='conduta')
    async def cmd_conduta(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} - O mais importante por aqui é o respeito.
            Conheça o Código de Conduta da nossa comunidade:
             https://github.com/feministech/codigo-de-conduta :)'''
            )

    @commands.command(name='recomenda')
    async def cmd_recomenda(self, ctx):
        await ctx.send(
            f'''{self.recomeda.get_random()}'''
            )

    @commands.command(name='feministech')
    async def cmd_feministech(self, ctx):
        await ctx.send(
                f'''{ctx.author.name} - Feministech é um  grupo de pessoas
                que se identificam no feminino e não binárias que compartilham
                o interesse por lives na Twitch. <3 | Siga e apoie: https://twitter.com/feminis_tech'''
            )
        await ctx.send(
                f'''{ctx.author.name} - Time da twitch: '
                https://www.twitch.tv/team/livecodergirls  |  Twitter:
                https://twitter.com/feminis_tech  |  Instagram:
                https://www.instagram.com/feminis_cat/ | Linkedin:
                https://www.linkedin.com/company/feministech/ | Github
                https://github.com/feministech '''
        )

    @commands.command(name='streamers')
    async def cmd_streamers(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} - Conheça as streamers incríveis
            da nossa comunidade, assista e apoie: https://www.twitch.tv/team/livecodergirls <3'''
        )

    @commands.command(name='caverna')
    async def cmd_caverna(self, ctx):
        await ctx.send(
            '''Uma comunidade voltada para programação em geral com o objetivo de
            ajudar uns aos outros,
            estudar coletivamente, e outros. http://caverna.live/discord PowerUpL
            Por favor, não se esqueça de passar no canal #🆁🅴🅶🆁🅰🆂
            para liberar o acesso á todas as salas do nosso servidor PowerUpR'''
        )

    @commands.command(name='podcast')
    async def cmd_podcast(self, ctx):
        await ctx.send(
            '''Conheça o Feministech Podcast, um podcast feito por uma
            equipe de mulheres maravilhosas que trabalham ou estudam
            tecnologia! | https://anchor.fm/feministech'''
        )

    @commands.command(name='evento')
    async def cmd_evento(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} - No dia 18/10, às 18h, vamos
            ter o evento “Feministalk: Ada Lovelace”.
            Com a @morgannadev como host, então já deixa o
            follow no canal: twitch.tv/morgannadev '''
        )

    @commands.command(name='palestras')
    async def cmd_palestras(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} -
            18h00 Abertura e palestra sobre a Ada Lovelace com a !morganna |
            18h20 “O que gostaria de saber antes de se tornar desenvolvedora” com a !jessica |
            18h55 “Arquitetura de microsserviços” com !nathally |
            19h30 “palestra sobre design de API” com !patricia |
            20h05 !rodadeconversa
            '''
        )

    @commands.command(name='rodadeconversa')
    async def cmd_rodadeconversa(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} - Vamos ter uma conversa sobre como
            usar a comunicação para evoluir tecnicamente e contaremos
            com a presença de !jessica, !patricia, !nathally, !pachi, !kamila.'''
        )

    @commands.command(name='morganna')
    async def cmd_morganna(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} - A Morganna Giovanelli (ela/dela) é Devrel,
            criadora de conteúdo, e cofundadora da Feministech e da Kotlinautas.
            Conheça e acompanhe a Kamila: https://twitter.com/morgannadev'''
        )

    @commands.command(name='kamila')
    async def cmd_kamila(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} - A Kamila Santos (ela/dela) é tech lead e vai
            participar conosco da roda de conversa sobre como usar a
            comunicação para evoluir tecnicamente. Conheça e acompanhe
            a Kamila: https://beacons.ai/kamila_code'''
        )

    @commands.command(name='pachi')
    async def cmd_pachi(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} - A Pachi Parra (ela/dela) é developer advocate e
            vai participar conosco da roda de conversa sobre como usar a
            comunicação para evoluir tecnicamente. Conheça e acompanhe a
            Pachi: https://twitter.com/pachicodes'''
        )

    @commands.command(name='nathally')
    async def cmd_nathally(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} - A Nathally Souza (ela/dela) é tech lead e vai
            conversar conosco sobre arquitetura de microsserviços. E depois
            vai participar conosco da roda de conversa sobre como usar a
            comunicação para evoluir tecnicamente. Conheça e acompanhe a
            Nath: https://twitter.com/nathsouzadev https://instagram.com/nathallyts
            https://www.linkedin.com/in/nathsouza'''
        )

    @commands.command(name='patricia')
    async def cmd_patricia(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} - A Patrícia Villela (ela/dela) é engenheira de software
            e vai conversar conosco sobre design de API. E depois vai participar
            conosco da roda de conversa sobre como usar a comunicação para evoluir
            tecnicamente. Conheça e acompanhe a Patrícia:
            https://twitter.com/patriciaverso'''
        )

    @commands.command(name='jessica')
    async def cmd_jessica(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} - A Jessica Trindade (ela/dela) é desenvolvedora iOS e vai
            conversar conosco sobre coisas que seriam boas de saber antes de se
            tornar uma pessoa desenvolvedora. E depois vai participar conosco da
            roda de conversa sobre como usar a comunicação para evoluir tecnicamente.
            Conheça e acompanhe a Jessica:
            https://www.linkedin.com/in/jessicalinotrindade'''
        )

    @commands.command(name='rainbow')
    async def cmd_rbw(self, ctx):
        await ctx.send('💖💖💖💖💖')
        await ctx.send('💖💖💖💖💖')
        await ctx.send('🧡🧡🧡🧡🧡')
        await ctx.send('🧡🧡🧡🧡🧡')
        await ctx.send('💛💛💛💛💛')
        await ctx.send('💛💛💛💛💛')
        await ctx.send('💚💚💚💚💚')
        await ctx.send('💚💚💚💚💚')
        await ctx.send('💙💙💙💙💙')
        await ctx.send('💙💙💙💙💙')
        await ctx.send('💜💜💜💜💜')
        await ctx.send('💜💜💜💜💜')
