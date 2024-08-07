from datetime import datetime
class Telegram:
    def __init__(self, user_name):
        self.user_name = user_name
        self.received = []
        self.status = ""
        self.unread = []

    def send(self, receiver, msg):
        current_time = datetime.now().time().strftime("%H:%M:%S")
        message = {"sender": self.user_name, 'msg': msg, 'time': current_time, 'from': self}
        receiver.unread.append(message)
        receiver.received.append(message)
        self.status = 'Sent'

    def receive(self):
        if len(self.unread) == 0:
            print("Yangi xabarlar mavjud emas!")
        else:
            print("Yangi xabarlar:")
            for i in self.unread:
                print(f"{i['sender']}: {i['msg']}, {i['time']}")
                self.unread.remove(i)
                i['from'].status = "Read"

    def receiveds(self):
        if len(self.unread) == 0:
            print("Xabarlar mavjud emas!")
        else:
            for i in self.received:
                print(f"{i['sender']}: {i['msg']}, {i['time']}")
            
    def stat(self):
        print("Status:", self.status)



user1 = Telegram("User 1")
user2 = Telegram("User 2")

user1.send(user2, "Salom to user2")
user1.stat()
user2.receive()
user1.stat()
user2.receive()
print("============================")
user2.send(user1, "Salom to user1")
user2.stat()
user1.receive()
user2.stat()
user1.receive()