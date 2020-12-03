from global_com.firebase_api import database


# User message channel
from global_com.message import _Message

class _MessageChannel:
    def __init__(self, user):
        self.user = user
    def getChannelId(self):
        return self.user.email

    def getMessagesPath(self):
        return 'message-channels/' + self.getChannelId() + '/messages'

    def getConfirmPath(self):
        return 'message-channels/' + self.getChannelId() + '_confirm/messages'

    def sendMessage(self, sender, type, content):
        database.addMessage(self.getChannelId(), sender, type, content)

    def getMessage(self):
        return _Message.from_dict(database.getOneDocument(self.getMessagesPath()).to_dict())

    def getMessages(self, n):
        return database.getDocuments(self.getMessagesPath(), n)

    def getConfirmMessage(self):
        return _Message.from_dict(database.getOneDocument(self.getConfirmPath()).to_dict())

    def sendConfirmMessage(self, sender, type, content):
        database.addMessage(self.getChannelId()+'_confirm', sender, type, content)
