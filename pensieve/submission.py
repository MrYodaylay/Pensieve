from pathlib import Path

from pensieve import Document, Response


class Submission:
    """The Submission class is like a folder containing both the input file and the optional output file.
    It provides the same interface as the Document class itself."""

    _document: Document = None
    _response: Response = None

    def __init__(self, path: Path):
        self.directory = path.parent
        self.name = path.name

    @property
    def document(self) -> Document:
        if self._document is None:
            try:
                self._document = Document(self.directory.joinpath(self.name))
            except TypeError:
                pass
        return self._document

    @property
    def response(self) -> Response:
        return self._response

    @response.setter
    def response(self, response: str):
        self._response = Response(response)


