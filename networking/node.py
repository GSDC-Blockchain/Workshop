import time

from global_com.auth import User
from global_com.firebase_api import database
from global_com.message import _Message
from global_com.settings import SETTINGS

from data.block import Block
from data.blockchain import Blockchain
from data.genesis_block import *

from global_com.master import Master
from global_com.message_channel import _MessageChannel
from global_com.chan import chans
import threading
import time
MAX_CONNECTED_NODES = 8

class Node:
    # Python class constructor
    def __init__(self, user):
        self.user = user
        self.channel = _MessageChannel(user)
        chans.addChannel(self.channel)
        self.node_pool = []
        self.mainThread = threading.Thread(target=self.threadFunction)
        self.connected_nodes = []
        self.blockchain = Blockchain()
        self.connection_error = False

        database.deleteAllDocuments(self.channel.getMessagesPath())
        database.deleteAllDocuments(self.channel.getConfirmPath())
        self.start()

    def confirm(self, content):
        master = SETTINGS['MASTER_ADDR']
        chans.addChannel(_MessageChannel(User(email=master)))
        chans.sendConfirmMessage(master, self.user.email, "confirm", content)

        # WAIT / sleep for 10 seconds
        time.sleep(SETTINGS['CONFIRM_WAITING_TIME'])

        msg =  _Message.from_dict(chans.getConfirmMessage(self.user.email).to_dict())

        #print(msg.toString())

        return msg

    # Send a message to all nodes
    def send_message_to_all_connected_nodes(self, type, data):
        for node in self.connected_nodes:
            self.send_to_node(node, type, data)

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

    def get_connected_nodes(self):
        return self.connected_nodes

    def advertise(self):
        self.send_message_to_all_connected_nodes("addr", self.user.email)

    # On message receive - do something based on message type
    def node_message(self, sender, type, message):
        if type == "get_addr":
            self.send_to_node(sender, "mult_addr", self.get_neighbor_addresses())
        elif type == "mult_addr":
            addresses = message.split(',')
            for address in addresses:
                self.node_pool.append(address)
        elif type == "addr":
            if message not in self.node_pool and message not in self.connected_nodes:
                self.node_pool.append(message)
                self.send_message_to_all_connected_nodes("addr", message)
        elif type == "block":
            self.block_function()
        elif type == "connect":
            if len(self.connected_nodes) < 8:
                self.send_to_node(sender, "connected", "")
        elif type == "connected":
            print("CONNECTED")
            self.connection_error = False
        elif type == "get_blockchain":
            for key, block in self.blockchain.items():
                self.send_to_node(sender, 'block', block.toString())
        elif type == "error":
            print("error: " + message)
        else:
            self.send_to_node(sender, "error", "")

    # TODO Should be implemented by the user
    def block_function(self, message):
        # check the hash!
        # check the block
        # insert into blockchain
        # send blockchain to master
        pass


    # When someone creates a block:
    # First sends it to the master for confirmation, then sends it to other nodes


    # Limit connections to 8
    def connect_with_node(self, nodeId):
        if len(self.connected_nodes) < 8 :
            chans.addChannel(_MessageChannel(User(email=nodeId)))
            self.connected_nodes.append(nodeId)
            self.connection_error = True
            print("CONNECTING to "+nodeId)
            self.send_to_node(nodeId, "connect", "")

            time.sleep(5)

            if self.connection_error == True:
                print("NOT CONNECTED")
                self.disconnect_from_node(nodeId)
            return True

        return False

    def disconnect_from_node(self, nodeId):
        if nodeId in self.connected_nodes:
            self.connected_nodes.remove(nodeId)

    # Connect with a node from the pool, and remove it from the pool
    def connect_with_pool_node(self):
        node = self.node_pool.pop()
        if not self.connect_with_node(node):
            self.node_pool.insert(node)

    def address_exists(self, address):
        return address in self.node_pool

    # Return all neighbor addresses
    def get_neighbor_addresses(self):
        addresses = ""
        for addr in self.connected_nodes:
            addresses += addr + ','
        return addresses[0: len(addresses)-1]
