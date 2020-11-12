import time

from networking.seed_node import SeedNode
from data.block import *

# Node usage

node = SeedNode("127.0.0.1", 10003)
time.sleep(1)

# Do not forget to start your node!
node.start()
time.sleep(1)

# Connect with another node, otherwise you do not create any network!
node.connect_with_node('127.0.0.1', 10001)
time.sleep(2)

b = Block("sad5asdasd6as6d600055775asd77da5")

# Example of sending a message to the nodes (dict).
node.send_message_to_nodes("block", b.toString())

time.sleep(5) # Create here your main loop of the application

node.stop()


