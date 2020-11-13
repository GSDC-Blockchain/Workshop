import time

from networking.seed_node import SeedNode


# Node usage

node = SeedNode("192.168.0.12", 10001)
time.sleep(1)

# Do not forget to start your node!
node.start()
time.sleep(1)

# Connect with another node, otherwise you do not create any network!
node.connect_with_node('192.168.253.1', 10001)
time.sleep(2)

# Example of sending a message to the nodes (dict).
node.send_message_to_nodes("msg", "aa")

time.sleep(5) # Create here your main loop of the application

node.stop()


