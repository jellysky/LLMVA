!pip install langchain
!pip install openai
!pip install tiktoken
!pip install chromadb
!pip install pypdf
!pip install unstructured==0.7.12
!pip install llama-index

import os
os.environ['OPENAI_API_KEY'] = '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'
pdf_folder_path = 'LLM_VirtualAsistant_codeA/MangrovePDFs'

from pathlib import Path
from llama_index.core import download_loader
PDFReader = download_loader("PDFReader")
from llama_index.core import SimpleDirectoryReader
documents = SimpleDirectoryReader(pdf_folder_path).load_data()

#vector index designed to work with text embeddings generated by the GPT (Generative Pre-trained Transformer) language models,
#which are part of the Transformer architecture

from llama_index.core import GPTVectorStoreIndex
index = GPTVectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()

