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
        super().__init__(
            token=TOKEN,
            nick=USERNAME,
            prefix='!',
            initial_channels=CHANNELS,
        )

        self.divulgacoes = Divulgation('divulgações.ini')
        self.boas_vindas = Suppress('boas_vindas.tmp')
        self.recomendacoes = RandomList('recomendações.txt')

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
            await message.channel.send(
                self.divulgacoes.get_message(name, f'{name} boas-vindas! <3')
            )

    # Commands

    @commands.command(name='comandos')
    async def cmd_comandos(self, ctx):
        comandos = list(self.commands.keys())
        await ctx.send(f'Comandos: {" | ".join(comandos)}')

    @commands.command(name='recomenda')
    async def cmd_recomendacoes(self, ctx):
        await ctx.send(f'{self.recomendacoes.get_random()}')

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

    ## Feministech

    @commands.command(name='feministech')
    async def cmd_feministech(self, ctx):
        await ctx.send(
            f"""{ctx.author.name} - A Feministech é um grupo de pessoas que se 
              identificam no feminino e não-bináries que produzem, consomem e 
              compartilham conteúdo sobre tecnologia, enquanto constroem uma 
              comunidade diversa e inclusiva. <3 | Siga e apoie: 
              https://feministech.com.br/"""
        )
        await ctx.send(
            f"""{ctx.author.name} - Time da twitch: 
            https://www.twitch.tv/team/livecodergirls | Twitter: 
            https://twitter.com/feminis_tech | Instagram: 
            https://www.instagram.com/feminis_tech/ | Linkedin: 
            https://www.linkedin.com/company/feministech/ | Github: 
            https://github.com/feministech."""
        )

    @commands.command(name='streamers')
    async def cmd_streamers(self, ctx):
        await ctx.send(
            f"""{ctx.author.name} - Conheça as pessoas streamers incríveis da 
            nossa comunidade, assista e apoie: 
            https://www.twitch.tv/team/livecodergirls. <3"""
        )

    @commands.command(name='podcast')
    async def cmd_podcast(self, ctx):
        await ctx.send(
            f"""{ctx.author.name} - Conheça o Feministech Podcast, um podcast 
            feito por uma equipe de pessoas maravilhosas que trabalham ou 
            estudam tecnologia! | https://anchor.fm/feministech."""
        )

    @commands.command(name='conduta')
    async def cmd_conduta(self, ctx):
        await ctx.send(
            f"""{ctx.author.name} - O mais importante por aqui é o respeito. 
            Conheça o Código de Conduta da nossa comunidade: 
            https://github.com/feministech/codigo-de-conduta. :)"""
        )

    ## Caverna

    @commands.command(name='caverna')
    async def cmd_caverna(self, ctx):
        await ctx.send(
            f"""{ctx.author.name} - A Caverna é uma comunidade de pessoas 
            desenvolvedoras de todos os níveis e das mais variadas 
            especializacões | http://caverna.live/. PowerUpL"""
        )
        await ctx.send(
            """Discord: http://caverna.live/discord | Por favor, não se 
            esqueça de passar no canal #🆁🅴🅶🆁🅰🆂 para liberar o acesso á todas 
            as salas do nosso servidor. PowerUpR"""
        )

    ## Misc.

    @commands.command(name='evento')
    async def cmd_evento(self, ctx):
        await ctx.send(
            f"""{ctx.author.name} - Nos dias 24, 25 e 26 de maio 
            acontecerá a GALACTECH! Uma conferência online para explorar 
            Comunidades, Conteúdo e Developer Relations. 
            Começa às 19h00, horário de Brasília. 
            Teremos a @gikapassuti e @morgannadev como hosts, então já 
            deixa o follow no canal: https://twitch.tv/feministech."""
        )

    @commands.command(name='gisele')
    async def cmd_gika(self, ctx):
        await ctx.send(
            f"""{ctx.author.name} - A Gisele (ela/dela) é DevRel na 
            db1group, coordenadora na @feministech, e tem um coraçãozinho na 
            qualidade de software. | Conheça e acompanhe a Gika: 
            https://twitter.com/gikapassuti | www.instagram.com/gikapassuti/"""
        )

    @commands.command(name='andreza')
    async def cmd_andreza(self, ctx):
        await ctx.send(
            f"""{ctx.author.name} - Andreza Rocha (ela/dela) é CEO e 
            fundadora do AfrOya Tech. 
            | Conheça e acompanhe a Andreza: 
            https://www.linkedin.com/in/andrezarocha/ """
        )

    @commands.command(name='morganna')
    async def cmd_morganna(self, ctx):
        await ctx.send(
            f"""{ctx.author.name} - Morganna (ela/dela) é DevRel na 
            BotCity, criadora de conteúdo e evangelizadora Ada Lovelace. 
            | Conheça e acompanhe a Morgs: 
            https://www.linkedin.com/in/morgannadev/ """
        )

    @commands.command(name='pachi')
    async def cmd_pachi(self, ctx):
        await ctx.send(
            f"""{ctx.author.name} - Pachi Parra (ela/dela) é Developer Advocate 
            no GitHub, Coach de dev de palco e patrimônio histórico da Feministech
            | Conheça e acompanhe a Pachi: 
            https://github.com/pachicodes | https://twitter.com/pachicodes """
        )

    @commands.command(name='lari')
    async def cmd_lari(self, ctx):
        await ctx.send(
            f"""{ctx.author.name} - Larissa Vitoriano (ela/dela) é Fundadora 
            do projeto Mais Meninas na Tecnologia e Community Manager Tech em 
            StackSpot. Você pode encontrá-la nas redes sociais como 
            @laricavitoriano. | Conheça e acompanhe a Larissa: 
            https://instagram.com/laricavitoriano """
        )

    @commands.command(name='levxyca')
    async def cmd_levxyca(self, ctx):
        await ctx.send(
            f"""{ctx.author.name} - Leticia 'levxyca' (ela/dela) é 
            desenvolvedora de software, criadora de conteúdo e 
            cofundadora da Feministech. 
            | Conheça e acompanhe a levxyca: 
            https://github.com/levxyca | 
            https://www.linkedin.com/in/leticiacaroline/ """
        )

    @commands.command(name='lunna')
    async def cmd_lunna(self, ctx):
        await ctx.send(
            f"""{ctx.author.name} - Lunna Fabris (ela/dela) é 
            Designer e Youtuber. 
            | Conheça e acompanhe a levxyca: 
            https://twitter.com/Lunna_Fabris """
        )

    @commands.command(name='natalia')
    async def cmd_natalia(self, ctx):
        await ctx.send(
            f"""{ctx.author.name} - Natália F. Dev (ela/dela) é 
            Desenvolvedora front-end e Devrel. 
            | Conheça e acompanhe a Natália: 
            https://www.instagram.com/nataliafdev/ """
        )

    @commands.command(name='jeniffer')
    async def cmd_jeniffer(self, ctx):
        await ctx.send(
            f"""{ctx.author.name} - Jeniffer Bittencourt (ela/dela) é 
            Criadora de bugs em Kotlin. 
            | Conheça e acompanhe a Jeniffer: 
            https://www.linkedin.com/in/jeniffer-bittencourt |
            https://instagram.com/jeniblo_dev """
        )

    @commands.command(name='nadi')
    async def cmd_nadi(self, ctx):
        await ctx.send(
            f"""{ctx.author.name} - Nadi Duno (ela/dela), 
            de pintora de paredes a artista de dados. 
            | Conheça e acompanhe a Nadi: 
            https://www.linkedin.com/in/nadiduno/ """
        )

    @commands.command(name='malu')
    async def cmd_malu(self, ctx):
        await ctx.send(
            f"""{ctx.author.name} - Malu Sabino (ela/dela) é 
            Community Manager e Porta voz do Roadsec.  
            | Conheça e acompanhe a Nadi: 
            https://www.linkedin.com/in/nadiduno/ """
        )

    ## Events

    """     
    @commands.command(name='evento')
    async def cmd_evento(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} - No dia 04/03 teremos o Feminisocial em 
            parceria com o projeto "Mais Meninas na Tecnologia" às 19h00, 
            horário de Brasília. Teremos a @gikapassuti como host, então já 
            deixa o follow no canal: https://twitch.tv/gikapassuti.'''
        )
        await ctx.send(
            '''Ainda nesse mês no dia 11/03 teremos nosso próximo 
            Feministalk presencial e será no RJ. Mais informações aqui: 
            https://www.sympla.com.br/evento/feministalk-presencial-rio-de-janeiro/1864354
            .'''
        )
    """

    """ 
    @commands.command(name='maratona')
    async def cmd_maratona(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} - A Maratona Feministech é um evento 
            marcante da comunidade que acontece anualmente para 
            compartilharmos conhecimento de diversas streamers.'''
        )
        await ctx.send(
            '''No ano de 2022, realizamos um evento para construir um sistema 
            simples que tenha como produto final um site de cadastro de 
            comunidades de tecnologia, com o objetivo de mostrar como 
            funciona o desenvolvimento de um site de ponta a ponta (banco de 
            dados, frontend, backend e deploy em produção), além de divulgar 
            diversas iniciativas de tecnologia.'''
        )
    """
