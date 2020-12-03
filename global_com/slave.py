from global_com.auth import User
from global_com.message import _Message
from global_com.message_channel import _MessageChannel
from global_com.chan import chans
from global_com.settings import SETTINGS
import time
# Don't let anyone send messages to themselves, or send messages to 'confirm pools'

class Slave:
    def __init__(self, user):
        self.user = user
        self.channel = _MessageChannel(user)

    def confirm(self, content):
        master = SETTINGS['MASTER_ADDR']
        chans.sendConfirmMessage(master, self.user.email, "confirm", content)

        # WAIT / sleep for 10 seconds
        time.sleep(SETTINGS['CONFIRM_WAITING_TIME'])

        msg = _Message.from_dict(chans.getConfirmMessage(self.user.email).to_dict())

        print(msg.toString())

        return msg.content == "confirm"

