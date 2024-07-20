import socket, pickle

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def summary(self):
        print(f"My name is {self.name}, I am {self.age} years old!")

s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

s.bind(("0.0.0.0",4444))

s.listen()

c, addr = s.accept()

print(f"New connection from {addr[0]}\n")

person = pickle.loads(c.recv(1024))

person.summary()
