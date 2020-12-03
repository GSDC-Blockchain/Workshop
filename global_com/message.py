class _Message:
    def __init__(self, sender, type, content, created):
        self.sender=sender
        self.type=type
        self.content=content
        self.created=created
    # Create Message object from dictionary
    @staticmethod
    def from_dict(source):
        return _Message(source['sender'], source['type'], source['content'], source['created'])

    def to_dict(self):
        return {'sender': self.sender, 'type': self.type, 'content': self.content, 'created': self.created}

    # Return an array of messages from an array of documents
    @staticmethod
    def messages_from_arr(source):
        messages = []
        for message in source:
            messages.append(_Message.from_dict(message.to_dict()))
        return messages

    def print(self):
        print(" --- Message --- ")
        print("Sender: "+self.sender)
        print("Type: "+self.type)
        print("Content: "+str(self.content))
        print("Created: "+str(self.created))
        print(" --------------- ")