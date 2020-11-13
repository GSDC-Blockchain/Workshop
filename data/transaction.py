
TRANSACTION_DELIMITER = '-'
num = 0

class Transaction :
    def __init__(self):
        global num
        self.version = " "
        self.inputCounter = 0
        self.inputs = []
        self.outputCounter = 0
        self.outputs = []
        self.locktime = 0
        self.number = num
        num+=1


