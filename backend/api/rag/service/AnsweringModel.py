import boto3
from botocore.config import Config

class AnsweringModel:
    def __init__(
        self,
        model_id="anthropic.claude-3-5-sonnet-20241022-v2:0",
        temperature=0.3,
        max_tokens=600,
        aws_region="us-east-1",
    ):
        config = Config(
            region_name=aws_region,
            retries={"max_attempts": 3, "mode": "adaptive"}
        )
        self.client = boto3.client("bedrock-runtime", config=config)
        self.model_id = model_id
        self.temperature = temperature
        self.max_tokens = max_tokens

    def answer(self, question: str, context: str) -> str:
        prompt = f"""Com base no contexto abaixo, responda a pergunta de forma clara e objetiva.

CONTEXTO:
{context}

PERGUNTA: {question}

RESPOSTA:"""

        response = self.client.converse(
            modelId=self.model_id,
            messages=[
                {
                    "role": "user",
                    "content": [{"text": prompt}]
                }
            ],
            inferenceConfig={
                "temperature": self.temperature,
                "maxTokens": self.max_tokens
            }
        )

        return response["output"]["message"]["content"][0]["text"]
