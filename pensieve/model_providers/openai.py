from openai import OpenAI

from pensieve import ModelProvider, Model


class OpenAIProvider(ModelProvider, provider_keys=["openai"]):

    def __init__(self, _):
        self.client = None
        self.system = ""

    def auth(self, auth_information: dict):
        self.client = OpenAI(
            api_key=auth_information["api-key"],
            organization=auth_information["organisation-id"],
            project=auth_information["project-id"]
        )

    def get_model(self, model_key: str):
        return GPTModel(self.client, model_key)


class GPTModel(Model):

    def __init__(self, client, model_key: str, *args, **kwargs):
        super().__init__()
        self.client = client
        self.model_key = model_key

    def system_prompt(self, prompt: str):
        self.system = prompt

    def get_completion(self, document):
        completion = self.client.chat.completions.create(
            model=self.model_key,
            messages=[
                {"role": "system", "content": self.system},
                {"role": "user", "content": document.plain_text}
            ]
        )
        print(completion.choices[0].message.content)
