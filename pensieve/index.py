import pathlib

from pensieve.document import Document


class DocumentIndex:

    def __init__(self, path: pathlib.Path):

        path = path.resolve()
        if not path.exists():
            raise FileNotFoundError(f"Path \"{path}\" cannot be found.")

        self._documents = list()

        if path.is_dir():
            self._import_directory(path)
            self.base_path = path

        elif path.is_file():
            self._import_file(path)
            self.base_path = path.parent

        else:
            raise FileNotFoundError(f"Path \"{path}\" is neither a file nor directory.")

    def __iter__(self):
        return self._documents.__iter__()

    def _import_directory(self, directory: pathlib.Path):

        for file in directory.iterdir():
            self._import_file(file)

    def _import_file(self, file: pathlib.Path):

        if (
                file.is_file() and
                file.suffix in Document._filetype_registry
        ):
            self._documents.append(Document(file))

    def get_document(self, i: int):
        return self._documents[i]
