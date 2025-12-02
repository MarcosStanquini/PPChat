from api.rag.core.VectorStoreIngestor import VectorStoreIngestor
from huggingface_hub import  InferenceClient


def responseLLm(user_query):
    ingestor = VectorStoreIngestor(
        persist_dir="api/rag/vector_store/db/chroma"  
    )
    vectorstore = ingestor.load_vectorstore()
    print(vectorstore)
    top_3_chunks = vectorstore.similarity_search(user_query, 3)
    print(top_3_chunks)

    
    context = "\n\n---\n\n".join([
        f"[Página {chunk.metadata.get('page')}]\n{chunk.page_content}" 
        for chunk in top_3_chunks
    ])

    print("📝 Contexto montado!\n")
    prompt = f"""Com base no contexto abaixo, responda a pergunta de forma clara e objetiva.

    CONTEXTO:
    {context}

    PERGUNTA: {user_query}

    RESPOSTA:"""

    messages = [{"role": "user", "content": prompt}]
    client = InferenceClient("meta-llama/Meta-Llama-3-8B-Instruct")
    response = client.chat_completion(messages, max_tokens=600, temperature=0.3)

    return {"Resposta:": response.choices[0].message.content,
            "Contexto": context}

####
####resposta = response("O que fala a disciplina de computação meio ambiente e sociedade")
###print(resposta[0])
###print("//////////////////////")
###print(resposta[1])