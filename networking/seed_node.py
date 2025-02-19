
import time

from data.block import Block
from data.genesis_block import *
from global_com.auth import User

from global_com.master import Master
from global_com.message_channel import _MessageChannel
from global_com.chan import chans

import threading

from system import system_parameters

MAX_CONNECTED_NODES = 8


class SeedNode:

    # Python class constructor
    def __init__(self, user):
        self.user = user
        self.channel = _MessageChannel(user)
        chans.addChannel(self.channel)
        self.node_pool = []
        self.mainThread = threading.Thread(target=self.threadFunction)
        self.starting_addresses = ['addr1']


    # Send a message to a single node
    def send_to_node(self, id, type, data):
        chans.addChannel(_MessageChannel(User(email=id)))
        chans.sendMessage(id, self.user.email, type, data)

    def threadFunction(self):
        while (True):
            m = chans.getMessage(self.user.email)
            if (m != None and m.sender != ""):
                self.node_message(m.sender, m.type, m.content)
                #print(m.toString())
            time.sleep(2)

    def start(self):
        self.mainThread.start()

    # On message receive - do something based on message type
    def node_message(self, sender, type, message):
        # Return only the starting addresses
        if type == "get_addr" :
           # print(self.get_starting_addresses())
            self.send_to_node(sender, "mult_addr", self.get_starting_addresses())
        elif type == "connect":
            self.send_to_node(sender, "connected", "")
        else:
            self.send_to_node(sender, "error", "")

    # Return all neighbor addresses
    def get_starting_addresses(self):
        addresses = ""
        for addr in self.starting_addresses:
            addresses += addr + ','
        return addresses[0: len(addresses)-1]

seed_node = SeedNode(User(email=system_parameters.SEED_NODE))