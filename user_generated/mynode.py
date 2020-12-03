import time

import crypto
from global_com.message import _Message
from global_com import firebase_api
from global_com.auth import User
from global_com.master import Master
from global_com.chan import _Channels
from global_com.chan import chans
from global_com.message_channel import _MessageChannel
from global_com.slave import Slave
from networking.seed_node import SeedNode
from networking.seed_node import seed_node
# 0a: Initialize
    # Install packages
    # Set the path to setup.json

# Double \
from data.block import Block
from networking.node import Node
from system import system_parameters

# TODO SETUP: add setup.json path

firebase_api.database.setup("C:\\Users\\Filip\\Desktop\\setup.json")
chans.setup()

m = Master('master1', 'addr1')

m.start()
seed_node.start()
# TODO SETUP: register -> run -> replace register with login
# ! DO NOT USE YOUR REAL PASSWORD!

user = User.login("filipdj98@gmail.com", "filip")


# TODO SETUP: extend Node class
class UserNode(Node):
    def __init__(self, user):
        super().__init__(user)

    def block_function(self, message):
        # Check the hash!

        b = Block("")
        b.init_from_message(message)
        last_block = self.blockchain.get_last_block()
        last_block_num = last_block.number

        if last_block_num == b.number - 1:
            self.blockchain.insert_block(block = b, blockHash = b.blockHash)

addr1 = UserNode(User(email='addr1'))
# TODO SETUP: instantiate an instance of the extended class with user passed as a parameter

user_node = UserNode(user)


# TODO 1: Master and seed nodes
#   a) Get the master and seed node addresses from system parameters
#   b) Try to connect with them
#   c) Check if they acceped (the Node class has a connection_error, which is True if the last connection try failed,
#   and False otherwise)

master_node = system_parameters.MASTER_NODE
seed_node_addr = system_parameters.SEED_NODE

message = user_node.confirm("connect")
print("CONFIRM 1")
message.print()

user_node.connect_with_node(seed_node_addr)
if user_node.connection_error:
    #ERROR
    pass


# TODO 2: Connect to 1 more node
#   a) Ask the seed node for some addresses with the get_addr message
#       The seed node will send some addresses to your Node, and they will be present in the node_pool
#       your_node.get_neighbor_addresses().split(',')
#   b) Connect with a pool node // The malicious node should be the last in the list of nodes
#       You have to wait a little to connect to a pool node, since the seed node needs some time to process the message
#       and send a response
#   c) Check the connection
#       You should also wait before checking this, because of similar reasons
#   d) Send address to the master (your_node.confirm(address))
#   e) Get the message -> print the message -> if everything is alright proceed

user_node.send_to_node(seed_node_addr, "get_addr", "")

time.sleep(5)

user_node.connect_with_pool_node()
print(user_node.get_connected_nodes())
connected_address = user_node.get_connected_nodes()[1]
print(connected_address)
message = user_node.confirm(connected_address)

print("CONFIRM 2")
message.print()

user_node.advertise()


time.sleep(5)

print(addr1.node_pool)
# TODO  3: Synchronization
#   a) Implement the block function -> go back to your node class and implement block_function
#       1) Check if the block hash is valid
#           We have to this to see if the information in the block is valid
#       2) Check if the block is next in line
#           You can do this by comparing the sent_block.number to the your_node.blockchain
#       3a) If the block number is next in line -> insert into blockchain
#   b) Send the whole blockchain to the master
#   c) Confirm -> print the message
#      The master will send you an error message, try to find out what it means
#
print("CONFIRM 3")
message = user_node.confirm(user_node.blockchain.toString())
message.print()
# ! Some nodes may not give you full information, or they can even give you false information
# ! If that happens we have to connect to other nodes

# TODO 4: Connect to other nodes
#    1) Call connect_with_pool_node until you connect to a legit node


connection_failed = True

while connection_failed and len(user_node.node_pool)>0:
    user_node.connect_with_pool_node()

    connection_failed = user_node.connection_error

# TODO 5: Get the blockchain from
#    1) Ask a non-malicious node for the blockchain (get_blockchain message)
#       Because you implemented the block function, when you ask for the blockchain,
#       everything will be automatically updated
#       You have to search through the neighbors and see if they differ from the master and seed nodes
#       your_node.get_neigbor_addresses()
#    2) Send blockchain to master -> get message -> confirm

neighbor_list = user_node.get_connected_nodes()

for neighbor in neighbor_list:
    if neighbor != master_node and neighbor != seed_node:
        user_node.send_to_node(neighbor, "get_blockchain", "")

        time.sleep(5)

        if user_node.confirm(user_node.blockchain.toString()):
            print("It's all good")
            break

b = Block("hashshs")

#b.blockHash = crypto.mine(b.toString(), system_parameters.DIFFICULTY)

user_node.send_message_to_all_connected_nodes('block',b.toString())

