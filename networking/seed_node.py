'''
    GUIDELINES

    1. send_address_to_neighbors(address) -> Used for ADVERTISING

    Nodes can advertise their address to the network, so that the whole network learns about them,
    by sending the address msg to their peers. The peers send the address to their peers, and the node initiator's address
    propagates through the whole network.
    It is important to note that peers will not accept an address if they already know it, and they will not send it to other nodes
    This means that a node can only advertise itself once

    2.


'''

import time

from networking.p2pnode import Peer2PeerNode
from data.block import Block
from data.genesis_block import *

class SeedNode (Peer2PeerNode):

    # Python class constructor
    def __init__(self, host, port):
        super().__init__(host, port)
        self.node_pool = []

    def send_message_to_nodes(self, type, data):
        self.send_to_nodes(type+"|"+data)

    def send_to_node(self, n, data):
        super().send_to_node(n,data)

    def node_message(self, connected_node, data):
        [type, message] = data.split(sep="|")
        if type == "addr" :
            if self.address_exists(message) == False:
                self.node_pool.insert(message)
                self.send_address_to_neighbors(message)
        elif type == "get_addr" :
            node = self.find_node(message)
            if(node != None):
                self.send_to_node(node, self.get_neighbor_addresses())

    def find_node(self, address):
        for node in self.all_nodes:
            if node.host+':'+node.port == address:
                return node


    # Address is host + port when testing on a single machine
    def address_exists(self, address):
        return address in self.node_pool

    # Address is host + port when testing on a single machine
    def send_address_to_neighbors(self, address):
        for node in self.all_nodes:
            self.send_message('address')

        return

    def get_neighbor_addresses(self):
        addresses = []
        for node in self.all_nodes:
            addresses.insert(node.host+':'+node.port)
        return addresses



node = SeedNode("127.0.0.1", 10002)
time.sleep(1)

# Do not forget to start your node!
node.start()
time.sleep(1)

# Connect with another node, otherwise you do not create any network!
node.connect_with_node('127.0.0.1', 10001)
time.sleep(2)

b = Block(prevHash=GENESIS_HASH)

# Example of sending a message to the nodes (dict).
node.send_to_nodes({"message": b.toString()})

time.sleep(5) # Create here your main loop of the application

node.stop()