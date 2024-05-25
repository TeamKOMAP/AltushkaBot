from Messages.Replies.AbstractCogReply import AbstractCommandReply
from Handlers.HandlerReply import HandlerResponse
from Messages.MessagesCategory import MessagesCategory
from Messages.DcMessages import AAbstractMessage, AWebHookMessage
from discord import ApplicationContext


class SlashEmbedReply(AbstractCommandReply):
    def __init__(self, response: HandlerResponse, ctx: ApplicationContext, category: MessagesCategory) -> None:
        self.__ctx = ctx
        super().__init__(response, category)

    async def run(self, deleteLast: bool = True) -> None:
        message = None
        # If the response has both embed and view to send
        if self.response.embed and self.response.view:
            # Respond the Slash command and set the view to contain the sended message
            message = await self.__ctx.send_followup(embed=self.response.embed, view=self.response.view)
            self.response.view.set_message(message)

        # If the response only has the embed then send the embed
        elif self.response.embed:
            message = await self.__ctx.send_followup(embed=self.response.embed)
        else:
            message = await self.__ctx.send_followup('Oк!')

        # If any message was sended
        if message:
            # Convert
            aMessage: AAbstractMessage = AWebHookMessage(message)
            # Only delete the previous message if this is not error and not forbidden by method caller
            if deleteLast and self.response.success:
                await self.manager.addMessageAndClearPrevious(self.context.guild.id, self.category, aMessage, self.response.view)
            else:
                self.manager.addMessage(self.context.guild.id, self.category, aMessage)
