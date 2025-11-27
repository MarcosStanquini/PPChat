from sentence_transformers import SentenceTransformer

class EmbeddingModel:
    def __init__(self, model_name, chunk_list):
        self.model_name = model_name
        self.chunk_list = chunk_list
        self.model = SentenceTransformer(self.model_name)
        
    def encode_chunks(self):
        texts = [chunk.page_content for chunk in self.chunk_list]
        embeddings = self.model.encode(
            texts,
            normalize_embeddings=True,
            show_progress_bar=True
        )
        return embeddings
    
    def encode_query(self, query):
        embedding = self.model.encode(
            query,
            normalize_embeddings=True
        )
        return embedding
