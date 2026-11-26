RAG System – Workflow
RAG (Retrieval-Augmented Generation) allows an AI system to answer questions using information retrieved from provided documents.
1. Document Loading
- Load documents containing the knowledge or information.
- Extract text from the documents for processing.
2. Text Chunking
- Divide large documents into smaller chunks.
- Smaller chunks make information easier to process and retrieve.
- Maintain context using overlapping chunks if configured.
3. Multi-Chunking
- Generate multiple chunk sizes or chunk variations from the document.
- This helps experiment with different levels of context during retrieval.
4. Embedding Generation
- Convert text chunks into numerical vectors using an embedding model.
- These vectors represent the semantic meaning of the text.
5. Vector Storage
- Store generated embeddings along with their original text chunks.
- These vectors are used for similarity-based searching.
6. User Query Processing
- Accept a question from the user.
- Convert the question into an embedding using the same embedding model.
7. Retrieval
- Compare the user's query embedding with stored document embeddings.
- Identify the most relevant chunks based on semantic similarity.
8. Cosine Similarity
- Calculate cosine similarity between query and document vectors.
- Higher similarity scores indicate that the vectors are more closely aligned in meaning.
9. Context Generation
- Retrieve the most relevant chunks.
- Combine them to create contextual information for answering the question.
10. LLM Response Generation
- Send the user's question and retrieved context to the LLM.
- The LLM generates an answer based on the retrieved information.