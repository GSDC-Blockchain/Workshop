from data.blockchain import Blockchain
from data.block import Block
from data.genesis_block import *


# Blockchain test

blockchain = Blockchain()

b = Block(prevHash=GENESIS_HASH)

b.info = "block number 1"

blockchain.insert_block(b, blockHash="AAA")

blockchain.print()

blockchain.get_block(b.header.previousBlockHash).print()
