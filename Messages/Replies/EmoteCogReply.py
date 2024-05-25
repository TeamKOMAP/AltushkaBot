from Configs.Emojis import AEmojis
from Messages.Replies.AbstractCogReply import AbstractCommandReply
from Handlers.HandlerReply import HandlerResponse
from Messages.MessagesCategory import MessagesCategory


class EmoteCommandReply(AbstractCommandReply):

    def __init__(self, response: HandlerResponse, category: MessagesCategory) -> None:
        super().__init__(response, category)
        self.__emojis = AEmojis()

    async def run(self, deleteLast: bool = True) -> None:
        # Now with Discord Interactions some commands are triggered without message
        if (self.message is None):
            return None

        if self.response.success:
            await self.message.add_reaction(self.__emojis.SUCCESS)
        else:
            await self.message.add_reaction(self.__emojis.ERROR)
