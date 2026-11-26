from google import genai
import numpy as np

client= genai.Client()
text1="question1"
text2="question2"
# converting text into embedding(numerical), used tool- gemini-embedding-2
result1 = client.models.embed_content(                             
    model="gemini-embedding-2",
    contents=text1
)
result2 = client.models.embed_content(                             
    model="gemini-embedding-2",
    contents=text2
)
# print(result.embeddings)

# embedding vector(A vector is a list of numbers that represents the meaning of text in AI embeddings.)
vector1 = result1.embeddings[0].values
vector2 = result2.embeddings[0].values
# print(len(vector1))
# print(len(vector2))

def cosine_similarity(a,b):
    a=np.array(a)
    b=np.array(b)

    return np.dot(a,b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )


score= cosine_similarity(vector1, vector2)
print(score)