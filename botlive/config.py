from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini', encoding='utf-8')

TOKEN = config.get('config', 'token')
USERNAME = config.get('config', 'username')
BOTS = config.get('config', 'bots').split()
BOTS.append(USERNAME)
PROJECT = config.get('config', 'project')
STREAMERS = config.get('config', 'streamers').split()
# STREAMERS = [
#     'bug_elseif',
#     'feministech',
#     'pachicodes',
#     'xtecna',
#     'mmillecm',
#     'leitoraincomum',
#     'morgannadev',
#     'levxyca',
#     'leonadev',
#     'moniquelive',
#     'punkdodevops',
#     'ehmuitodrama',
#     'lissatransborda',
#     'danicaus',
#     'unnotedme',
#     'increibleju',
#     'andreiammm',
#     'patriciaverso',
#     'gikapassuti',
#     'sejogaaline',
#     'amandamartinsdev',
#     'karennovaesd',
#     ]
