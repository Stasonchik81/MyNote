import datetime
import json

class Note:
    def __init__(self, title, message, number) -> None:
        self.title = title
        self.message = message
        self.date = datetime.datetime.now()
        self.id = number

class NoteEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Note):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj) 

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()  
    
    
