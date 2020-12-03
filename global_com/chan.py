from global_com.message_channel import _MessageChannel
from global_com.auth import User
from global_com.settings import SETTINGS
class _Channels:
    def __init__(self):
        self.channels = {}


    def setup(self):
        master = SETTINGS['MASTER_ADDR']
        u = User(email=master)
        self.channels[master] = _MessageChannel(u)

    def addChannel(self, channel):
        self.channels[channel.getChannelId()] = channel

    def sendMessage(self, channelId, sender, type, content):
        self.channels[channelId].sendMessage(sender, type, content)

    def getMessage(self, channelId):
        return self.channels[channelId].getMessage()

    def sendConfirmMessage(self, channelId, sender, type, content):
        self.channels[channelId].sendConfirmMessage(sender, type, content)

    def getConfirmMessage(self, channelId):
        if not channelId in self.channels:
            return None
        return self.channels[channelId].getConfirmMessage()

chans = _Channels()

#chans.sendMessage(u.email, "init", "Goran")

#print(Message.messages_from_arr(mc.getMessages(1))[0].toString())