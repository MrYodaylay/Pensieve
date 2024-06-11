from pathlib import Path


class Response:

    def __init__(self, text: str):
        self._text = text

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text: str):
        self._text = text

    @property
    def lines(self):
        return [line for line in self._text.splitlines() if line.strip() != ""]

    def write(self, path: Path):
        with open(path, "w") as output_file:
            output_file.write(self._text)
