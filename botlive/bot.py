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
            f'''{self.recomeda.get_random()} -{ctx.author.name} '''
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
            f'''{ctx.author.name} No dia 28/05, das 10h00 às 12h00, vamos
            ter o evento “Feministalk: Como se tornar uma Feministreamer”
            para compartilharmos sobre como começar a fazer lives na Twitch.
            Teremos a @gikapassuti como host, então já deixa o follow no
            canal dela: https://www.twitch.tv/gikapassuti '''
        )

    @commands.command(name='gisele')
    async def cmd_gisele(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} Gisele (ela/dela) iniciou a carreira em
            TI na área de testes e recentemente migrou para DevRel.
            Produtora de conteúdo, (aspirante) a streamer e palestrante
            gosta muito de aprender e compartilhar conhecimento. |
            IG https://www.instagram.com/gikatips/ | TT https://twitter.com/gikatips '''
        )

    @commands.command(name='levxyca')
    async def cmd_levxyca(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} Leticia 'levxyca' (ela/dela) é desenvolvedora web
            front-end, streamer, criadora de conteúdo de tecnologia/programação,
            cofundadora/coordenadora da @feminis_tech e tech community
            manager na http://abacatinhos.dev. Conheça mais sobre ela:
            https://links.levxyca.com/ '''
        )

    @commands.command(name='tecna')
    async def cmd_tecna(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} Raquel Marcolino (ela/dela) é desenvolvedora
            backend e doutoranda em Inteligência Artificial. Conheça mais
            sobre ela: Twitter: https://twitter.com/RaquelTecna | Instagram:
            https://www.instagram.com/RaquelTecna/ | Twitch: https://www.twitch.tv/xtecna '''
        )

    @commands.command(name='amanda')
    async def cmd_amanda(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} Amanda Martins Xavier (ela/dela) é desenvolvedora de software.
            Conheça mais sobre ela: https://amandamartins.dev/'''
        )


    @commands.command(name='danicaus')
    async def cmd_danicaus(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} Dani Caus (ela/dela) é desenvolvedora frontend.
            Conheça mais sobre ela: https://www.twitch.tv/danicaus'''
        )


    @commands.command(name='sejogaaline')
    async def cmd_sejogaaline(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} Aline (ela/dela) é analista de automatização de
            processos com robôs que agora transicionando para front-end.
            Conheça mais sobre ela: https://www.twitch.tv/sejogaaline |
            https://www.instagram.com/sejogaaline/ '''
        )

    @commands.command(name='alinepontocom')
    async def cmd_alinepontocom(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} Aline (ela/dela) é analista de automatização de
            processos com robôs que agora transicionando para front-end.
            Conheça mais sobre ela: https://www.twitch.tv/sejogaaline |
            https://www.instagram.com/sejogaaline/ '''
        )

    @commands.command(name='morganna')
    async def cmd_morganna(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} Morganna (ela/dela) é devRel, co-fundadora
            Feministech, co-fundadora Kotlinautas, bancada da Mlkda da DeepWeb.
            Conheça mais sobre ela: https://morganna.dev/ '''
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
