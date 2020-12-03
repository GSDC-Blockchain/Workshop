from data.block import Block
from data.blockchain import Blockchain
from global_com.auth import User
from global_com.firebase_api import database
from global_com.chan import chans
import threading
import time

from global_com.message_channel import _MessageChannel


class Master:
    def __init__(self, id, firstAddr):
        self.id = id
        self.mainThread = threading.Thread(target=self.threadFunction)
        self.firstAddr = firstAddr
        self.blockchain = Blockchain()
        self.blockchain.insert_block(Block("a"), "a")
        self.channel = _MessageChannel(User(email=self.id))
        database.deleteAllDocuments(self.channel.getMessagesPath())
        database.deleteAllDocuments(self.channel.getConfirmPath())

    def _validate(self, slaveId, content):
        stepNum = database.getStep(slaveId)
        [verified, verifiedMessage] = self.validate(stepNum, content, slaveId)

        chans.addChannel(_MessageChannel(User(email=slaveId)))
        chans.sendConfirmMessage(slaveId, self.id, "confirm",verifiedMessage)

        if verified:
            database.incStep(slaveId)

    # Should be implemented / Return True or False
    def validate(self, stepNum, validationContent, slaveId):
        if validationContent == "connect":
                database.resetStep(slaveId)
                return True, "You have successfully connected to the master"
        elif stepNum == 1:
            if validationContent == self.firstAddr:
                return True, "You have successfully connected to " + self.firstAddr
        elif stepNum == 2:
            print(validationContent)
            print(self.blockchain.toString())
            if validationContent == self.blockchain.toString():
                return True, "Congrats, your blockchain is up to date"
            else:
                return False, "Your blockchain is either not up to date, or it has been altered"


        return False, "Unknown error"
    def threadFunction(self):
        while(True):
            m = chans.getConfirmMessage(self.id)
            if(m!=None and m.sender!=""):
                self._validate(m.sender, m.content)
                #print(m.toString())
            time.sleep(2)

    def start(self):
        self.mainThread.start()


"""
u = User.register("milan", "milan@gmail.com", "mmm")
print(database.getStep("milan@gmail.com"))
database.incStep("milan@gmail.com")

print(database.getStep("milan@gmail.com"))
"""



