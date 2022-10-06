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
            f'''{ctx.author.name} - No dia 08/10, às 14h, vamos
            ter o evento “Feministalk: Hacktoberfest”.
            Um evento dedicado a falarmos sobre o maior evento
            de contribuição do mundo.
            Com a @danicaus como host, então já deixa o
            follow no canal: twitch.tv/danicaus '''
        )

    @commands.command(name='palestras')
    async def cmd_palestras(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} - 14:00 Abertura do evento |
            14:15 Keynote Pachi, Devrel no Github |
            14:55 Bruna apresenta "O que é e como participar do evento Hacktoberfest" |
            15:35 Andressa apresenta "Aprendendo Git e Github" |
            16:05 Patrícia apresenta "O que é open source e como fazer um PR para contribuir"
            '''
        )

    @commands.command(name='dani')
    async def cmd_dani(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} - Dani Caus (ela/dela) Desenvolvedora de software.
            Encontre ela em: https://danicaus.dev/  '''
        )

    @commands.command(name='andressa')
    async def cmd_andressa(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} - Andressa Codes (ela/dela) Analista de Operações
            Sênior Sites e Mautic. Criadora de conteúdo com mais de 10 anos de
            experiência em conteúdo digital de tecnologia. Com foco em programação
            e transição de carreira pela comunidade Andressa Codes.  Ajudo
            contribuindo com contéudo voltado desde iniciantes a intermediários.
            '''
        )
        await ctx.send('''
            Encontre ela em: twitter.com/andressacodes/status/1498057751876063238
            '''
        )

    @commands.command(name='pachi')
    async def cmd_pachi(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} - Pachi Parra (ela/dela) DevRel (Relacionamentos com
            Pessoas Desenvolvedoras), Co-Fundadora da @feministech.
            Encontre ela em: twitter.com/pachicodes '''
        )

    @commands.command(name='bruna')
    async def cmd_bruna(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} - Bruna Ferreira (ela/dela)
            Estudante de Ciência da computação, uma deusa, uma louca, uma feiticeira dos codes.
            Encontre ela em: instagram.com/bug.elseif, twitter.com/bug_elseif'''
        )

    @commands.command(name='patricia')
    async def cmd_patricia(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} - Patrícia Villela (ela/dela) Engenheira de Software desde
            que se entende por gente. Apaixonada por regex e por programação além do saudável,
            e está muito feliz com isso.
            Encontre ela em: twitter.com/patriciaverso'''
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
