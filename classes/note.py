import datetime

class Note:
    def __init__(self, title, message) -> None:
        self.title = title
        self.message = message
        self.date = datetime.datetime.now()
    def display_info(self):
        print(f"{self.date}\t{self.title}\t{self.message}")