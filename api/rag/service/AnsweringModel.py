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
        prompt = (
            f"Responda de forma direta, objetiva e baseada EXCLUSIVAMENTE no contexto abaixo.\n"
            f"Se o contexto não tiver a resposta, diga apenas: 'Não tenho informação suficiente.'\n\n"
            f"Contexto:\n{context}\n\n"
            f"Pergunta:\n{question}\n\n"
            f"Resposta:"
        )


        response = self.client.chat_completion(
            messages=[{"role": "user", "content": prompt}],
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )

        return response.choices[0].message.content
