from google import genai
from dotenv import load_dotenv

load_dotenv()

client= genai.Client()

# converting text into embedding(numerical), used tool- gemini-embedding-2
result = client.models.embed_content(                             
    model="gemini-embedding-2",
    contents="question"
)
# print(result.embeddings)

# embedding vector(A vector is a list of numbers that represents the meaning of text in AI embeddings.)
vector = result.embeddings[0].values
print(vector[:10])