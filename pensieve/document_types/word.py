import docx2txt

from pensieve.document import Document


class WordDocument(Document, file_types=[".docx"]):

    def _gen_text(self):
        return docx2txt.process(self.path)

