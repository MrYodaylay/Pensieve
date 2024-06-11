from pypdf import PdfReader

from pensieve.document import Document


class PdfDocument(Document, file_types=[".pdf"]):

    def _gen_text(self):

        reader = PdfReader(self.path)

        text = ""
        for page in reader.pages:
            text += page.extract_text()

        return text
