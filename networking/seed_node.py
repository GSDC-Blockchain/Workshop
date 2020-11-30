
import time

from data.block import Block
from data.genesis_block import *

from global_com.master import Master
from global_com.message_channel import _MessageChannel
from global_com.chan import chans

import threading
MAX_CONNECTED_NODES = 8


class SeedNode:

    # Python class constructor
    def __init__(self, user):
        self.user = user
        self.channel = _MessageChannel(user)
        chans.addChannel(self.channel)
        self.node_pool = []
        self.mainThread = threading.Thread(target=self.threadFunction)

    # Send a message to all nodes
    def send_message_to_nodes(self, type, data):
        for node in self.all_nodes:
            self.send_to_node(node, type, data)

    # Send a message to a single node
    def send_to_node(self, id, type, data):
        chans.sendMessage(id, type, data)

    def threadFunction(self):
        while (True):
            m = chans.getMessage(self.user.email)
            if (m != None and m.sender != ""):
                self.node_message(m.sender, m.type, m.content)
                print(m.toString())
            time.sleep(2)

    def start(self):
        self.mainThread.start()

    # On message receive - do something based on message type
    def node_message(self, connected_node, type, message):
        if type == "get_addr" :
            self.send_to_node(message, "mult_addr", self.get_neighbor_addresses())
        elif type == "mult_addr" :
            addresses = message.split(',')
            for address in addresses :
                if self.address_exists(address) == False:
                    self.node_pool.insert(address)
        elif type == "block" :
            block = Block("")
            block.init_from_message(message)
            print(block.toString())

    """
    # Limit connections to 8
    def connect_with_node(self, host, port):
        if len(self.all_nodes) < 8 :
            super().connect_with_node(host,port)

    # Connect with a node from the pool, and remove it from the pool
    def connect_with_pool_node(self):
        if len(self.node_pool) > 0:
            node = self.node_pool.pop()
            self.connect_with_node(node.host, node.port)
    """

    def address_exists(self, address):
        return address in self.node_pool

    # Return all neighbor addresses
    def get_neighbor_addresses(self):
        addresses = ""
        for addr in self.connected_nodes:
            addresses += addr + ','
        return addresses[0, len(addresses)-1]
