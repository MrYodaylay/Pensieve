from openai import OpenAI

from pensieve import ModelProvider, Model


class OpenAIProvider(ModelProvider, provider_keys=["openai"]):

    def __init__(self, *args, auth: dict = None):
        self.client = OpenAI(
            api_key=auth["api-key"],
            organization=auth["organisation-id"],
            project=auth["project-id"]
        )

    def get_model(self, model_key: str, prompt: str = None):
        return GPTModel(self.client, model_key)


class GPTModel(Model):

    def __init__(self, client, model_key: str):
        super().__init__()
        self.client = client
        self.model_key = model_key

    def complete(self, system: str, user: str) -> str:
        # TODO: Check for openai.RateLimitError, implement exponential backoff if hit
        completion = self.client.chat.completions.create(
            model=self.model_key,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user}
            ]
        )
        return completion.choices[0].message.content.encode("utf-8").decode()
