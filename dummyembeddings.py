#Definition of my Embeddings class
# langchain_core.embeddings.embeddings.Embeddings
from langchain_core.embeddings import Embeddings
import numpy as np
import json

class DummyEmbeddings(Embeddings):
    def __init__(self):
        pass

    def embed_documents(self, texts):
        #list of json array strings is expected, with all json arrays having the same length.
        vectors = []
        for text in texts:
          vectors.append(json.loads(text))
        return vectors

    def embed_query(self, text):
        #json array string is expected
        return json.loads(text)