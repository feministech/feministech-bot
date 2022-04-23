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
            f'''{ctx.author.name} Hoje estamos realizando o nosso
            evento Feministalk: Carreiras para compartilharmos
            juntes um excelente conteúdo, contando com apoio de
            pessoas profissionais da área. Aproveitem para compartilhar,
            fazer networking e tirarem dúvidas. Para uma boa experiência
            para todes, conheçam nosso Código de Conduta: digite !conduta no chat.'''
        )

    @commands.command(name='rodadeconversa')
    async def cmd_rodadeconversa(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} Teremos uma Roda de Conversa para falar
            com pessoas profissionais maravilhosas da área de recrutamento
            e tecnologia sobre carreira e diversas dicas deste universo.
            Teremos a presença de !marianna, !bru, !jamille, !jessica, !kamila,
            !isabela, !leticia. Conheça mais sobre elas digitando o
            comando no chat.'''
        )

    @commands.command(name='palestras')
    async def cmd_palestras(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} 13h00 - 13h30: !silva como keynote do
            tema "Conhecendo Silvia Coelho: inspire-se em sua história"
            || 13h35 - 14h05: !paula com o tema "O mundo das mentorias e
            suas surpresas" '''
        )
        await ctx.send(
            ''' 14h10 - 14h40: !monique com o tema "Papo
            sobre vida de pessoa desenvolvedora e empreendedora" ||
            14h45 - 15h15: !cami com o tema  "Dicas de carreira para ingresso,
            transição e processos seletivos" ||
            15h20 - 16h00: !isabelle com o tema "PJotinha, vale mesmo a
            pena?" || 16h05 - 17h30: !rodadeconversa
            '''
        )

    @commands.command(name='silvia')
    async def cmd_silvia(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} Silvia Coelho (ela/dela) é fundadora
            do Elas Programam e estará em nosso keynote para contar sua
            história. Conheça e acompanhe seu trabalho:
            https://instagram.com/elasprogramam'''
        )

    @commands.command(name='paula')
    async def cmd_paula(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} Paula Santana (ela/dela) é especialista
            de desenvolvimento, educadora, mentora, pagando os boletos com
            Java desde 2014, apaixonada por viajar, mãe de gato e cansada.
            É também palestrante do tema “O mundo das mentorias e suas
            surpresas”. Conheça e acompanhe seu trabalho:
            https://twitter.com/psanrosa13 e
            https://www.linkedin.com/in/paula-macedo-santana-dev/'''
        )

    @commands.command(name='monique')
    async def cmd_monique(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} Monique Oliveira (ela/dela) é empreendedora
            e nerd raíz. E também palestrante do tema: “Papo sobre vida de
            pessoa desenvolvedora e empreendedora”. Conheça e acompanhe seu
            trabalho: https://twitter.com/moniquelive e
            https://www.instagram.com/moniquelive.dev/'''
        )

    @commands.command(name='cami')
    async def cmd_cami(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} Cami Martins (ele/ela https://pronoun.is/they)
            é punk, paulista, santista. Docker Community Leader. Sou Senior Site
            Reliability Engineer e atualmente trabalho na Storyblok, com pós em
            Forense Computacional e mestrando em Operação, avaliação e gerenciamento
            avançado de redes de computadores na Universidade Federal do Estado do
            Rildy Janeiro hehe.'''
        )
        await ctx.send(
            ''' Nas horas vagas, estou codando (também!) e surtando
            com uma gatinha preta chamada Marvel (!) <3.
            Conheça e acompanhe seu trabalho:
            https://punkdodevops.com
            '''
        )

    @commands.command(name='leticia')
    async def cmd_leticia(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} Letícia Silva (ela/dela) é Gerente
            de Engenharia na Z1, é também responsável pela área de
            Developer Experience na empresa. Veio da área de Ciência
            de Dados e possui formação em Ciência da Computação. É
            podcaster no Botech-in, ensina sobre Dados na PretaLab,
            cria conteúdo para a comunidade e é palestrinha e mentora nas
            horas vagas.
            '''
        )
        await ctx.send(
            '''É também participante da nossa roda de conversa
            sobre Carreiras em Tecnologia. Conheça e acompanhe seu trabalho:
            https://www.instagram.com/dii_lua/ e  https://twitter.com/dii_lua'''
        )

    @commands.command(name='isabelle')
    async def cmd_isabelle(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} Isabelle Samways (ela/dela) é Pedreira
            de Software, aka dev backend. É também palestrante do tema
            “PJotinha, vale mesmo a pena?”. Conheça e acompanhe seu
            trabalho: https://twitter.com/bellesamways'''
        )

    @commands.command(name='marianna')
    async def cmd_marianna(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} Marianna Costa (ela/dela) é Tech Recruiter.
            É também participante da nossa roda de conversa sobre Carreiras
            em Tecnologia. Conheça e acompanhe seu trabalho:
            https://twitter.com/ITrecruitermari e
            https://www.linkedin.com/in/mariannapcosta/'''
        )

    @commands.command(name='bru')
    async def cmd_bru(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} Bru (ela/dela) é Vendedora
            de Oportunidades. É também participante da nossa
            roda de conversa sobre Carreiras em Tecnologia.
            Conheça e acompanhe seu trabalho:
            https://www.linkedin.com/in/bruna-s-b2700b46/'''
        )

    @commands.command(name='jamille')
    async def cmd_jamille(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} Jamille de Oliveira
            (ela/dela) é Analista de Atração e Seleção
            de Talentos. É também participante da nossa
            roda de conversa sobre Carreiras em Tecnologia.
            Conheça e acompanhe seu trabalho:
            https://www.linkedin.com/in/jamille-de-oliveira-26b4756b/'''
        )

    @commands.command(name='kamila')
    async def cmd_kamila(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} Kamila Santos (ela/dela)
            é Desenvolvedora backend e criadora de conteúdo
            kamila code. É também participante da nossa roda
            de conversa sobre Carreiras em Tecnologia. Conheça
            e acompanhe seu trabalho: https://beacons.page/kamila_code'''
        )

    @commands.command(name='isabela')
    async def cmd_isabela(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} Isabela Norton (ela/dela) é Tech
            Recruiter. É também participante da nossa roda de
            conversa sobre Carreiras em Tecnologia. Conheça e acompanhe
            seu trabalho: Twitter https://twitter.com/isanortontech e
            Linkedin https://www.linkedin.com/in/isabelanorton/ '''
        )

    @commands.command(name='sorteio')
    async def cmd_sorteio(self, ctx):
        await ctx.send(
            f'''{ctx.author.name} Para participar do sorteio,
            preencha o seguinte formulário:
            https://forms.gle/yhhmooBWikus428v6 e continue
            online conosco para ser considerade.'''
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
