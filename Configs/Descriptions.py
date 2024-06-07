from Configs.Singleton import Singleton
from Configs.Configs import AConfigs


class Descriptions(Singleton):
    def __init__(self) -> None:
        if not super().created:
            config = AConfigs()
            self.HELP_SKIP = 'Пропускает текущий трек.'
            self.HELP_SKIP_LONG = 'Пропускает текущий трек. Не работает, если включен повтор.'
            self.HELP_RESUME = 'Возобновляет воспроизведение.'
            self.HELP_RESUME_LONG = 'Возобновляет воспроизведение, если оно приостановлено.'
            self.HELP_CLEAR = 'Очищает очередь и историю.'
            self.HELP_CLEAR_LONG = 'Очищает очередь и историю треков.'
            self.HELP_STOP = 'Останавливает воспроизведение.'
            self.HELP_STOP_LONG = 'Останавливает воспроизведение, очищает очередь и историю и отключает бота от канала.'
            self.HELP_LOOP = 'Управляет повтором треков.'
            self.HELP_LOOP_LONG = """Управляет повтором треков.\n\n Требования: Песня играет в настоящий момент.\nАргументы:
                One - Повтор текущего трека.
                All - Повтор всей очереди.
                Off - Повтор выкл."""
            self.HELP_NP = 'Информация о текущем треке.'
            self.HELP_NP_LONG = 'Показывает информацию о текущем треке.\n\nТребования: Песня играет в настоящий момент.'
            self.HELP_QUEUE = f'Показывает первые {config.MAX_SONGS_IN_PAGE} треков в очереди.'
            self.HELP_QUEUE_LONG = f'Показывает первые {config.MAX_SONGS_IN_PAGE} треков в очереди.'
            self.HELP_PAUSE = 'Ставит плеер на паузу.'
            self.HELP_PAUSE_LONG = 'Если песня играет, ставит её на паузу.'
            self.HELP_PREV = 'Включает предыдущий трек.'
            self.HELP_PREV_LONG = 'Включает предыдущий трек. Если играет, ставит текущий трек в очередь.\n\nТребования: Повтор выкл.'
            self.HELP_SHUFFLE = 'Включает случайный порядок треков.'
            self.HELP_SHUFFLE_LONG = 'Включает случайный порядок треков в очереди.'
            self.HELP_PLAY = 'Включает трек по URL или названию.'
            self.CHANGE_VOLUME = 'Переключает громкость плеера.'
            self.CHANGE_VOLUME_LONG = 'Переключает громкость плеера, варьируется от 0 до 100.'
            self.HELP_PLAY_LONG = 'Включает трек. \n\nТребования: Вы подключены к голосовому каналу.\nАргументы: Ссылка на песню/плейлист на Youtube, Spotify или Deezer, или название песни для поиска на YouTube.'
            self.HELP_HISTORY = f'Показывает историю треков.'
            self.HELP_HISTORY_LONG = f'Отображает последние {config.MAX_SONGS_HISTORY} воспроизведённых треков'
            self.HELP_MOVE = 'Ставит песню в очереди с одной позиции на другую.'
            self.HELP_MOVE_LONG = 'Ставит песню в очереди с позиции x на позицию y.\n\nТребования: Обе позиции являются натуральными числами.\nАргументы: 1º Номер => Первоначальная позиция, 2º Номер => Итоговая позиция. Для обозначения последней песни в очереди число может равняться -1.\nПо умолчанию: Если число 2 не указано, будет выбрана позиция 1.'
            self.HELP_REMOVE = 'Удаляет трек из очереди.'
            self.HELP_REMOVE_LONG = 'Удаляет трек на выбранной позиции из очереди.\n\nТребования: Позиция должна быть натуральным числом.\nАргументы: Номер трека, который нужно удалить'
            self.HELP_RESET = 'Сбрасывает плеер.'
            self.HELP_RESET_LONG = 'Сбрасывает плеер сервера.'
            self.HELP_HELP = f'Используй {config.BOT_PREFIX}help "command" для подробной информации.'
            self.HELP_HELP_LONG = f'Используй {config.BOT_PREFIX}help "command" для подробной информации о конкретной команде.'
            self.HELP_INVITE = 'Отправляет ссылку-приглашение для заказа альтушки на твой сервер :3.'
            self.HELP_INVITE_LONG = 'Отправляет ссылку-приглашение для заказа альтушки на твой сервер :3'
            self.HELP_RANDOM = 'Выбирает случайное число от 1 до x.'
            self.HELP_RANDOM_LONG = 'Выбирает случайное число от 1 до x.\n\nТребованияd: Число должно быть натуральным.\nАргументы: Любое натуральное число больше 1.'
            self.HELP_CHOOSE = 'Выбирает случайный объект.'
            self.HELP_CHOOSE_LONG = 'Выбирает случайный объект, указанный в аргументе.\n\nТребования: Объекты должны быть разделены запятой.\nАргументы: Сколько угодно аргументов.'
            self.HELP_CARA = 'Возвращает Komaru или Komugi.'
            self.HELP_CARA_LONG = 'Возвращает Komaru или Komugi.'
            self.HELP_PURGE = 'Удаляет указанное количество сообщений'
            self.HELP_PURGE_LONG = 'Удаляет указанное в аргументе количество сообщений.\nАргументы: Любое натуральное число от 1'

            self.SLASH_QUEUE_DESCRIPTION = f'На странице может быть только {config.MAX_SONGS_IN_PAGE} треков'
            self.SLASH_MOVE_HELP = 'Перемещает трек в очереди с позиции 1 на позицию 2.'
