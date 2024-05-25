from discord import Message, WebhookMessage
from abc import ABC, abstractmethod


class AAbstractMessage(ABC):
    """
    Абстрактный класс, позволяющий создавать шаблон при работе с несколькими Discord.
    типы сообщений, такие как сообщения взаимодействия и стандартные сообщения разногласий
    который содержит два разных способа удаления
    """
    @abstractmethod
    async def delete(self):
        pass


class AWebHookMessage(AAbstractMessage):
    """
    Holds a WebhookMessage instance 
    """

    def __init__(self, message: WebhookMessage) -> None:
        self.__message = message
        super().__init__()

    async def delete(self):
        await self.__message.delete()


class ADefaultMessage(AAbstractMessage):
    """
    Holds a Message instance, the basic Discord message type
    """

    def __init__(self, message: Message) -> None:
        self.__message = message
        super().__init__()

    async def delete(self):
        await self.__message.delete()
