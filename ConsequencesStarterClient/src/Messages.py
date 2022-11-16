class InboundMessage:
    def __init__(self, json):
        self.json = json
        self.message = json["Message"]

    @property
    def players(self):
        if "Players" in self.json:
            return self.json["Players"]

    @property
    def question(self):
        if "Question" in self.json:
            return self.json["Players"]