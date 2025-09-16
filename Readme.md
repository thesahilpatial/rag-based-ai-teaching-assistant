# How to use this RAG AI Teaching assistant on your own data
## Step 1 - Collect your videos
Move all your video files to the videos folder

## Step 2 - Convert to mp3
Convert all the video files to mp3 by ruunning video_to_mp3

## Step 3 - Convert mp3 to json 
Convert all the mp3 files to json by ruunning mp3_to_json

## Step 4 - Convert the json files to Vectors
Use the file preprocess_json to convert the json files to a dataframe with Embeddings and save it as a joblib pickle

## Step 5 - Prompt generation and feeding to LLM

Read the joblib file and load it into the memory. Then create a relevant prompt as per the user query and feed it to the LLM


<img width="2930" height="1778" alt="image" src="https://github.com/user-attachments/assets/9e1459eb-d8ce-406b-89ca-b1ade02fbeb9" />
<img width="2746" height="1152" alt="image" src="https://github.com/user-attachments/assets/89ae2c2a-2441-49d0-9f14-31c6d0fef763" />
<img width="2298" height="1098" alt="image" src="https://github.com/user-attachments/assets/8256817c-b0b7-4eab-a18a-6bba4bca3901" />


