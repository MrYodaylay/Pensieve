from pensieve import DocumentIndex, Document


class Model:

    def __init__(self, *args, **kwargs):
        self.system = None

    def system_prompt(self, prompt: str):
        raise NotImplementedError()

    def get_completion(self, document: Document | DocumentIndex):
        raise NotImplementedError()

