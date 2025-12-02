from huggingface_hub import InferenceClient

class AnsweringModel:
    def __init__(
        self,
        model_name="meta-llama/Meta-Llama-3-8B-Instruct",
        temperature=0.3,
        max_tokens=600,
    ):
        self.client = InferenceClient(model_name)
        self.temperature = temperature
        self.max_tokens = max_tokens

    def answer(self, question: str, context: str) -> str:
        prompt = f"""Com base no contexto abaixo, responda a pergunta de forma clara e objetiva.

CONTEXTO:
{context}

PERGUNTA: {question}

RESPOSTA:"""


        response = self.client.chat_completion(
            messages=[{"role": "user", "content": prompt}],
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )

        return response.choices[0].message.content
