from google import genai
import numpy as np

client= genai.Client()

documents = ["add your documents or text"
]

question = input("Enter Your Question:")


document_vector=[]

for document in documents:
    result= client.models.embed_content(
        model="gemini-embedding-2",
        contents=document
    )

    vector=result.embeddings[0].values

    document_vector.append(vector)


question_result= client.models.embed_content(
    model="gemini-embedding-2",
    contents=question
)
question_vector= question_result.embeddings[0].values


def cosine_similarity(a,b):
    a=np.array(a)
    b=np.array(b)

    return np.dot(a,b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )

scores=[]

for item in document_vector:
    score= cosine_similarity(
        question_vector,
        item
    )

    scores.append(score)

best_index = np.argmax(scores)
best_score = scores[best_index]
print(best_score)

if best_score >= 0.70:
    best_doc= documents[best_index]
    print(best_doc)
else:
    print("Question is Not Valid:")

