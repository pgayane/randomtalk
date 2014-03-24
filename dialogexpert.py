import random, time

class DialogExpert():

    
    def __init__(self, role):
        self.message_base = None
        self.MESSAGE_BASE_PATH = 'messagebase'
        self.THINK_TIME = 1
        self.role = role

    def load_message_base(self):
        if self.message_base is None:
            self.message_base = []
            
            with open(self.MESSAGE_BASE_PATH, 'r') as f:
                for line in f:
                    [role, message] = line.split(':')
                    if int(role) == self.role:
                        self.message_base.append(message.strip())

    def get_random_message(self):
        self.load_message_base()

        l = len(self.message_base)
        r = random.randint(0, l-1)

        return self.message_base[r]

    def think(self):
        time.sleep(self.THINK_TIME)
