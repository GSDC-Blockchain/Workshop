
import time

from networking.p2pnode import Peer2PeerNode
from data.block import Block
from data.genesis_block import *

class SeedNode (Peer2PeerNode):

    # Python class constructor
    def __init__(self, host, port):
        super().__init__(host, port)
        self.node_pool = []

    # Send a message to all nodes
    def send_message_to_nodes(self, type, data):
        self.send_to_nodes(type+"|"+data)

    # Send a message to a single node
    def send_to_node(self, n, type, data):
        super().send_to_node(n,type+"|"+data)


    # On message receive - do something based on message type
    def node_message(self, connected_node, data):
        [type, message] = data.split(sep="|")
        if type == "addr" :
            if self.address_exists(message) == False:
                self.node_pool.insert(message)
                self.send_address_to_neighbors(message)
        elif type == "get_addr" :
            node = self.find_node(message)
            if(node != None):
                self.send_to_node(node, "mult_addr", self.get_neighbor_addresses())
        elif type == "mult_addr" :
            addresses = message.split(',')
            for address in addresses :
                if self.address_exists(message) == False:
                    self.node_pool.insert(message)
       
    # Find node by address
    def find_node(self, address):
        for node in self.all_nodes:
            if node.host+':'+node.port == address:
                return node


    # Address is host + : + port when testing on a single machine
    def address_exists(self, address):
        return address in self.node_pool

    # Send address to all the neighbors
    def send_address_to_neighbors(self, address):
        for node in self.all_nodes:
            self.send_message('address')
        return

    # Return all neighbor addresses
    def get_neighbor_addresses(self):
        addresses = ""
        for node in self.all_nodes:
            addresses += node.host+':'+node.port
        return addresses
