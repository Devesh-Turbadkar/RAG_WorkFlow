from google import genai
import numpy as np

client = genai.Client()

documents = [
    "documents or text"
]

question = input("Ask your question:")

document_vectors = []

# Convert each document into an embedding vector
for document in documents:
    result = client.models.embed_content(
        model="gemini-embedding-2",
        contents=document
    )

    vector = result.embeddings[0].values
    document_vectors.append(vector)

# Convert the question into an embedding vector
question_result = client.models.embed_content(
    model="gemini-embedding-2",
    contents=question
)

question_vector = question_result.embeddings[0].values

# Calculate cosine similarity
def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)

    return np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )

# Compare the question with each document
best_score = -1
best_document = ""

for document, vector in zip(documents, document_vectors):
    score = cosine_similarity(question_vector, vector)

    if score > best_score:
        best_score = score
        best_document = document

if best_score >= 0.60:
    print("Answer:", best_document)
else:
    print("Sorry, I can only answer questions related to the provided documents.")

print(f"Similarity score: {round(best_score, 2)}")
# print("Your answer:", best_document)

