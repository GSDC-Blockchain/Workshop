
TRANSACTION_DELIMITER = '-'
num = 0

class Transaction :
    def __init__(self):
        global num
        self.version = " "
        self.data = []
        self.locktime = 0
        self.number = num
        num+=1




