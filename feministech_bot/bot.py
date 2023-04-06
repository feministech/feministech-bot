from functools import wraps

from twitchio.ext import commands

from .config import BOTS, CHANNELS, TOKEN, USERNAME
from .divulgation import Divulgation
from .random_list import RandomList
from .suppress import Suppress


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
        super().__init__(irc_token=TOKEN, nick=USERNAME, prefix='!', initial_channels=CHANNELS)

        self.divulgation = Divulgation('divulgações.ini')
        self.boas_vindas = Suppress('boas_vindas.tmp')
        self.recomenda = RandomList('recomendações.txt')

    # Events

    async def event_ready(self):
        self.channel = self.get_channel(self.nick)

        print('💜 | Conectado a Twitch com sucesso!')

    async def event_message(self, message):
        await self.handle_boas_vindas(message)
        await self.handle_commands(message)

    async def event_command_error(self, error):
        print(error)

    # Handles

    async def handle_boas_vindas(self, message):
        name = message.author.name
        if message.content and name not in BOTS and self.boas_vindas.add(name):
            await message.channel.send(self.divulgation.get_message(name, f'{name} Boas vindas <3'))

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
            f'''{self.recomenda.get_random()}'''
            )

    @commands.command(name='feministech')
    async def cmd_feministech(self, ctx):
        await ctx.send(
                f'''{ctx.author.name} - Feministech é um grupo de pessoas
                que se identificam no feminino e não binárias que compartilham
                o interesse por lives na Twitch. <3 | Siga e apoie: 
                https://feministech.com.br/'''
            )
        await ctx.send(
                f'''{ctx.author.name} - Time da twitch: '
                https://www.twitch.tv/team/livecodergirls  |  Twitter:
                https://twitter.com/feminis_tech  |  Instagram:
                https://www.instagram.com/feminis_tech/ | Linkedin:
                https://www.linkedin.com/company/feministech/ | Github
                https://github.com/feministech '''
        )

    @commands.command(name='streamers')
    async def cmd_streamers(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} - Conheça as pessoas streamers incríveis
            da nossa comunidade, assista e apoie: 
            https://www.twitch.tv/team/livecodergirls <3'''
        )

    @commands.command(name='caverna')
    async def cmd_caverna(self, ctx):
        await ctx.send(
            '''Uma comunidade voltada para programação em geral com o objetivo de
            se ajudar, estudar coletivamente, e outros. 
            http://caverna.live/discord PowerUpL
            Por favor, não se esqueça de passar no canal #🆁🅴🅶🆁🅰🆂 para liberar
             o acesso á todas as salas do nosso servidor PowerUpR'''
        )

    @commands.command(name='podcast')
    async def cmd_podcast(self, ctx):
        await ctx.send(
            '''Conheça o Feministech Podcast, um podcast feito por uma equipe de 
            mulheres maravilhosas que trabalham ou estudam tecnologia! | 
            https://anchor.fm/feministech'''
        )

    @commands.command(name='evento')
    async def cmd_evento(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} - No dia 04/03 teremos o Feminisocial em parceria
             com o projeto "Mais Meninas na Tecnologia" às 19h00, horário de Brasília.
            Teremos a @gikapassuti como host, então já deixa o follow no canal: 
            twitch.tv/gikapassuti'''
        )
        await ctx.send(
            f'''{ctx.author.name} - Ainda nesse mês no dia 11/03 teremos nosso próximo
            Feministalk presencial e será no RJ. Mais informações aqui:
            https://www.sympla.com.br/evento/feministalk-presencial-rio-de-janeiro/1864354.
            '''
        )

    @commands.command(name='maratona')
    async def cmd_maratona(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} - A Maratona Feministech é um evento marcante da
             comunidade que acontece anualmente para compartilharmos conhecimento
             de diversas streamers.'''
        )
        await ctx.send(
            f'''No ano de 2022,
            realizamos um evento para construir um sistema simples que tenha como
            produto final um site de cadastro de comunidades de tecnologia,
            com o objetivo de mostrar como funciona o desenvolvimento de um
            site de ponta a ponta (banco de dados, frontend, backend e deploy
            em produção), além de divulgar diversas iniciativas de tecnologia.'''
        )

    @commands.command(name='gika')
    async def cmd_gika(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} - A Gisele Passuti (ela/dela) é DevRel na db1group,
            coordenadora na @feministech, com coraçãozinho na qualidade de software. 
            Conheça e acompanhe a Gika: https://twitter.com/gikapassuti'''
        )

    @commands.command(name='lari')
    async def cmd_lari(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} - Larissa Vitoriano (ela/dela). Fundadora do projeto
             Mais Meninas na Tecnologia e Community Manager Tech em StackSpot. Você pode
            encontrá-la nas redes sociais como @laricavitoriano.
            Conheça mais sobre o projeto: https://maismeninasnatecnologia.com/.'''
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

    @commands.command(name='sobe')
    async def cmd_sobe(self, ctx):
        await ctx.send('!rainbow')
