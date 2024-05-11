import os
from dotenv import load_dotenv
from Config.Singleton import Singleton
from Config.Folder import Folder


load_dotenv()

class AConfigs(Singleton):
    def __init__(self) -> None:
        if not super().created:
            # You can change this boolean to False if you want to prevent the Bot from auto disconnecting
            self.SHOULD_AUTO_DISCONNECT_WHEN_ALONE = os.getenv('SHOULD_AUTO_DISCONNECT_WHEN_ALONE') == 'True'
            
            # Рекомендуется установить значение True, за исключением случаев, когда ваш бот присутствует на тысячах серверов,
            # в этом случае задержка запуска нового процесса Python для воспроизведения слишком велика,
            # и чтобы избежать этого, вы устанавливаете значение False.
            self.SONG_PLAYBACK_IN_SEPARATE_PROCESS = os.getenv('SONG_PLAYBACK_IN_SEPARATE_PROCESS', 'True') == 'True'

            # Максимальное количество песен, которые будут загружены одновременно, и чем выше это число,
            # тем быстрее все песни будут доступны, но медленнее будут выполняться остальные команды бота во время загрузки
            self.MAX_DOWNLOAD_SONGS_AT_A_TIME = int(os.getenv('MAX_DOWNLOAD_SONGS_AT_A_TIME', 5))

            self.BOT_PREFIX = os.getenv('BOT_PREFIX', '!')

            if self.BOT_PREFIX == 'Your_Wanted_Prefix':
                self.BOT_PREFIX = '!'
            
            self.BOT_TOKEN = os.getenv('BOT_TOKEN')
            if self.BOT_TOKEN is None:
                raise ValueError('No token was given')

            self.SPOTIFY_ID = os.getenv('SPOTIFY_ID')
            self.SPOTIFY_SECRET = os.getenv('SPOTIFY_SECRET')
            
            if self.SPOTIFY_ID == "Your_Own_Spotify_ID":
                self.SPOTIFY_ID = None
            
            if self.SPOTIFY_SECRET == "Your_Own_Spotify_Secret":
                self.SPOTIFY_SECRET = None
            
            if self.SPOTIFY_ID is None or self.SPOTIFY_SECRET is None:
                print('Spotify will not work')

            self.CLEANER_MESSAGES_QUANT = int(os.getenv('CLEANER_MESSAGES_QUANT', 5))
            self.ACQUIRE_LOCK_TIMEOUT = int(os.getenv('ACQUIRE_LOCK_TIMEOUT', 10))
            self.QUEUE_VIEW_TIMEOUT = int(os.getenv('QUEUE_VIEW_TIMEOUT', 120))

            self.COMMANDS_FOLDER_NAME = os.getenv('COMMANDS_FOLDER_NAME', 'DiscordCogs')
            self.COMMANDS_PATH = f'{Folder().rootFolder}{self.COMMANDS_FOLDER_NAME}'
            self.VC_TIMEOUT = int(os.getenv('VC_TIMEOUT', 300))

            self.CHANCE_SHOW_PROJECT = int(os.getenv('CHANCE_SHOW_PROJECT', 1))
            self.PROJECT_URL = os.getenv('PROJECT_URL', 'https://github.com/offlayt/kakashka')
            self.SUPPORTING_ICON = os.getenv('SUPPORTING_ICON', 'https://i.imgur.com/SUEohXG.png')

            self.MAX_PLAYLIST_LENGTH = int(os.getenv('MAX_PLAYLIST_LENGTH', 50))
            self.MAX_PLAYLIST_FORCED_LENGTH = int(os.getenv('MAX_PLAYLIST_FORCED_LENGTH', 5))
            self.MAX_SONGS_IN_PAGE = int(os.getenv('MAX_SONGS_IN_PAGE', 10))
            self.MAX_PRELOAD_SONGS = int(os.getenv('MAX_PRELOAD_SONGS', 15))
            self.MAX_SONGS_HISTORY = int(os.getenv('MAX_SONGS_HISTORY', 15))

            self.INVITE_MESSAGE = os.getenv('INVITE_MESSAGE', """- Чтобы заказать Альтушку к себе на сервер, просто нажмите [здесь!]({}). 
            - Или используйте эту ссылку: {}""")

            self.MY_ERROR_BAD_COMMAND = os.getenv('MY_ERROR_BAD_COMMAND', 'This string serves to verify if some error was raised by myself on purpose')
            self.INVITE_URL = os.getenv('INVITE_URL', 'https://discordapp.com/oauth2/authorize?client_id={}&permissions=8&scope=bot')

    def getPlayersManager(self):
        return self.__manager

    def setPlayersManager(self, newManager):
        self.__manager = newManager
