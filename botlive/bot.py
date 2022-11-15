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
            f'''{ctx.author.name} - No dia 20/11, às 14h
            vamos ter o evento “Maratona Feministech 2022”.
            Com a @gikapassuti como host, então já deixa o
            follow no canal: twitch.tv/gikapassuti
            '''
        )

    @commands.command(name='palestras')
    async def cmd_palestras(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} -
            14h00 Abertura !gika |
            14h10 UX com a !bia |
            15h10 QA com a !gika |
            15h40 Banco de dados com a !ka |
            16h10 Backend com a !nath |
            17h10 Frontend com a !natalia |
            18h10 QA com a !gika |
            18h40 Agradecimento
            '''
        )

    @commands.command(name='gika')
    async def cmd_gika(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} - A Gisele Passuti (ela/dela)
            é DevRel na db1group,
            coordenadora na @feministech, com coraçãozinho
            na qualidade de software. Conheça e acompanhe a
            Gika: https://twitter.com/gikapassuti
            '''
        )

    @commands.command(name='bia')
    async def cmd_bia(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} - A Bianca Peninga (ela/dela)
            é designer. Conheça e acompanhe a
            Bia: https://linkedin.com/in/biancapeninga/
            '''
        )

    @commands.command(name='ka')
    async def cmd_ka(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} - A Kamila Santos (ela/dela) é
            Tech lead na zup innovation. Conheça e acompanhe a
            Kamila: https://beacons.ai/kamila_code'''
        )

    @commands.command(name='nath')
    async def cmd_nath(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} - A Nathally Souza (ela/dela) é tech lead e vai
            conversar conosco sobre arquitetura de microsserviços. E depois
            vai participar conosco da roda de conversa sobre como usar a
            comunicação para evoluir tecnicamente. Conheça e acompanhe a
            Nath: https://twitter.com/nathsouzadev https://instagram.com/nathallyts
            https://www.linkedin.com/in/nathsouza'''
        )

    @commands.command(name='natalia')
    async def cmd_natalia(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} - A Natália (ela/dela) é
            Desenvolvedora front-end e artista de CSS.
            Conheça e acompanhe a Natália:
            https://www.linkedin.com/in/natalia-f-da-silva/ |
            https://www.tiktok.com/@nataliafdev'''
        )

    @commands.command(name='ReveloCommunity')
    async def cmd_ReveloCommunity(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} - A Revelo Community é uma
            iniciativa da Revelo que tem como objetivo elevar
            as carreiras dos profissionais de tecnologia
            oferecendo conteúdo de qualidade sobre o mundo tech
            por meio das redes sociais, podcasts, eventos e conteúdos
            no blog, os quais você pode contribuir e ser remunerada
            em dólares. Para saber mais, acesse o Instagram
            @revelocobrazil ou o nosso blog https://community.revelo.com'''
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
