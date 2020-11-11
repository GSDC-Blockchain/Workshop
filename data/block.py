from .block_header import BlockHeader

num = 0

class Block :
    def __init__(self, prevHash):
        global num
        self.blockSize = 0
        self.header = BlockHeader(prevBlockHash=prevHash)
        self.transactionCounter = 0
        self.transactions = []
        self.info = ""
        self.number = num
        num+=1

    def print(self):
        print("Block "+ str(self.number))
        print("Info: " + self.info)

    def toString(self):
        return "Block "+ str(self.number)