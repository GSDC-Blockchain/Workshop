 GUIDELINES

    * Message structure : {type}|{data}
    * Message delimiter : |

    <--- Supported Message Types --->

    1. addr

    Nodes can advertise their address to the network, so that the whole network learns about them,
    by sending the address msg to their peers. The peers send the address to their peers, and the node initiator's address
    propagates through the whole network.
    It is important to note that peers will not accept an address if they already know it, and they will not send it to other nodes
    This means that a node can only advertise itself once

    2. get_addr

    This message means that a node wants to know new addresses. The node's peer gets all of it's peer addresses and sends it back
    to the node initiator

    <--- Nodes --->

    1. Seed Node -> a node that has been in the network for a long time, and is expected to stay in the network

    The seed node addresses should be well-known, and are present in system/system_parameters.py. When a node connects to
    the network, it first connects to a seed node