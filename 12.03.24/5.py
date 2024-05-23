class Mail:
    def __init__(self, sender, receiver, message):
        self.sender = sender
        self.receiver = receiver
        self.message = message

class MailServer:
    def __init__(self, name):
        self.name = name
        self.inbox = []

    def receive_mail(self):
        if self.inbox:
            mail = self.inbox.pop(0)
            return mail
        else:
            return None

    def send_mail(self, receiver_server, mail):
        receiver_server.inbox.append(mail)


class MailClient:
    def __init__(self, server, user):
        self.server = server
        self.user = user

    def receive_mail(self):
        mail = self.server.receive_mail()
        if mail:
            return f"Received mail from {mail.sender}: {mail.message}"
        else:
            return "No new mail"

    def send_mail(self, receiver_server, receiver_user, message):
        mail = Mail(self.user, receiver_user, message)
        self.server.send_mail(receiver_server, mail)
        return f"Sent mail to {receiver_user} on {receiver_server.name}"

server1 = MailServer("Server1")
server2 = MailServer("Server2")

client1 = MailClient(server1, "user1")
client2 = MailClient(server2, "user2")


print(client1.send_mail(server2, "user2", "hello from user1"))
print(client2.receive_mail())