from Config.Singleton import Singleton
from Config.Configs import AConfigs
from Config.Emojis import AEmojis


class Messages(Singleton):
    def __init__(self) -> None:
        if not super().created:
            self.__emojis = AEmojis()
            configs = AConfigs()
            self.STARTUP_MESSAGE = 'Starting Altushka...'
            self.STARTUP_COMPLETE_MESSAGE = 'Альтушка прибыла(читать голосом пророка Санбоя)!!!'

            self.SONGINFO_UPLOADER = "Uploader: "
            self.SONGINFO_DURATION = "Duration: "
            self.SONGINFO_REQUESTER = 'Requester: '
            self.SONGINFO_POSITION = 'Position: '

            self.VOLUME_CHANGED = 'Громкость изменена на `{}`%'
            self.SONGS_ADDED = 'Загрузка `{}` треков в очередь'
            self.SONG_ADDED = 'Загрузка трека `{}` в очередь'
            self.SONG_ADDED_TWO = f'{self.__emojis.MUSIC} Трек добавлен в очередь'
            self.SONG_PLAYING = f'{self.__emojis.MUSIC} Трек воспроизводится'
            self.SONG_PLAYER = f'{self.__emojis.MUSIC} Музыкальный плеер'
            self.QUEUE_TITLE = f'{self.__emojis.MUSIC} Треки в очереди'
            self.ONE_SONG_LOOPING = f'{self.__emojis.MUSIC} Повтор одного трека'
            self.ALL_SONGS_LOOPING = f'{self.__emojis.MUSIC} Повтор всех треков'
            self.SONG_PAUSED = f'{self.__emojis.PAUSE} Трек на паузе'
            self.SONG_RESUMED = f'{self.__emojis.PLAY} Трек воспроизводится'
            self.SONG_SKIPPED = f'{self.__emojis.SKIP} Трек пропущен'
            self.RETURNING_SONG = f'{self.__emojis.BACK} Играет предыдущий трек'
            self.STOPPING = f'{self.__emojis.STOP} Воспроизведение остановлено'
            self.EMPTY_QUEUE = f'{self.__emojis.QUEUE} Очередь пуста, используй {configs.BOT_PREFIX}play для добавления треков'
            self.SONG_DOWNLOADING = f'{self.__emojis.DOWNLOADING} Загрузка...'
            self.PLAYLIST_CLEAR = f'{self.__emojis.MUSIC} Плейлист очищен'

            self.HISTORY_TITLE = f'{self.__emojis.MUSIC} Воспроизведенные треки'
            self.HISTORY_EMPTY = f'{self.__emojis.QUEUE} Очередь пуста'

            self.SONG_MOVED_SUCCESSFULLY = 'Трек `{}` на позиции `{}` успешно перемещён на позицию `{}`'
            self.SONG_REMOVED_SUCCESSFULLY = 'Трек `{}` успешно удалён'

            self.LOOP_ALL_ON = f'{self.__emojis.ERROR} Альтушка повторяет все треки, используй {configs.BOT_PREFIX}loop off для выключения повтора'
            self.LOOP_ONE_ON = f'{self.__emojis.ERROR} Альтушка повторяет один трек, используй {configs.BOT_PREFIX}loop off для выключения повтора'
            self.LOOP_ALL_ALREADY_ON = f'{self.__emojis.LOOP_ALL} Альтушка уже повторяет все треки'
            self.LOOP_ONE_ALREADY_ON = f'{self.__emojis.LOOP_ONE} Альтушка уже повторяет один трек'
            self.LOOP_ALL_ACTIVATE = f'{self.__emojis.LOOP_ALL} Все треки на повторе'
            self.LOOP_ONE_ACTIVATE = f'{self.__emojis.LOOP_ONE} Выбранный трек на повторе'
            self.LOOP_DISABLE = f'{self.__emojis.LOOP_OFF} Повтор отключён'
            self.LOOP_ALREADY_DISABLE = f'{self.__emojis.ERROR} Повтор уже отключён'
            self.LOOP_ON = f'{self.__emojis.ERROR} Эта команда не может быть использована, если активен повтор. Используй {configs.BOT_PREFIX}loop off для отключения повтора'
            self.BAD_USE_OF_LOOP = f"""{self.__emojis.ERROR} Неверный аргумент для повтора. Используй {configs.BOT_PREFIX}help loop для полной информации.
                                -> Available Arguments: ["all", "off", "one", ""]"""

            self.SONGS_SHUFFLED = f'{self.__emojis.SHUFFLE} Треки успешно перемешаны'
            self.ERROR_SHUFFLING = f'{self.__emojis.ERROR} Ошибка при перемешивании'
            self.ERROR_MOVING = f'{self.__emojis.ERROR} Ошибка перемещения треков'
            self.LENGTH_ERROR = f'{self.__emojis.ERROR} Числа могут быть от 1 до конца очереди, используй -1 для обозначения последнего трека в очереди.'
            self.ERROR_NUMBER = f'{self.__emojis.ERROR} Эта команда запрашивает число.'
            self.ERROR_VOLUME_NUMBER = f'{self.__emojis.ERROR} Эта команда запрашивает число от 0 до 100'
            self.ERROR_PLAYING = f'{self.__emojis.ERROR} Ошибка воспроизведения'
            self.COMMAND_NOT_FOUND = f'{self.__emojis.ERROR} Команда не найдена, используй {configs.BOT_PREFIX}help, чтобы увидеть список команд'
            self.UNKNOWN_ERROR = f'{self.__emojis.ERROR} Неизвестная ошибка, ты можешь использовать {configs.BOT_PREFIX}reset чтобы сбросить плеер сервера'
            self.ERROR_MISSING_ARGUMENTS = f'{self.__emojis.ERROR} Недостаточно аргументов. Используй {configs.BOT_PREFIX}help "command" для более подробной информации об этой команде'
            self.NOT_PREVIOUS = f'{self.__emojis.ERROR} Предыдущий трек отсутствует'
            self.PLAYER_NOT_PLAYING = f'{self.__emojis.ERROR} Ничего не играет. Используй {configs.BOT_PREFIX}play для воспроизведения'
            self.IMPOSSIBLE_MOVE = 'Это невозможно :('
            self.ERROR_TITLE = 'Ошибочка :-('
            self.COMMAND_NOT_FOUND_TITLE = 'Странно... :-('
            self.NO_CHANNEL = 'Чтобы включить музыку, подключись к какому-либо голосовому каналу.'
            self.NO_GUILD = f'Нет активного плеера, используй {configs.BOT_PREFIX}reset'
            self.INVALID_INPUT = f'Странная ссылка... Попробуй что-то другое или используй {configs.BOT_PREFIX}help play'
            self.INVALID_INDEX = f'Недопустимый индекс в качестве аргумента.'
            self.INVALID_ARGUMENTS = f'Недопустимые аргументы.'
            self.DOWNLOADING_ERROR = f"{self.__emojis.ERROR} Невозможно загрузить и воспроизвести это видео"
            self.EXTRACTING_ERROR = f'{self.__emojis.ERROR} Возникла ошибка при поиске треков'

            self.ERROR_IN_PROCESS = f"{self.__emojis.ERROR} Плеер был перезапущен из-за внутренней ошибки, трек пропущен."
            self.MY_ERROR_BAD_COMMAND = 'Эта строка служит для проверки, не была ли какая-то ошибка вызвана мной специально'
            self.BAD_COMMAND_TITLE = 'Неправильное использование команды'
            self.BAD_COMMAND = f'{self.__emojis.ERROR} Неправильное использование команды, используй {configs.BOT_PREFIX}help "command" для подробной информации о команде'
            self.VIDEO_UNAVAILABLE = f'{self.__emojis.ERROR} Приносим свои извинения. Это видео недоступно для загрузки.'
            self.ERROR_DUE_LOOP_ONE_ON = f'{self.__emojis.ERROR} Эта команда не может быть использована, когда повтор активен. ИСпользуй {configs.BOT_PREFIX}loop off для отключения повтора.'


