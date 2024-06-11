import time

from pensieve import Index, Model
from pensieve.submission import Submission

import tiktoken


class Processor:

    def __init__(self, model: Model = None, prompt: str = None):
        self.model = model
        self.system = prompt
        self.enc = None

    def run(self, item: Submission | Index):

        if isinstance(item, Submission):
            self._run(item)

        elif isinstance(item, Index):
            self._run_all(item)

    def _run_all(self, index: Index):

        for submission in index:
            self._run(submission)

    def _run(self, submission: Submission):

        print(f"Processing \"{submission.name}\"")

        if self.enc is None:
            self.enc = tiktoken.encoding_for_model("gpt-4o")

        num_tokens = len(self.enc.encode(submission.document.text))
        print(f" - using {num_tokens} tokens")

        try:
            submission.response = self.model.complete(system=self.system, user=submission.document.text)
            time.sleep(num_tokens / 10_000)  # Sleep longer for larger essays to avoid rate limit
        except Exception as e:
            pass
