import requests
import os
import json
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import joblib

def create_embedding(text_list):
    # https://github.com/ollama/ollama/blob/main/docs/api.md#generate-embeddings
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": text_list
    })

    embedding = r.json()["embeddings"] 
    return embedding


jsons = sorted(os.listdir("jsons"))  # List all the jsons 
my_dicts = []
chunk_id = 0

for json_file in jsons:
    with open(f"jsons/{json_file}") as f:
        content = json.load(f)
    print(f"Creating Embeddings for {json_file}")
    embeddings = create_embedding([c['text'] for c in content['chunks']])
       
    for i, chunk in enumerate(content['chunks']):
        chunk['chunk_id'] = chunk_id
        chunk['embedding'] = embeddings[i]
        chunk_id += 1
        my_dicts.append(chunk) 
        # if(i==3):  # Just do 5 chunks for testing
        #     break
    # break  # Just do 1 file for testing
df = pd.DataFrame.from_records(my_dicts)
#save this dataframe
joblib.dump(df,"embedding.joblib")
# print(df)
incoming_query=input("Ask a Question: ")
question_embedding=create_embedding([incoming_query])[0]

# print(question_embedding)
# a = create_embedding(["Cat sat on the mat", "Harry dances on a mat"])
# print(a)
#find similarities of question e,mbedding with all chunk embeddings
# print(np.vstack(df["embedding"].values))
# print(np.vstack(df["embedding"].values).shape)

similarities=cosine_similarity([question_embedding], np.vstack(df["embedding"].values)).flatten()
print(similarities)
top_results=3
max_indx=similarities.argsort()[::-1][0:top_results] #top 3 most similar chunks
print(max_indx)
new_df=df.iloc[max_indx]
print(new_df[["title", "number", "text"]])


