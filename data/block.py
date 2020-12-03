from .block_header import BlockHeader

BLOCK_DELIMITER = ','
num = 0

class Block :
    def __init__(self, prevHash):
        global num
        self.blockSize = " "
        self.header = BlockHeader(prevBlockHash=prevHash)
        self.transactionCounter = " "
        self.transactions = []
        self.info = " "
        self.number = str(num)
        self.blockHash = " "
        num+=1

    def init_from_message(self, message):
        [self.blockSize, blockHeaderTmp, self.transactionCounter, self.info, self.number ,self.blockHash] = message.split(BLOCK_DELIMITER)
        self.header.init_from_message(blockHeaderTmp)

    def print(self):
        print("Block "+ str(self.number))
        print("Info: " + self.info)

    def toString(self):
        # Add transactions later
        return str(self.blockSize) + BLOCK_DELIMITER +\
                self.header.toString() + BLOCK_DELIMITER +\
                str(self.transactionCounter) + BLOCK_DELIMITER + \
                str(self.info) + BLOCK_DELIMITER +\
                str(self.number) + BLOCK_DELIMITER +\
                str(self.blockHash);


