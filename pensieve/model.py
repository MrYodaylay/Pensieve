from pensieve import Index, Document


class Model:

    def __init__(self, *args, **kwargs):
        self.prompt = None

    def set_prompt(self, prompt: str):
        raise NotImplementedError()

    def complete(self, system: str, user: str):
        raise NotImplementedError()

