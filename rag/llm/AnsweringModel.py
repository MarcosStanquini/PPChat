import transformers
import torch

class AnsweringModel:
    def __init__(self, model_name, dtype=torch.bfloat16, device_map="auto"):
        self.model_name = model_name
        self.pipeline = transformers.pipeline(
            "text-generation",
            model=self.model_name,
            model_kwargs={"dtype": dtype},
            device_map=device_map,
        )

    def answer(self, messages, max_tokens=256):
        outputs = self.pipeline(messages, max_new_tokens=max_tokens)
        return outputs[0]["generated_text"]
