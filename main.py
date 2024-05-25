from Music.AltushkaBotInit import AltushkaBotInit
from Configs.Folder import Folder

if __name__ == '__main__':
    folder = Folder()
    initializer = AltushkaBotInit(willListen=True)
    AltushkaBot = initializer.getBot()
    AltushkaBot.startBot()
