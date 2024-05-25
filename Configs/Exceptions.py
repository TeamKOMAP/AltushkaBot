from Configs.Messages import Messages


class AltError(Exception):
    def __init__(self, message='', title='', *args: object) -> None:
        self.__message = message
        self.__title = title
        super().__init__(*args)

    @property
    def message(self) -> str:
        return self.__message

    @property
    def title(self) -> str:
        return self.__title


class ImpossibleMove(AltError):
    def __init__(self, message='', title='', *args: object) -> None:
        message = Messages()
        if title == '':
            title = message.IMPOSSIBLE_MOVE
        super().__init__(message, title, *args)


class MusicUnavailable(AltError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class YoutubeError(AltError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class BadCommandUsage(AltError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class DownloadingError(AltError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class SpotifyError(AltError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class DeezerError(AltError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class UnknownError(AltError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class InvalidInput(AltError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class WrongLength(AltError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class ErrorMoving(AltError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class ErrorRemoving(AltError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class InvalidIndex(AltError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class NumberRequired(AltError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)
