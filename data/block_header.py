
HEADER_DELIMITER = '*'

class BlockHeader :
    def __init__(self, prevBlockHash):
        self.previousBlockHash = prevBlockHash
        self.timestamp = " "
        self.nonce = " "
        self.difficulty = " "
        self.merkleroot = " "

    def init_from_message(self, message):
        [self.previousBlockHash, self.timestamp, self.nonce, self.difficulty, self.merkleroot] = message.split(HEADER_DELIMITER)

    def toString(self):
        return self.previousBlockHash+HEADER_DELIMITER+\
               self.timestamp+HEADER_DELIMITER+\
               self.nonce+HEADER_DELIMITER+\
               self.difficulty+HEADER_DELIMITER+\
               self.merkleroot;


