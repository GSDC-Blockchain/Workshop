from .genesis_block import GenesisBlock
from .genesis_block import GENESIS_HASH

class Blockchain:
    def __init__(self):
        self.chain = {}
        self.insert_block(GenesisBlock(), GENESIS_HASH)

    # Insert block in a dictionary
    def insert_block(self, block, blockHash):
        self.chain[blockHash] = block

    def get_block(self, blockHash):
        return self.chain.get(blockHash)

    def print(self):
        for key in self.chain:
            block = self.chain.get(key)
            block.print()
