from flask import Flask, request
import base64
import pickle

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def summary(self):
        return f"My name is {self.name}, I am {self.age} years old!"


app = Flask(__name__)

@app.route("/summary")
def get_summary():
    # Just loading the object and calling the summary method using pickle
    person_object = request.args.get("person")
    if person_object is None:
        return "missing person parameter"
    # since we are receiving a string we need to convert it to bytes
    person = pickle.loads(base64.b64decode(person_object))

    return f"{person.summary()}"

@app.route("/create")
def create_person():
    name = request.args.get("name")
    age = request.args.get("age")

    if name is None:
        return "missing name parameter"
    if age is None:
        return "missing age parameter"

    new_person = Person(name,int(age))
    return f"{base64.b64encode(pickle.dumps(new_person)).decode()}"
