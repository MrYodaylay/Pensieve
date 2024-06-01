import pathlib


class Document:
    """The Document class represents an input file that is on disk, such as a PDF or DOCX file. The reading and
    processing of the files is delegated to subclasses, in the document_types submodule"""

    _filetype_registry = dict()

    def __init_subclass__(cls, file_types: list[str] = None, **kwargs):
        if file_types is None:
            raise TypeError(f'{cls.__name__} must include one or more file_types')

        super().__init_subclass__(**kwargs)

        for file_type in file_types:
            Document._filetype_registry[file_type] = cls

    def __new__(cls, path: pathlib.Path, **kwargs):
        subclass = cls._filetype_registry.get(path.suffix.lower())

        if subclass is None:
            raise TypeError(f'No valid implementation for \"{path.suffix.lower()}\" found')

        return super().__new__(subclass)

    def __init__(self, path: pathlib.Path):
        self.path = path
        self._plain_text = None

    @property
    def plain_text(self):
        if self._plain_text is None:
            self._plain_text = self._gen_plain_text()

        return self._plain_text

    def _gen_plain_text(self):
        raise NotImplementedError()


