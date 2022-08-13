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
            f'''{ctx.author.name} - No dia 27/08, às 14h, vamos
            ter o evento “Feministalk: Como escrever um livro”.
            Com a @karennovaesd e @patriciavob como host, então já deixa o
            follow no canal: twitch.tv/karennovaesd '''
        )

    @commands.command(name='palestras')
    async def cmd_palestras(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} - 14:00 Introdução ao evento |
            14:15 Pachi apresenta “Como começar: Da proposta aos primeiros capítulos” |
            14:55 Loiane apresenta “5 Dicas de Como Escrever um Livro de Tecnologia” |
            15:35 Entrevistando Vivian Matsui'''
        )

    @commands.command(name='vivian')
    async def cmd_vivian(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} - Vivian Matsui (ela/dela) é editora de livros.
            Encontre ela em: linkedin.com/in/vivianmatsui/
            | instagram.com/vivianmatsui/ '''
        )

    @commands.command(name='loiane')
    async def cmd_loiane(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} - Loiane Groner (ela/dela) é
            possui 15+ anos de experiência em TI, trabalha na área de
            desenvolvimento de software nos Estados Unidos e ama compartilhar
            conhecimento! Palestrante internacional e autora de livros
            publicados mundialmente (com tradução para chinês, coreano e português).
            É Google Developer Expert, Microsoft MVP,
            '''
        )
        await ctx.send('''Sencha MVP, Oracle ACE e Java Champion. Publica tutoriais
            técnicos no Youtube, oferece cursos gratuitos em https://loiane.training e
            escreve para o blog https://loiane.com.
            Encontre ela em: twitter.com/loiane | github.com/loiane | instagram.com/loiane
            youtube.com/loianegroner '''
        )


    @commands.command(name='pachi')
    async def cmd_pachi(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} - Pachi Parra (ela/dela) DevRel (Relacionamentos com
            Pessoas Desenvolvedoras), Co-Fundadora da @feministech.
            Encontre ela em: twitter.com/pachicodes '''
        )


    @commands.command(name='karen')
    async def cmd_karen(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} - Karen Novaes (ela/dela) SRE e produtora de conteúdo.
            Encontre ela em: twitter.com/novaes_karen '''
        )

    @commands.command(name='patricia')
    async def cmd_patricia(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} - Patrícia Villela (ela/dela) Compositora de software.
            Encontre ela em: br.linkedin.com/in/patriciavob | github.com/patriciavillela |
            instagram.com/patriciavob | dev.to/patriciavillela |
            twitter.com/patriciaverso | polywork.com/patriciavillela |
            youtube.com/channel/UCq4Dvs9TkKAPQFbAMvrI8hg |
            patriciavillela.com.br  | twitch.tv/patriciaverso '''
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
