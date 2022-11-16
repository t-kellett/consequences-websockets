class InboundMessage:
    def __init__(self, json):
        self.json = json
        self.message = json["Message"]

    @property
    def players(self) -> list:
        if "Players" in self.json:
            return self.json["Players"]

    @property
    def question(self) -> str:
        if "Question" in self.json:
            return self.json["Question"]

    @property
    def results(self) -> list:
        if "Results" in self.json:
            return self.json["Results"]
