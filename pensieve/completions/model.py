from pensieve.documents import DocumentIndex, Document


class Model:

    def __init__(self, *args, **kwargs):
        self.system = None

    def system_prompt(self, prompt: str):
        raise NotImplementedError()

    def get_completions(self, documents: DocumentIndex):
        for document in documents:
            self.get_completion(document)

    def get_completion(self, document: Document):
        raise NotImplementedError()

