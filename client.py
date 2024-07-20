import pickle
import socket

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def summary(self):
        print(f"My name is {self.name}, I am {self.age} years old!")


elliot = Person("Elliot Alderson", 28 )

host = "127.0.0.1"
port = 4444

s = socket.socket()

s.connect((host,port))

payload = pickle.dumps(elliot)

s.send(payload)
