from Music.AltushkaInit import AltushkaInit
from Config.Folder import Folder

if __name__ == '__main__':
    folder = Folder()
    initializer = AltushkaInit(willListen=True)
    AltushkaBot = initializer.getBot()
    AltushkaBot.startBot()
