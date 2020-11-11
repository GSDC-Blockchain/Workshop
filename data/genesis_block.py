from .block import Block

# Bitcoin genesis hash
GENESIS_HASH = "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"

class GenesisBlock (Block) :
    def __init__(self):
        super().__init__("")
        self.info = "THE GENESIS BLOCK "
