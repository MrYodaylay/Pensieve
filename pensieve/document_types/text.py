from pensieve.document import Document


class TextDocument(Document, file_types=[".txt"]):

    def _gen_text(self):
        with open(self.path, "r") as text_file:
            return text_file.read(1 * 1024 * 1024)  # Maximum file size 1MB
