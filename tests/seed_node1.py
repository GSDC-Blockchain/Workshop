from global_com import firebase_api
from global_com.auth import User
from global_com.chan import chans
from global_com.message_channel import _MessageChannel

from data.block import Block
from networking.seed_node import SeedNode


# Double \
firebase_api.database.setup("C:\\Users\\Filip\\Desktop\\setup.json")
chans.setup()

u = User.login("filipdj98@gmail.com", "filip")

seed_n = SeedNode(u)


u2 = User.login("milan@gmail.com", "mmm")

msgChan = _MessageChannel(u2)
b = Block("")
chans.addChannel(msgChan)

chans.sendMessage('filipdj98@gmail.com',u2.email,'block', b.toString())


seed_n.start()