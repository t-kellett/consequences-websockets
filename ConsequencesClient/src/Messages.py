from attr import dataclass


@dataclass
class InboundMessage:
    json: dict

    @property
    def message(self):
        return self.json["Message"]

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
