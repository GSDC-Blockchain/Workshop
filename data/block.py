from .block_header import BlockHeader

BLOCK_DELIMITER = ','
num = 0

class Block :
    def __init__(self, prevHash):
        global num
        self.blockSize = ""
        self.header = BlockHeader(prevBlockHash=prevHash)
        self.transactionCounter = ""
        self.transactions = []
        self.info = ""
        self.number = str(num)
        num+=1

    def init_from_message(self, message):
        [self.blockSize, blockHeaderTmp, self.transactionCounter, self.transactions, self.info, self.number] = message.split(BLOCK_DELIMITER)
        self.header.init_from_message(blockHeaderTmp)

    def print(self):
        print("Block "+ str(self.number))
        print("Info: " + self.info)

    def toString(self):
        # Add transactions later
        return self.blockSize + BLOCK_DELIMITER +\
                self.header.toString() + BLOCK_DELIMITER +\
                self.transactionCounter + BLOCK_DELIMITER + \
                self.info + BLOCK_DELIMITER +\
                self.number;