class SearchMessages(Singleton):
    def __init__(self) -> None:
        if not super().created:
            config = AConfigs()
            self.UNKNOWN_INPUT = f'Странный тип ввода, попробуй по-другому или используй {config.BOT_PREFIX}help play'
            self.UNKNOWN_INPUT_TITLE = 'Ничего не найдено'
            self.GENERIC_TITLE = 'Не удалось обработать URL'
            self.SPOTIFY_NOT_FOUND = 'Spotify не смог найти ни одной песни с такими данными, проверь свою ссылку или попробуй позже.'
            self.YOUTUBE_NOT_FOUND = 'Youtube не смог найти ни одной песни с такими данными, проверь свою ссылку или попробуй позже.'
            self.DEEZER_NOT_FOUND = 'Deezer не смог найти ни одной песни с такими данными, проверь свою ссылку или попробуй позже.'


class SpotifyMessages(Singleton):
    def __init__(self) -> None:
        if not super().created:
            self.INVALID_SPOTIFY_URL = 'Неверный Spotify URL, проверь свою ссылку.'
            self.GENERIC_TITLE = 'URL не может быть обработан'


class DeezerMessages(Singleton):
    def __init__(self) -> None:
        if not super().created:
            self.INVALID_DEEZER_URL = 'Неверный Deezer URL, проверь свою ссылку.'
            self.GENERIC_TITLE = 'URL не может быть обработан'
